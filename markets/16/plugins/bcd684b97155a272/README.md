# Valohai plugin

This plugin provides instructions for migrating Python ML projects to Valohai.
It does not yet include a Valohai API connection or CLI installation.

## Included skills

- `valohai-yaml-step` — define steps in `valohai.yaml`
- `valohai-migrate-parameters` — expose configurable parameters
- `valohai-migrate-metrics` — log metrics for Valohai experiments
- `valohai-migrate-data` — use Valohai inputs and outputs
- `valohai-project-run` — set up and run projects with the `vh` CLI
- `valohai-design-pipelines` — plan multi-step pipelines

The six skills can be used individually or together.
For a full migration, start with steps, then parameters, metrics, data, project execution, and pipeline design.
You will need your own Valohai account and `valohai-cli` for commands that create or run projects.
These skills are separately available in [valohai/valohai-skills](https://github.com/valohai/valohai-skills).

## Install from GitHub

```shell
codex plugin marketplace add valohai/valohai-agent-plugin
codex plugin add valohai@valohai
```

Start a new Codex task after installing so it can load the skills. 
The plugin will also be available through the public plugin directory after its listing is approved and published.
