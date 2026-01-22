# AI System Prompts Catalog

> Comprehensive index of all AI system prompts and tool definitions in this repository.
>
> Run `./scripts/generate_catalog.sh` (requires bash with standard tools) or `python scripts/generate_catalog.py` (requires Python 3.6+) to regenerate this catalog.

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total AI Tools | 33 |
| Total Files | 95 |
| Categories | 6 |

---

## Quick Navigation

- [Anthropic](#anthropic) - Claude and Anthropic tools
- [Google](#google) - Google AI tools
- [IDE Extensions](#ide-extensions) - Code editor integrations
- [Web Platforms](#web-platforms) - Web-based AI development tools
- [Commercial Tools](#commercial-tools) - Commercial AI products
- [Open Source](#open-source) - Open source AI tools

---

## Anthropic

### Anthropic

| File | Type | Description |
|------|------|-------------|
| [Claude Code 2.0.txt](Anthropic/Claude%20Code%202.0.txt) | System Prompt | Claude Code version 2.0 system instructions |
| [Sonnet 4.5 Prompt.txt](Anthropic/Sonnet%204.5%20Prompt.txt) | System Prompt | Sonnet 4.5 model instructions |

### Claude Code

| File | Type | Description |
|------|------|-------------|
| [claude-code-system-prompt.txt](Claude%20Code/claude-code-system-prompt.txt) | System Prompt | Core system prompt for Claude Code CLI tool |
| [claude-code-tools.json](Claude%20Code/claude-code-tools.json) | Tool Definition | JSON schema definitions for Claude Code tools |

---

## Google

### Gemini

| File | Type | Description |
|------|------|-------------|
| [AI Studio Vibe-Coder.txt](Gemini/AI%20Studio%20Vibe-Coder.txt) | System Prompt | AI Studio Vibe-Coder configuration |

### Google/Antigravity

| File | Type | Description |
|------|------|-------------|
| [Fast Prompt.txt](Google/Antigravity/Fast%20Prompt.txt) | System Prompt | Google Antigravity fast mode prompt |
| [planning-mode.txt](Google/Antigravity/planning-mode.txt) | System Prompt | Google Antigravity planning mode |

---

## IDE Extensions

### Amp

| File | Type | Description |
|------|------|-------------|
| [claude-4-sonnet.yaml](Amp/claude-4-sonnet.yaml) | Configuration | Amp config for Claude 4 Sonnet |
| [gpt-5.yaml](Amp/gpt-5.yaml) | Configuration | Amp config for GPT-5 |

### Augment Code

| File | Type | Description |
|------|------|-------------|
| [claude-4-sonnet-agent-prompts.txt](Augment%20Code/claude-4-sonnet-agent-prompts.txt) | System Prompt | Augment Code prompts for Claude 4 Sonnet |
| [claude-4-sonnet-tools.json](Augment%20Code/claude-4-sonnet-tools.json) | Tool Definition | Tool definitions for Claude 4 Sonnet |
| [gpt-5-agent-prompts.txt](Augment%20Code/gpt-5-agent-prompts.txt) | System Prompt | Augment Code prompts for GPT-5 |
| [gpt-5-tools.json](Augment%20Code/gpt-5-tools.json) | Tool Definition | Tool definitions for GPT-5 |

### Cursor Prompts

| File | Type | Description |
|------|------|-------------|
| [Agent CLI Prompt 2025-08-07.txt](Cursor%20Prompts/Agent%20CLI%20Prompt%202025-08-07.txt) | System Prompt | CLI agent prompt (Aug 2025) |
| [Agent Prompt 2.0.txt](Cursor%20Prompts/Agent%20Prompt%202.0.txt) | System Prompt | Version 2.0 agent prompt |
| [Agent Prompt 2025-09-03.txt](Cursor%20Prompts/Agent%20Prompt%202025-09-03.txt) | System Prompt | Agent prompt (Sep 2025) |
| [Agent Prompt v1.0.txt](Cursor%20Prompts/Agent%20Prompt%20v1.0.txt) | System Prompt | Version 1.0 agent prompt |
| [Agent Prompt v1.2.txt](Cursor%20Prompts/Agent%20Prompt%20v1.2.txt) | System Prompt | Version 1.2 agent prompt |
| [Agent Tools v1.0.json](Cursor%20Prompts/Agent%20Tools%20v1.0.json) | Tool Definition | Agent tool definitions v1.0 |
| [Chat Prompt.txt](Cursor%20Prompts/Chat%20Prompt.txt) | System Prompt | Chat mode prompt |

### Junie

| File | Type | Description |
|------|------|-------------|
| [Prompt.txt](Junie/Prompt.txt) | System Prompt | JetBrains Junie AI assistant |

### Kiro

| File | Type | Description |
|------|------|-------------|
| [Mode_Clasifier_Prompt.txt](Kiro/Mode_Clasifier_Prompt.txt) | System Prompt | Mode classification prompt |
| [Spec_Prompt.txt](Kiro/Spec_Prompt.txt) | System Prompt | Spec mode prompt |
| [Vibe_Prompt.txt](Kiro/Vibe_Prompt.txt) | System Prompt | Vibe mode prompt |

### Trae

| File | Type | Description |
|------|------|-------------|
| [Builder Prompt.txt](Trae/Builder%20Prompt.txt) | System Prompt | Builder mode prompt |
| [Builder Tools.json](Trae/Builder%20Tools.json) | Tool Definition | Builder tool definitions |
| [Chat Prompt.txt](Trae/Chat%20Prompt.txt) | System Prompt | Chat mode prompt |

### VSCode Agent

| File | Type | Description |
|------|------|-------------|
| [Prompt.txt](VSCode%20Agent/Prompt.txt) | System Prompt | Main VSCode agent prompt |
| [chat-titles.txt](VSCode%20Agent/chat-titles.txt) | System Prompt | Chat title generation |
| [claude-sonnet-4.txt](VSCode%20Agent/claude-sonnet-4.txt) | System Prompt | Claude Sonnet 4 specific prompt |
| [gemini-2.5-pro.txt](VSCode%20Agent/gemini-2.5-pro.txt) | System Prompt | Gemini 2.5 Pro specific prompt |
| [gpt-4.1.txt](VSCode%20Agent/gpt-4.1.txt) | System Prompt | GPT-4.1 specific prompt |
| [gpt-4o.txt](VSCode%20Agent/gpt-4o.txt) | System Prompt | GPT-4o specific prompt |
| [gpt-5-mini.txt](VSCode%20Agent/gpt-5-mini.txt) | System Prompt | GPT-5 Mini specific prompt |
| [gpt-5.txt](VSCode%20Agent/gpt-5.txt) | System Prompt | GPT-5 specific prompt |
| [nes-tab-completion.txt](VSCode%20Agent/nes-tab-completion.txt) | System Prompt | Tab completion prompt |

### Windsurf

| File | Type | Description |
|------|------|-------------|
| [Prompt Wave 11.txt](Windsurf/Prompt%20Wave%2011.txt) | System Prompt | Wave 11 system prompt |
| [Tools Wave 11.txt](Windsurf/Tools%20Wave%2011.txt) | Tool Definition | Wave 11 tool definitions |

### Xcode

| File | Type | Description |
|------|------|-------------|
| [DocumentAction.txt](Xcode/DocumentAction.txt) | Action | Document action prompt |
| [ExplainAction.txt](Xcode/ExplainAction.txt) | Action | Explain action prompt |
| [MessageAction.txt](Xcode/MessageAction.txt) | Action | Message action prompt |
| [PlaygroundAction.txt](Xcode/PlaygroundAction.txt) | Action | Playground action prompt |
| [PreviewAction.txt](Xcode/PreviewAction.txt) | Action | Preview action prompt |
| [System.txt](Xcode/System.txt) | System Prompt | Main Xcode system prompt |

---

## Web Platforms

### Leap.new

| File | Type | Description |
|------|------|-------------|
| [Prompts.txt](Leap.new/Prompts.txt) | System Prompt | Leap.new prompts |
| [tools.json](Leap.new/tools.json) | Tool Definition | Leap.new tool definitions |

### Lovable

| File | Type | Description |
|------|------|-------------|
| [Agent Prompt.txt](Lovable/Agent%20Prompt.txt) | System Prompt | Lovable agent prompt |
| [Agent Tools.json](Lovable/Agent%20Tools.json) | Tool Definition | Lovable tool definitions |

### Replit

| File | Type | Description |
|------|------|-------------|
| [Prompt.txt](Replit/Prompt.txt) | System Prompt | Replit AI assistant prompt |
| [Tools.json](Replit/Tools.json) | Tool Definition | Replit tool definitions |

### Same.dev

| File | Type | Description |
|------|------|-------------|
| [Prompt.txt](Same.dev/Prompt.txt) | System Prompt | Same.dev prompt |
| [Tools.json](Same.dev/Tools.json) | Tool Definition | Same.dev tool definitions |

### v0 Prompts and Tools

| File | Type | Description |
|------|------|-------------|
| [Prompt.txt](v0%20Prompts%20and%20Tools/Prompt.txt) | System Prompt | Vercel v0 prompt |
| [Tools.json](v0%20Prompts%20and%20Tools/Tools.json) | Tool Definition | Vercel v0 tool definitions |

---

## Commercial Tools

### Cluely

| File | Type | Description |
|------|------|-------------|
| [Default Prompt.txt](Cluely/Default%20Prompt.txt) | System Prompt | Default prompt |
| [Enterprise Prompt.txt](Cluely/Enterprise%20Prompt.txt) | System Prompt | Enterprise prompt |

### CodeBuddy Prompts

| File | Type | Description |
|------|------|-------------|
| [Chat Prompt.txt](CodeBuddy%20Prompts/Chat%20Prompt.txt) | System Prompt | Chat mode prompt |
| [Craft Prompt.txt](CodeBuddy%20Prompts/Craft%20Prompt.txt) | System Prompt | Craft mode prompt |

### Comet Assistant

| File | Type | Description |
|------|------|-------------|
| [System Prompt.txt](Comet%20Assistant/System%20Prompt.txt) | System Prompt | Comet assistant prompt |

### Devin AI

| File | Type | Description |
|------|------|-------------|
| [DeepWiki Prompt.txt](Devin%20AI/DeepWiki%20Prompt.txt) | System Prompt | DeepWiki mode prompt |
| [Prompt.txt](Devin%20AI/Prompt.txt) | System Prompt | Main Devin prompt |

### dia

| File | Type | Description |
|------|------|-------------|
| [Prompt.txt](dia/Prompt.txt) | System Prompt | dia AI prompt |

### Emergent

| File | Type | Description |
|------|------|-------------|
| [Prompt.txt](Emergent/Prompt.txt) | System Prompt | Emergent prompt |
| [Tools.json](Emergent/Tools.json) | Tool Definition | Emergent tool definitions |

### Manus Agent Tools & Prompt

| File | Type | Description |
|------|------|-------------|
| [Agent loop.txt](Manus%20Agent%20Tools%20%26%20Prompt/Agent%20loop.txt) | System Prompt | Agent loop instructions |
| [Modules.txt](Manus%20Agent%20Tools%20%26%20Prompt/Modules.txt) | System Prompt | Module descriptions |
| [Prompt.txt](Manus%20Agent%20Tools%20%26%20Prompt/Prompt.txt) | System Prompt | Main Manus prompt |
| [tools.json](Manus%20Agent%20Tools%20%26%20Prompt/tools.json) | Tool Definition | Manus tool definitions |

### NotionAi

| File | Type | Description |
|------|------|-------------|
| [Prompt.txt](NotionAi/Prompt.txt) | System Prompt | Notion AI prompt |
| [tools.json](NotionAi/tools.json) | Tool Definition | Notion AI tool definitions |

### Orchids.app

| File | Type | Description |
|------|------|-------------|
| [Decision-making prompt.txt](Orchids.app/Decision-making%20prompt.txt) | System Prompt | Decision-making prompt |
| [System Prompt.txt](Orchids.app/System%20Prompt.txt) | System Prompt | Main system prompt |

### Perplexity

| File | Type | Description |
|------|------|-------------|
| [Prompt.txt](Perplexity/Prompt.txt) | System Prompt | Perplexity AI prompt |

### Poke

| File | Type | Description |
|------|------|-------------|
| [Poke agent.txt](Poke/Poke%20agent.txt) | System Prompt | Main agent prompt |
| [Poke_p1.txt](Poke/Poke_p1.txt) | System Prompt | Phase 1 prompt |
| [Poke_p2.txt](Poke/Poke_p2.txt) | System Prompt | Phase 2 prompt |
| [Poke_p3.txt](Poke/Poke_p3.txt) | System Prompt | Phase 3 prompt |
| [Poke_p4.txt](Poke/Poke_p4.txt) | System Prompt | Phase 4 prompt |
| [Poke_p5.txt](Poke/Poke_p5.txt) | System Prompt | Phase 5 prompt |
| [Poke_p6.txt](Poke/Poke_p6.txt) | System Prompt | Phase 6 prompt |

### Qoder

| File | Type | Description |
|------|------|-------------|
| [Quest Action.txt](Qoder/Quest%20Action.txt) | Action | Quest action prompt |
| [Quest Design.txt](Qoder/Quest%20Design.txt) | System Prompt | Quest design prompt |
| [prompt.txt](Qoder/prompt.txt) | System Prompt | Main Qoder prompt |

### Traycer AI

| File | Type | Description |
|------|------|-------------|
| [phase_mode_prompts.txt](Traycer%20AI/phase_mode_prompts.txt) | System Prompt | Phase mode prompts |
| [phase_mode_tools.json](Traycer%20AI/phase_mode_tools.json) | Tool Definition | Phase mode tools |
| [plan_mode_tools.json](Traycer%20AI/plan_mode_tools.json) | Tool Definition | Plan mode tools |

### Warp.dev

| File | Type | Description |
|------|------|-------------|
| [Prompt.txt](Warp.dev/Prompt.txt) | System Prompt | Warp terminal AI prompt |

### Z.ai Code

| File | Type | Description |
|------|------|-------------|
| [prompt.txt](Z.ai%20Code/prompt.txt) | System Prompt | Z.ai Code prompt |

---

## Open Source

### Bolt

| File | Type | Description |
|------|------|-------------|
| [Prompt.txt](Open%20Source%20prompts/Bolt/Prompt.txt) | System Prompt | Bolt AI prompt |

### Cline

| File | Type | Description |
|------|------|-------------|
| [Prompt.txt](Open%20Source%20prompts/Cline/Prompt.txt) | System Prompt | Cline AI assistant prompt |

### Codex CLI

| File | Type | Description |
|------|------|-------------|
| [Prompt.txt](Open%20Source%20prompts/Codex%20CLI/Prompt.txt) | System Prompt | Codex CLI prompt |
| [openai-codex-cli-system-prompt-20250820.txt](Open%20Source%20prompts/Codex%20CLI/openai-codex-cli-system-prompt-20250820.txt) | System Prompt | Official OpenAI Codex CLI prompt (Aug 2025) |

### Gemini CLI

| File | Type | Description |
|------|------|-------------|
| [google-gemini-cli-system-prompt.txt](Open%20Source%20prompts/Gemini%20CLI/google-gemini-cli-system-prompt.txt) | System Prompt | Official Google Gemini CLI prompt |

### Lumo

| File | Type | Description |
|------|------|-------------|
| [Prompt.txt](Open%20Source%20prompts/Lumo/Prompt.txt) | System Prompt | Lumo AI prompt |

### RooCode

| File | Type | Description |
|------|------|-------------|
| [Prompt.txt](Open%20Source%20prompts/RooCode/Prompt.txt) | System Prompt | RooCode AI prompt |

---

## Legend

| Icon | Description |
|------|-------------|
| System Prompt | Core instructions that define AI behavior |
| Tool Definition | JSON schemas defining available tools/functions |
| Configuration | YAML/settings files for model configuration |
| Action | Specific action-triggered prompts |

---

## Contributing

To add new prompts or tools:

1. Create a directory with the tool name
2. Add prompt files as `.txt` and tool definitions as `.json`
3. Run the catalog generator to update this index
4. Submit a pull request

---

*This catalog provides an overview of the repository contents. For detailed information, refer to individual files.*
