# Macroscope for Codex

Run Macroscope code review against your local branch before you push.

## Included skills

- `macroscope:codereview`: run one review, validate findings, and safely prepare confirmed fixes.
- `macroscope:autoloop`: repeat review, repair, verification, and commits until clean, up to five passes.

## Requirement

Install and configure the Macroscope CLI before using either skill:

```bash
curl -sSL https://raw.githubusercontent.com/prassoai/macroscope-local/main/install.sh | bash
```

Restart Codex after installation, then ask: “Review my current changes with Macroscope.”
