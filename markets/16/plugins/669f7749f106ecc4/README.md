# Mojulo Work-native plugin

Mojulo's Work-native plugin is a skills-only distribution path for running Mojulo inside the agent's writable execution environment. It contains no MCP configuration and does not require hosted Mojulo compute.

## Runtime behavior

The skill bootstraps exact `mojulo@3.0.0` into a workspace-local runtime, binds state to the active workspace, and hands generated files back through the host environment. Node >=22.14 and npm are required.

Portable Mojulo recipes/checkpoints are the recovery boundary across fresh execution environments.
