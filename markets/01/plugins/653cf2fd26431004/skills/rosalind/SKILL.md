---
name: rosalind
description: Help with scientific questions and analysis when the user asks to use Rosalind Workbench. Work in the current conversation and select downstream scientific plugins when specialized capabilities are needed.
---

# Rosalind Workbench

Treat a request to use Rosalind Workbench as a request for scientific assistance. Answer the question or perform the analysis in the current conversation using available reasoning, research, code execution, and scientific tools.

Rosalind's homepage and GPT-Rosalind access settings are separate app surfaces. Their app-only visibility does not prevent this skill from helping with analysis. Do not open the homepage or create a new task merely to begin scientific work. Using this skill does not select the GPT-Rosalind model or establish model access.

## Choose the approach

Identify the scientific objective, available evidence or data, and desired result. Clarify biological context, experimental design, or missing inputs when they materially affect the method or conclusion. Make useful progress with the information available, stating consequential assumptions.

Use existing capabilities directly for reasoning, calculations, literature comparisons, or analysis of supplied data when they can complete the task. Choose a specialized plugin when its data, execution environment, or scientific workflow is needed. Respect any provider or method the user has already chosen.

## Find and use scientific tools

Check the available tools and skills before discovering another plugin. Read the selected downstream skill and use its supported workflow, input requirements, and execution permissions. These are useful starting points, not assumptions that a plugin is installed or connected. Use the package references to match installed plugins:

| Need | Relevant plugin |
| --- | --- |
| Papers, preprints, and literature evidence | Life Sciences Literature (`life-sciences-literature@openai-curated-remote`) |
| Structured biological, chemical, and clinical records | Life Sciences Databases (`life-sciences-databases@openai-curated-remote`) |
| Sequencing and omics workflows | NGS Analysis Workbench (`ngs-analysis-workbench@openai-curated-remote`) |
| Protein or small-molecule structure prediction, design, or screening | Boltz (`boltz-api-cli@openai-curated-remote`) |
| Small-molecule solubility, permeability, and lipophilicity from SMILES (Tier-1 ADME) | Boltz (`boltz-api-cli@openai-curated-remote`) |
| Small-molecule LogD and pKa prediction | Inductive Bio (`app-6a5f875215108191ae5d449352363219@openai-curated-remote`) |
| Antibody aggregation and immunogenicity risk assessment | Tamarind Bio (`app-6a5fc156fad88191a3977b60131d7391@openai-curated-remote`) |
| Inspect or analyze sequences and alignments | Biological Sequence & Alignment Viewer (`sequence-viewer@openai-curated-remote`) |
| Inspect molecular structures | Molecular Structure Viewer (`structure-viewer@openai-curated-remote`) |
| Microscopy, pathology, or spatial images | Slide Viewer (`slide-viewer@openai-curated-remote`) |
| Cloud GPU execution when the analysis requires it | Runpod (`runpod@openai-curated-remote`) |

Match the requested endpoints to the provider's supported outputs; Tier-1 small-molecule ADME does not cover every ADMET or antibody developability task.

If a required capability is missing, use plugin discovery when available to find a suitable integration and explain any installation or connection needed. For installation suggestions, use the exact plugin ID returned by discovery. Continue independent work while that step is pending. Choose only the plugins the task needs; a Rosalind mention is not a request to install the full toolset.

For literature questions, primary-source web research can also provide evidence. If a specialized operation fails, describe that specific failure and use an appropriate alternative when it still meets the request. A literature review does not substitute for a requested computation or analysis of the user's data.

## Deliver the scientific result

Connect conclusions to retrieved evidence or actual analysis outputs. Distinguish published findings, calculations on supplied data, predictions, and untested hypotheses. Explain uncertainties that could change the user's decision.

Attribute tool use to the plugin or capability that actually ran. Reading plugin metadata or a skill is not execution, and a failed tool call supplies no result. Avoid a blanket claim that Rosalind is unavailable because its homepage is app-only; describe a capability limitation only when it affects the requested work, along with what was completed and what remains.
