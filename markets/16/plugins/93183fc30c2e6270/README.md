# Qdrant Advisor

A skill-based plugin for diagnosing and advising on Qdrant deployments using current guidance from https://skills.qdrant.tech.

## Usage

Ask about slow queries, memory growth, indexing, scaling, search relevance, deployment options, SDKs, monitoring, or migrations. Include your Qdrant version, deployment type, symptoms, and recent changes when available.

The advisor searches the live registry, follows relevant linked skills and documentation, and cites the guidance used. The host agent needs web-fetch access. This package does not supply a browsing tool, an MCP server, or a connection to your Qdrant cluster.

## Contents and provenance

- `.codex-plugin/plugin.json`: plugin metadata and starter prompts.
- `skills/qdrant-advisor/SKILL.md`: unchanged Qdrant Advisor skill from `qdrant/skills`, `meta/qdrant-advisor`.
- `LICENSE`: original Apache 2.0 license, including Qdrant Solutions GmbH attribution.

Version: 0.1.1. The ZIP contains the plugin contents at its root, including the hidden `.codex-plugin` directory.

Icon source: https://qdrant.tech/images/android-chrome-512x512.png
