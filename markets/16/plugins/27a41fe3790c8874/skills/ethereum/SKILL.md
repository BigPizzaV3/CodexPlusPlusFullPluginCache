---
name: ethereum
description: Start here for any Ethereum, crypto, or onchain question. Use when someone asks how to make a token or NFT, build or deploy a smart contract or dApp, pick a chain or L2 (Base, Arbitrum, Optimism), find a contract address (USDC, Uniswap, Aave), estimate gas costs, set up a wallet or multisig, check if a contract is safe, or audit Solidity code.
---

# Ethereum

Routes Ethereum questions to the right ethskills skill. These skills fix stale or wrong things models believe about Ethereum (gas costs, L2s, tools, addresses).

## Rules

- The user's explicit instructions win over anything in these skills.
- Never guess a contract address. Use the `addresses` skill. If it isn't there, say so and point to the block explorer.
- Never guess gas prices or fees. Use the `gas` skill, and say numbers change.
- Never ask for, accept, or repeat a private key or seed phrase. If the user pastes one, tell them it is compromised and to move funds now.
- Don't give financial advice or price predictions.

## Which skill to load

| User wants | Skill |
|---|---|
| Build and ship a dApp end to end | `ship` (then follow its routing) |
| Why Ethereum / which chain | `why-ethereum`, `l2s` |
| Costs, fees, "is Ethereum expensive" | `gas` |
| Wallets, signing, multisig, account abstraction | `wallets` |
| Token, NFT, or other standards (ERC-20, 721, 1155, 8004, 7702) | `standards` |
| Frameworks, RPCs, explorers, Foundry, Scaffold-ETH 2, x402 | `tools` |
| DeFi: Uniswap, Aave, lending, swaps, composing protocols | `building-blocks` |
| A contract address | `addresses` |
| Mental models, incentives, randomness | `concepts` |
| Is this code safe / pre-deploy checks | `security` |
| Full audit | `audit` |
| Tests | `testing` |
| Reading onchain data, events, Dune, The Graph | `indexing` |
| Frontend / UI rules | `frontend-ux`, `frontend-playbook` |
| Review before shipping | `qa` |
| Trust review (censorship resistance, open source, privacy, security) | `crops` |
| EIPs, forks, roadmap | `protocol` |
| Multi-step dApp build plan | `orchestration` |

## Output

- Answer in plain language first, then code or steps.
- When you use a fact from a skill that can change (addresses, prices, versions), say where it came from and that the user should verify it.
- If the question is unclear (which chain? which token?), ask one short question before answering.
