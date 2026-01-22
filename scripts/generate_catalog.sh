#!/bin/bash
#
# Catalog Generator for AI System Prompts Repository
#
# This script scans the repository and generates a comprehensive CATALOG.md file
# documenting all AI tools, their prompts, tool definitions, and metadata.
#
# Usage:
#     ./scripts/generate_catalog.sh
#
# Features:
# - Automatically discovers all prompt and tool files
# - Extracts metadata (file size, line count)
# - Organizes by category (Commercial, Open Source, etc.)
# - Generates a searchable index with links
#

set -e

# Get the repository root (parent of scripts directory)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
OUTPUT_FILE="$REPO_ROOT/CATALOG.md"

# Directories to skip
SKIP_DIRS=".git .github assets scripts __pycache__ node_modules"

# Counters
total_files=0
total_tools=0
total_size=0

# Function to format file size
format_size() {
    local size=$1
    if [ "$size" -lt 1024 ]; then
        echo "${size} B"
    elif [ "$size" -lt 1048576 ]; then
        echo "$(( size / 1024 )) KB"
    else
        echo "$(( size / 1048576 )) MB"
    fi
}

# Function to classify file type based on name/extension
classify_file() {
    local filename="$1"
    local basename=$(basename "$filename" | tr '[:upper:]' '[:lower:]')
    local ext="${basename##*.}"

    case "$ext" in
        json)
            echo "🔧 Tool Definition"
            ;;
        yaml|yml)
            echo "⚙️ Configuration"
            ;;
        md)
            echo "📝 Documentation"
            ;;
        txt)
            if [[ "$basename" == *"tool"* ]]; then
                echo "🔧 Tool Definition"
            elif [[ "$basename" == *"system"* ]]; then
                echo "🤖 System Prompt"
            elif [[ "$basename" == *"action"* ]]; then
                echo "⚡ Action"
            else
                echo "💬 Prompt"
            fi
            ;;
        *)
            echo "📄 File"
            ;;
    esac
}

# Function to get category for a tool
get_category() {
    local tool_name="$1"
    case "$tool_name" in
        "Claude Code"|"Anthropic")
            echo "Anthropic"
            ;;
        "Google"|"Google/"*|"Gemini")
            echo "Google"
            ;;
        "VSCode Agent"|"Cursor Prompts"|"Windsurf"|"Amp")
            echo "IDE Extensions"
            ;;
        "v0 Prompts and Tools"|"Same.dev"|"Lovable"|"Replit"|"Leap.new")
            echo "Web Platforms"
            ;;
        "Bolt"|"Cline"|"Codex CLI"|"Gemini CLI"|"Lumo"|"RooCode")
            echo "Open Source"
            ;;
        *)
            echo "Commercial Tools"
            ;;
    esac
}

# Function to extract first meaningful line as description
get_description() {
    local filepath="$1"
    local ext="${filepath##*.}"

    # For JSON files, just note it's a tool definition
    if [ "$ext" = "json" ]; then
        local count=$(grep -c '"name"' "$filepath" 2>/dev/null || echo "0")
        if [ "$count" -gt 0 ]; then
            echo "Tool definitions ($count tools)"
        else
            echo "JSON configuration"
        fi
        return
    fi

    # For text files, get first meaningful line
    local desc=$(head -20 "$filepath" 2>/dev/null | grep -v '^$' | grep -v '^#' | grep -v '^---' | grep -v '^<' | grep -v '^Knowledge cutoff' | grep -v '^Image input' | head -1 | cut -c1-60)

    if [ -n "$desc" ]; then
        echo "${desc}..."
    else
        echo "System prompt / configuration"
    fi
}

# Start generating catalog
echo "Generating catalog..."

# Create temporary file
TEMP_FILE=$(mktemp)

# Write header
cat > "$TEMP_FILE" << 'EOF'
# AI System Prompts Catalog

> Auto-generated catalog of all AI system prompts and tool definitions in this repository.
>
> Run `./scripts/generate_catalog.sh` to regenerate this file.

---

## Quick Navigation

