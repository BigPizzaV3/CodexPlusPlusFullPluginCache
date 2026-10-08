# Unix Copilot Plugin

Version: 0.1.0

A skills-only, safety-first command-line copilot for Unix, Linux, macOS, Bash, zsh, shell scripts, text/file processing, and CLI data workflows.

## Architecture

```text
Unix Copilot
└── unix-copilot
    ├── shell safety & portability
    ├── file & text processing
    ├── CSV / CLI data patterns
    ├── shell script debugging
    └── install / environment guidance
```

No MCP server is required for v0.1.

The plugin generates commands and guidance only. It cannot execute commands, inspect the user's system, modify files, install packages, or verify results by itself.

## Package structure

```text
plugin.json
assets/
  icon.svg
  logo.svg
skills/
  unix-copilot/
    SKILL.md
    agents/
      openai.yaml
    assets/
      icon.svg
    references/
      shell_safety_portability.md
      file_text_processing_patterns.md
      csv_data_cli_patterns.md
      shell_script_debugging_patterns.md
      unix_install_environment_reference.md
      official_source_registry.md
submission/
  listing-and-prompts.md
  test-cases.md
  public-submission-checklist.md
  release-notes.md
docs/
  RESEARCH_NOTES.md
PLUGIN_CREATOR_PROMPT.md
README.md
```

## Recommended next step

Review the package and upload it to the OpenAI plugin workflow only when ready.

This package has deliberately **not** been created, installed, or submitted as a plugin.
