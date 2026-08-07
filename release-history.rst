.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


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
