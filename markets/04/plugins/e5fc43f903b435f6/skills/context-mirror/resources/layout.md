# Context Mirror Layout

Cloud mirror root:

```text
stash://<owner>/.camber/agent-context/<agent-alias>/
├── README.md
├── instruction.md
├── chat/
├── knowledge-base/
├── project/
├── requirements/
├── schema/
└── skills/
```

Folder purpose:
- `README.md`: mission statement, inspected sources, exclusions, key commands, and sync status.
- `instruction.md`: the agent's runtime instructions, stored at the root of the agent context.
- `chat/`: current and approved extra chat exports, synced via chat export paths in `.camber/sync.yaml` and `$ camber agent push`.
- `knowledge-base/`: durable docs, files, and links approved as normal agent knowledge.
- `project/`: approved workspace files copied with relative project paths. Mirror-only, not KB.
- `requirements/`: dependency and runtime files such as manifests, lockfiles, Dockerfiles, compose files, Makefiles, and environment templates.
- `schema/`: markdown notes for datasets, database schemas, API schemas, column mappings, and relationships.
- `skills/`: migrated skill folders using `<skill-name>/SKILL.md`. Skill folders are never normal KB.

When Camber Web copies mirrored project files into a conversation project, the project folder appears as:

```text
<owner>_<agent-alias>_project-directory/
```

Keep the Stash mirror path and the Web project copy path distinct in agent instructions.