- [Anthropic](#anthropic) - Claude and Anthropic tools
- [Google](#google) - Google AI tools
- [IDE Extensions](#ide-extensions) - Code editor integrations
- [Web Platforms](#web-platforms) - Web-based AI tools
- [Commercial Tools](#commercial-tools) - Commercial AI products
- [Open Source](#open-source) - Open source AI tools

---

EOF

# Collect all tools and their files
declare -A TOOLS
declare -A TOOL_CATEGORIES

# Scan top-level directories
for dir in "$REPO_ROOT"/*/; do
    dir_name=$(basename "$dir")

    # Skip certain directories
    if echo "$SKIP_DIRS" | grep -qw "$dir_name"; then
        continue
    fi

    # Handle Open Source prompts specially
    if [ "$dir_name" = "Open Source prompts" ]; then
        for subdir in "$dir"/*/; do
            if [ -d "$subdir" ]; then
                sub_name=$(basename "$subdir")
                TOOL_CATEGORIES["$sub_name"]="Open Source"
                TOOLS["$sub_name"]="$subdir"
                ((total_tools++)) || true
            fi
        done
        continue
    fi

    # Handle Google subdirectories
    if [ "$dir_name" = "Google" ]; then
        for subdir in "$dir"/*/; do
            if [ -d "$subdir" ]; then
                sub_name="Google/$(basename "$subdir")"
                TOOL_CATEGORIES["$sub_name"]="Google"
                TOOLS["$sub_name"]="$subdir"
                ((total_tools++)) || true
            fi
        done
        continue
    fi

    # Regular directory
    TOOL_CATEGORIES["$dir_name"]=$(get_category "$dir_name")
    TOOLS["$dir_name"]="$dir"
    ((total_tools++)) || true
done

# Generate sections by category
for category in "Anthropic" "Google" "IDE Extensions" "Web Platforms" "Commercial Tools" "Open Source"; do
    echo "" >> "$TEMP_FILE"
    echo "## $category" >> "$TEMP_FILE"
    echo "" >> "$TEMP_FILE"

    # Find all tools in this category
    found_any=false
    for tool_name in $(echo "${!TOOL_CATEGORIES[@]}" | tr ' ' '\n' | sort); do
        if [ "${TOOL_CATEGORIES[$tool_name]}" = "$category" ]; then
            tool_dir="${TOOLS[$tool_name]}"

            # Check if directory has relevant files
            files=$(find "$tool_dir" -maxdepth 1 -type f \( -name "*.txt" -o -name "*.json" -o -name "*.yaml" -o -name "*.yml" \) 2>/dev/null | grep -v -i readme || true)

            if [ -n "$files" ]; then
                found_any=true
                echo "### $tool_name" >> "$TEMP_FILE"
                echo "" >> "$TEMP_FILE"
                echo "| File | Type | Size | Lines | Description |" >> "$TEMP_FILE"
                echo "|------|------|------|-------|-------------|" >> "$TEMP_FILE"

                while IFS= read -r filepath; do
                    if [ -f "$filepath" ]; then
                        filename=$(basename "$filepath")
                        file_type=$(classify_file "$filepath")
                        file_size=$(stat -f%z "$filepath" 2>/dev/null || stat -c%s "$filepath" 2>/dev/null || echo "0")
                        size_str=$(format_size "$file_size")
                        line_count=$(wc -l < "$filepath" 2>/dev/null | tr -d ' ')
                        description=$(get_description "$filepath")

                        # Create relative path for link
                        rel_path="${filepath#$REPO_ROOT/}"
                        link_path=$(echo "$rel_path" | sed 's/ /%20/g')

                        echo "| [$filename]($link_path) | $file_type | $size_str | $line_count | $description |" >> "$TEMP_FILE"

                        ((total_files++)) || true
                        total_size=$((total_size + file_size))
                    fi
                done <<< "$files"

                echo "" >> "$TEMP_FILE"
            fi
        fi
    done

    if [ "$found_any" = false ]; then
        echo "*No tools found in this category.*" >> "$TEMP_FILE"
        echo "" >> "$TEMP_FILE"
    fi

    echo "---" >> "$TEMP_FILE"
done

# Add summary statistics at the top (after header)
SUMMARY=$(cat << EOF

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total AI Tools | $total_tools |
| Total Files | $total_files |
| Total Size | $(format_size $total_size) |

EOF
)

# Insert summary after the header
sed -i.bak "s/## Quick Navigation/$SUMMARY\n## Quick Navigation/" "$TEMP_FILE" 2>/dev/null || \
    sed "s/## Quick Navigation/$SUMMARY\n## Quick Navigation/" "$TEMP_FILE" > "${TEMP_FILE}.new" && mv "${TEMP_FILE}.new" "$TEMP_FILE"

# Add legend at the end
cat >> "$TEMP_FILE" << 'EOF'

## Legend

| Icon | Type |
|------|------|
| 💬 | Prompt - Instructions for AI behavior |
| 🤖 | System Prompt - Core system instructions |
| 🔧 | Tool Definition - JSON schemas for tools |
| ⚙️ | Configuration - YAML/settings files |
| ⚡ | Action - Specific action prompts |
| 📝 | Documentation - Markdown docs |
| 📄 | File - Other file types |

---

*This catalog was auto-generated. For accurate, up-to-date information, regenerate with `./scripts/generate_catalog.sh`*
EOF

# Move temp file to final location
mv "$TEMP_FILE" "$OUTPUT_FILE"

echo "Catalog generated: $OUTPUT_FILE"
echo "Total tools: $total_tools"
echo "Total files: $total_files"
echo "Total size: $(format_size $total_size)"
