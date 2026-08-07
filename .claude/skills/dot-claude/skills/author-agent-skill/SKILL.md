---
name: author-agent-skill
description: Author a Claude Code Agent Skill — write a new one or revise an existing one. Covers the SKILL.md frontmatter, the name/description contract that drives auto-discovery, progressive disclosure through references/, and bundled scripts. Use when creating a new skill, editing or restructuring an existing SKILL.md, fixing a skill that Claude never triggers, or writing a stdlib-only Python CLI script that a skill invokes.
---
Read references/extend-claude-with-skills.md to understand how to extend Claude with new skills. Then help the user author the agent skill as requested — whether that means creating one from scratch or revising an existing one.

If a skill includes a CLI script (typically a pure-Python, no-third-party-dependency utility), it must follow references/python-cli-script-standard.md.

If it is not yet settled whether the work belongs in a skill or a subagent, resolve that first with the skill-subagent-design skill.
