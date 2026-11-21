# Adaption Plugin for ChatGPT & Codex

Connect ChatGPT and Codex to [Adaption](https://adaptionlabs.ai) for dataset management, fine-tuning, and AutoScientist workflows.

The plugin bundles three skills and the remote Adaption MCP server
(`https://api.prod.adaptionlabs.ai/api/v1/mcp`). You sign in with your Adaption
account in the browser; no API key is needed.

## Installation

### Codex CLI

```bash
codex plugin marketplace add adaptionlabs/adaption-codex-plugin
codex plugin add adaption@adaption
codex mcp login adaption
```

`codex mcp login` opens the Adaption sign-in page. Choose the organization and
click **Authorize**. Check the connection with:

```bash
codex mcp list
```

`adaption` should show as logged in.

### Codex in the ChatGPT desktop app

1. Add the marketplace with the CLI command above (the desktop app reads the
   same configuration), then restart the app
2. Open the **Plugins Directory**, choose the **Adaption** marketplace, and
   install **Adaption**
3. Sign in with your Adaption account when prompted

### ChatGPT

A listing in the public Plugins Directory is coming soon. Until then, add the
MCP server as a custom connector:

1. Turn on **Developer mode** in ChatGPT settings
2. Create a custom connector with the MCP server URL
   `https://api.prod.adaptionlabs.ai/api/v1/mcp` and **OAuth** authentication
3. Sign in with your Adaption account when ChatGPT redirects you

### Headless use with an API key

For CI or machines without a browser, skip `codex mcp login` and authenticate
with an Adaption API key instead. Create one at
[adaptionlabs.ai/app/settings](https://adaptionlabs.ai/app/settings?tab=api_keys)
and add the server to `~/.codex/config.toml`:

```toml
[mcp_servers.adaption]
url = "https://api.prod.adaptionlabs.ai/api/v1/mcp"
bearer_token_env_var = "ADAPTION_API_KEY"
```

Then export `ADAPTION_API_KEY` in the environment Codex runs in.

### Local development

```bash
git clone https://github.com/adaptionlabs/adaption-codex-plugin.git
cd adaption-codex-plugin
codex plugin marketplace add ./
codex plugin add adaption@adaption
```

Codex installs a copy into `~/.codex/plugins/cache/`. After changing the plugin,
run `codex plugin remove adaption@adaption` and add it again, then restart
Codex.

## Features

### 📊 Dataset Management (11 tools)

- **Import** datasets from HuggingFace, Kaggle, or Google Sheets
- **Adapt** datasets with Adaption's processing pipeline
- **Augment** datasets with synthetic domain/general rows
- **Translate** and **localize** dataset content
- **Combine** multiple datasets
- **Export** processed results

### 🎯 Fine-tuning (5 tools)

- Browse available **base models**
- Get **hyperparameter recommendations**
- Launch **AutoScientist training runs**
- Monitor **training progress** and results

### 🔬 Invent (2 tools)

- Explore available **domains and subdomains**
- **Generate synthetic datasets** from natural language descriptions

## Available Skills

| Skill | Description |
|-------|-------------|
| `adaption-dataset` | Dataset import, processing, and transformation workflows |
| `adaption-training` | AutoScientist training run management |
| `adaption-invent` | Synthetic data generation with Invent |

## MCP Tools Reference

### Dataset Tools

| Tool | Description |
|------|-------------|
| `list_datasets` | List datasets visible to your organization |
| `get_dataset` | Get details of one dataset |
| `get_dataset_status` | Poll processing status and progress |
| `get_dataset_evaluation` | Get quality evaluation results |
| `get_dataset_export_links` | Get export download URLs |
| `import_dataset` | Import from HuggingFace, Kaggle, or Google Sheets |
| `run_dataset_adaptation` | Estimate or launch adaptation |
| `augment_dataset` | Add synthetic domain/general rows |
| `translate_dataset` | Translate rows to target languages |
| `localize_dataset` | Localize for country/language pairs |
| `combine_datasets` | Combine compatible datasets |

### Training Tools

| Tool | Description |
|------|-------------|
| `list_training_models` | List available base models |
| `list_autoscientist_runs` | List training runs |
| `get_autoscientist_run` | Get run details and progress |
| `recommend_autoscientist_hyperparameters` | Get recommended config |
| `create_autoscientist_run` | Launch training (spends credits) |

### Invent Tools

| Tool | Description |
|------|-------------|
| `list_invent_domains` | List valid domain/subdomain codes |
| `generate_dataset` | Estimate or launch dataset generation |

## Example Usage

Once installed, interact with Adaption through natural conversation:

> "List my Adaption datasets"

> "Import this HuggingFace dataset and adapt it for fine-tuning"

> "Start fine-tuning on my adapted dataset and pick a suitable base model"

> "Generate 1000 customer service examples using Invent"

> "Check the status of my training job"

## Requirements

- Codex CLI, the ChatGPT desktop app, or ChatGPT with Developer mode
- An Adaption account

## Support

- **Documentation**: [docs.adaptionlabs.ai](https://docs.adaptionlabs.ai)
- **Issues**: [GitHub Issues](https://github.com/adaptionlabs/adaption-codex-plugin/issues)
- **Email**: support@adaptionlabs.ai

## License

MIT License - see [LICENSE](LICENSE) for details.
