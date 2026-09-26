---
name: skill-base-invoker-design
description: "The base invoker agent skill family pattern: one <prefix>-base skill holds the shared docs, scripts, and assets, and invoker skills each load the base and do one job. Use to design, scaffold, extend, or review such a family."
argument-hint: "[prefix and what the family should do | path to an existing family]"
---
Target: $ARGUMENTS

Read references/base-invoker-agent-skill-family-pattern.md. It defines the pattern, the required rules, what goes in the base versus an invoker, and recommended SKILL.md shapes.

For the SKILL.md spec itself, read ../author-agent-skill/references/extend-claude-with-skills.md. If the base bundles a Python CLI script, it must follow ../author-agent-skill/references/python-cli-script-standard.md.

Then do whichever the target calls for:

- **New family**: confirm the prefix, the suffix (possibly empty), and the list of invokers before writing. Build the base first, then each invoker.
- **Add an invoker** to an existing family: read the base first and reuse what is there. Add to the base only what is new and shared.
- **Refactor** existing skills into a family: move shared material into the base, then cut each skill down to an invoker.
- **Review** a family: check it against the required rules and point out anything shared that lives in more than one place.

If no target is given, ask for the prefix and what the family should do.

Default location is `<project>/.claude/skills/`. Never write to `~/.claude/` unless the user asks for it explicitly.
