#!/usr/bin/env python3
"""
Catalog Generator for AI System Prompts Repository

This script scans the repository and generates a comprehensive CATALOG.md file
documenting all AI tools, their prompts, tool definitions, and metadata.

Usage:
    python scripts/generate_catalog.py

Features:
- Automatically discovers all prompt and tool files
- Extracts metadata (file size, line count, brief description)
- Organizes by category (Commercial, Open Source, etc.)
- Generates a searchable index with links
- Tracks file types (prompts, tools, configs)
"""

import os
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict


# File type classifications
PROMPT_EXTENSIONS = {'.txt'}
TOOL_EXTENSIONS = {'.json'}
CONFIG_EXTENSIONS = {'.yaml', '.yml'}
DOC_EXTENSIONS = {'.md'}

# Directories to skip
SKIP_DIRS = {'.git', '.github', 'assets', 'scripts', '__pycache__', 'node_modules'}

# Known categories for organization
OPEN_SOURCE_TOOLS = {'Bolt', 'Cline', 'Codex CLI', 'Gemini CLI', 'Lumo', 'RooCode'}


def get_file_stats(filepath: Path) -> dict:
    """Get basic statistics about a file."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            lines = content.count('\n') + 1
            words = len(content.split())

        size_bytes = filepath.stat().st_size

        # Format size
        if size_bytes < 1024:
            size_str = f"{size_bytes} B"
        elif size_bytes < 1024 * 1024:
            size_str = f"{size_bytes / 1024:.1f} KB"
        else:
            size_str = f"{size_bytes / (1024 * 1024):.1f} MB"

        return {
            'lines': lines,
            'words': words,
            'size': size_str,
            'size_bytes': size_bytes
        }
    except Exception as e:
        return {'lines': 0, 'words': 0, 'size': 'N/A', 'size_bytes': 0, 'error': str(e)}


def extract_brief_description(filepath: Path, max_chars: int = 200) -> str:
    """Extract a brief description from the first meaningful lines of a file."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read(1000)  # Read first 1000 chars

        # For JSON files, try to get a description field
        if filepath.suffix == '.json':
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                if isinstance(data, list) and len(data) > 0:
                    return f"Tool definitions ({len(data)} tools)"
                elif isinstance(data, dict):
                    if 'description' in data:
                        return data['description'][:max_chars]
                    return f"Configuration with {len(data)} keys"
            except:
                pass

        # For text/yaml files, get first meaningful line
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines, headers, and common boilerplate
            if not line:
                continue
            if line.startswith('#') or line.startswith('---') or line.startswith('<'):
                continue
            if line.startswith('Knowledge cutoff:') or line.startswith('Image input'):
                continue
            # Return first meaningful content
            if len(line) > 20:
                return line[:max_chars] + ('...' if len(line) > max_chars else '')

        return "System prompt / configuration"
    except Exception:
        return "Unable to extract description"


def classify_file_type(filepath: Path) -> str:
    """Classify the type of file based on name and extension."""
    name = filepath.name.lower()
    suffix = filepath.suffix.lower()

    if suffix in TOOL_EXTENSIONS:
        return "🔧 Tool Definition"
    elif suffix in CONFIG_EXTENSIONS:
        return "⚙️ Configuration"
    elif suffix in DOC_EXTENSIONS:
        return "📝 Documentation"
    elif 'tool' in name:
        return "🔧 Tool Definition"
    elif 'prompt' in name:
        return "💬 Prompt"
    elif 'system' in name:
        return "🤖 System Prompt"
    elif 'action' in name:
        return "⚡ Action"
    elif suffix in PROMPT_EXTENSIONS:
        return "💬 Prompt"
    else:
        return "📄 File"


def get_tool_category(tool_dir: str) -> str:
    """Determine the category for a tool."""
    if tool_dir in OPEN_SOURCE_TOOLS:
        return "Open Source"
    elif tool_dir.startswith('Open Source'):
        return "Open Source"
    elif tool_dir in {'Claude Code', 'Anthropic'}:
        return "Anthropic"
    elif tool_dir in {'Google', 'Gemini'}:
        return "Google"
    elif tool_dir in {'VSCode Agent', 'Cursor Prompts', 'Windsurf', 'Amp'}:
        return "IDE Extensions"
    elif tool_dir in {'v0 Prompts and Tools', 'Same.dev', 'Lovable', 'Replit', 'Leap.new'}:
        return "Web Platforms"
    else:
        return "Commercial Tools"


