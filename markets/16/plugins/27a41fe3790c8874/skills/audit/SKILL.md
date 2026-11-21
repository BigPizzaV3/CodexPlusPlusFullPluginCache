---
name: audit
description: Deep EVM smart contract security audit. Use when asked to audit a contract, find vulnerabilities, or review Solidity someone else wrote. Covers 500+ checklist items across 19 domains. Different from the security skill, which teaches defensive coding.
---

# EVM Smart Contract Audit

Walks domain-specific checklists against a contract and reports findings. All checklists are bundled in `references/`. Do not fetch them from the web.

## Input

The contract source (pasted, uploaded, or a verified-source link the user provides). If you don't have the source, ask for it. Never audit from a contract address alone without the code.

## Steps

1. Read `references/master.md`. It has the routing table, methodology, and finding format.
2. Read the contract(s).
3. Pick 5–8 checklists from the routing table. Always include `evm-audit-general` and `evm-audit-precision-math`.
4. Walk each checklist in `references/<skill-name>.md` against the code.
5. Report findings using the format in `master.md`, sorted by severity.

## Checklists

| File | When |
|---|---|
| `references/evm-audit-general.md` | Always |
| `references/evm-audit-precision-math.md` | Always |
| `references/evm-audit-erc20.md` | Takes ERC20 tokens |
| `references/evm-audit-defi-amm.md` | AMM, DEX, Uniswap V3/V4, liquidity pools |
| `references/evm-audit-defi-lending.md` | Lending, borrowing, liquidations |
| `references/evm-audit-defi-staking.md` | Staking, liquid staking, restaking |
| `references/evm-audit-erc4626.md` | Vaults |
| `references/evm-audit-erc4337.md` | Account abstraction, paymasters |
| `references/evm-audit-bridges.md` | Cross-chain |
| `references/evm-audit-proxies.md` | Upgradeable contracts |
| `references/evm-audit-signatures.md` | EIP-712, permits, off-chain signatures |
| `references/evm-audit-governance.md` | DAOs, voting, timelocks |
| `references/evm-audit-oracles.md` | Price feeds |
| `references/evm-audit-assembly.md` | Inline assembly, Yul, CREATE2 |
| `references/evm-audit-chain-specific.md` | Non-mainnet chains |
| `references/evm-audit-flashloans.md` | Flash loans |
| `references/evm-audit-erc721.md` | NFTs |
| `references/evm-audit-dos.md` | Loops, gas griefing |
| `references/evm-audit-access-control.md` | Ownership, roles, admin powers |

## Rules

- Only report issues you can point to in the code. Quote the line.
- Say clearly that this is an automated review, not a professional audit. For contracts holding real value, recommend a human audit too.
- Don't file issues, open PRs, or post anywhere unless the user asks.

## Sources

Checklists from [evm-audit-skills](https://github.com/austintgriffith/evm-audit-skills), built from research by Dacian, beirao.xyz, Sigma Prime, RareSkills, Decurity, weird-erc20, Spearbit, Hacken, OpenZeppelin, Cyfrin, and more.
