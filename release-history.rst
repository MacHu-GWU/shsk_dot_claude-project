.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add the ``skill-base-invoker-design`` skill: one ``<prefix>-base`` skill holds the shared docs, scripts, and assets, and invoker skills load it and read the files they need. Invoke it as ``/dot-claude:skill-base-invoker-design <prefix and goal>`` to design a new family, add an invoker, refactor existing skills into a family, or review one.

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.4.1 (2026-09-26)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add the ``skill-base-invoker-design`` skill to the ``dot-claude`` plugin. It helps you build a family of skills that share one ``<prefix>-base<suffix>`` skill, which holds the family's docs, scripts, assets, and workflow, while each invoker skill loads the base, reads the base files it needs, and does one job. This keeps every shared spec in a single place, so skills that work together cannot drift apart. Invoke it as ``/dot-claude:skill-base-invoker-design <prefix and goal>`` to design a new family, add an invoker to an existing one, refactor standalone skills into a family, or review a family. Before writing anything it confirms the names and the base/invoker split with you, and when a request does not fit the pattern it suggests ordinary skills instead.
- The skill ships a ``base-invoker-agent-skill-family-pattern`` reference. It keeps the required rules to a short list (a shared prefix and suffix, a base always named ``<prefix>-base<suffix>``, a base that owns shared material but no single action, and invokers that each do one thing) and treats the rest as recommendations. It explains what belongs in the base versus an invoker: an invoker's own interaction style stays local, while the family workflow of which invoker runs before or after which goes in the base. It also gives lightweight base and invoker ``SKILL.md`` shapes.

**Miscellaneous**

- List ``skill-base-invoker-design`` in the README.


0.3.2 (2026-08-07)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- ``author-agent-skill`` and ``author-subagent`` now take the target as an argument, so you can point them straight at what you want to work on: ``/dot-claude:author-agent-skill .claude/skills/my-skill/``. Invoked with no argument, they ask which skill directory or subagent file to create or revise instead of guessing.
- Both skills now default to writing into the current project's ``.claude/`` directory, and will not write to the user-level ``~/.claude/`` unless you ask for it explicitly.

**Minor Improvements**

- Trim the two vendored Claude Code reference docs down to the authoring spec, roughly halving both. Dropped material covers product introductions, built-in skill and subagent catalogs, the ``/agents`` UI walkthrough, settings-level admin configuration, runtime-usage topics, and most of the long worked examples. Each file now opens with a provenance header recording its source URL, snapshot date, what was removed, and how to refresh it.
- Condense the ``description`` of all three authoring skills to a single line, and restructure the ``skill-subagent-design`` body into short paragraphs.


0.3.1 (2026-08-07)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Breaking Changes**

- Rename the two authoring skills in the ``dot-claude`` plugin so they share a single verb: ``write-agent-skill`` becomes ``author-agent-skill``, and ``create-sub-agent`` becomes ``author-subagent`` (also adopting the official one-word ``subagent`` spelling). Invoke them as ``/dot-claude:author-agent-skill`` and ``/dot-claude:author-subagent``; the old names no longer resolve.

**Minor Improvements**

- Rewrite the ``description`` of ``author-agent-skill`` and ``author-subagent`` to state what each skill does and when to use it, so Claude can discover them automatically instead of requiring an explicit slash command. Both descriptions now also cover revising an existing skill or subagent, not just creating a new one.


0.2.2 (2026-08-06)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add the ``python-cli-script-standard`` reference to the ``write-agent-skill`` skill in the ``dot-claude`` plugin, specifying the two-layer ``_main``/``main`` structure, ``--arg_name`` keyword style, and exit code conventions that stdlib-only Python CLI scripts must follow. ``SKILL.md`` now points to this reference so skills with such scripts are held to the standard.


0.2.1 (2026-08-01)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add the ``init-claude-messages`` skill to the ``dot-claude`` plugin. It generates a blank, numbered ``claude-code-messages.md`` template at ``.claude/claude-code-messages.md`` for a project, and warns instead of silently overwriting when the file already exists.


0.1.1 (2026-07-22)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First release.
- Add the ``dot-claude`` Claude Code plugin with four meta-skills for authoring and maintaining a project's ``.claude/`` setup: ``create-sub-agent``, ``write-agent-skill``, ``skill-subagent-design``.