def scan_repository(repo_root: Path) -> dict:
    """Scan the repository and collect all tool/prompt information."""
    tools = defaultdict(lambda: {'files': [], 'category': ''})

    for item in sorted(repo_root.iterdir()):
        if not item.is_dir():
            continue
        if item.name in SKIP_DIRS:
            continue
        if item.name.startswith('.'):
            continue

        tool_name = item.name
        category = get_tool_category(tool_name)

        # Handle nested directories (like Open Source prompts)
        if tool_name == 'Open Source prompts':
            for subdir in sorted(item.iterdir()):
                if subdir.is_dir():
                    sub_tool_name = subdir.name
                    tools[sub_tool_name]['category'] = 'Open Source'
                    for file in sorted(subdir.iterdir()):
                        if file.is_file() and file.suffix in PROMPT_EXTENSIONS | TOOL_EXTENSIONS | CONFIG_EXTENSIONS:
                            tools[sub_tool_name]['files'].append(file)
        elif tool_name == 'Google':
            for subdir in sorted(item.iterdir()):
                if subdir.is_dir():
                    sub_tool_name = f"Google/{subdir.name}"
                    tools[sub_tool_name]['category'] = 'Google'
                    for file in sorted(subdir.iterdir()):
                        if file.is_file() and file.suffix in PROMPT_EXTENSIONS | TOOL_EXTENSIONS | CONFIG_EXTENSIONS:
                            tools[sub_tool_name]['files'].append(file)
        else:
            tools[tool_name]['category'] = category
            for file in sorted(item.iterdir()):
                if file.is_file() and file.suffix in PROMPT_EXTENSIONS | TOOL_EXTENSIONS | CONFIG_EXTENSIONS | DOC_EXTENSIONS:
                    # Skip READMEs in tool directories
                    if file.name.lower() == 'readme.md':
                        continue
                    tools[tool_name]['files'].append(file)

    return tools


def generate_catalog(repo_root: Path) -> str:
    """Generate the complete catalog markdown content."""
    tools = scan_repository(repo_root)

    # Calculate statistics
    total_files = sum(len(t['files']) for t in tools.values())
    total_tools = len(tools)
    total_size = sum(
        get_file_stats(f)['size_bytes']
        for t in tools.values()
        for f in t['files']
    )

    # Group by category
    by_category = defaultdict(list)
    for tool_name, tool_info in tools.items():
        if tool_info['files']:  # Only include tools with files
            by_category[tool_info['category']].append((tool_name, tool_info))

    # Sort categories
    category_order = [
        'Anthropic', 'Google', 'IDE Extensions',
        'Web Platforms', 'Commercial Tools', 'Open Source'
    ]

    # Build markdown
    lines = []
    lines.append("# AI System Prompts Catalog")
    lines.append("")
    lines.append(f"> Auto-generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    lines.append(">")
    lines.append("> Run `python scripts/generate_catalog.py` to regenerate this file.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Summary Statistics")
    lines.append("")
    lines.append(f"| Metric | Count |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total AI Tools | {total_tools} |")
    lines.append(f"| Total Files | {total_files} |")
    lines.append(f"| Total Size | {total_size / 1024:.1f} KB |")
    lines.append("")

    # Quick navigation
    lines.append("## Quick Navigation")
    lines.append("")
    for category in category_order:
        if category in by_category:
            tool_count = len(by_category[category])
            anchor = category.lower().replace(' ', '-')
            lines.append(f"- [{category}](#{anchor}) ({tool_count} tools)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Detailed listing by category
    for category in category_order:
        if category not in by_category:
            continue

        lines.append(f"## {category}")
        lines.append("")

        for tool_name, tool_info in sorted(by_category[category]):
            lines.append(f"### {tool_name}")
            lines.append("")

            if not tool_info['files']:
                lines.append("*No prompt or tool files found.*")
                lines.append("")
                continue

            lines.append("| File | Type | Size | Lines | Description |")
            lines.append("|------|------|------|-------|-------------|")

            for filepath in tool_info['files']:
                stats = get_file_stats(filepath)
                file_type = classify_file_type(filepath)
                description = extract_brief_description(filepath, 60)
                # Create relative path for link
                rel_path = filepath.relative_to(repo_root)
                # Escape special characters in path for markdown
                link_path = str(rel_path).replace(' ', '%20')

                lines.append(
                    f"| [{filepath.name}]({link_path}) | {file_type} | "
                    f"{stats['size']} | {stats['lines']} | {description} |"
                )

            lines.append("")

        lines.append("---")
        lines.append("")

    # Appendix: File type legend
    lines.append("## Legend")
    lines.append("")
    lines.append("| Icon | Type |")
    lines.append("|------|------|")
    lines.append("| 💬 | Prompt - Instructions for AI behavior |")
    lines.append("| 🤖 | System Prompt - Core system instructions |")
    lines.append("| 🔧 | Tool Definition - JSON schemas for tools |")
    lines.append("| ⚙️ | Configuration - YAML/settings files |")
    lines.append("| ⚡ | Action - Specific action prompts |")
    lines.append("| 📝 | Documentation - Markdown docs |")
    lines.append("| 📄 | File - Other file types |")
    lines.append("")

    return '\n'.join(lines)


def main():
    """Main entry point."""
    # Determine repo root (parent of scripts directory)
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent

    print(f"Scanning repository: {repo_root}")

    # Generate catalog
    catalog_content = generate_catalog(repo_root)

    # Write to CATALOG.md
    catalog_path = repo_root / 'CATALOG.md'
    with open(catalog_path, 'w', encoding='utf-8') as f:
        f.write(catalog_content)

    print(f"Catalog generated: {catalog_path}")
    print(f"Total size: {len(catalog_content)} bytes")


if __name__ == '__main__':
    main()
