---
name: squidlor-transfer
description: >-
  Use when the user wants to send, transfer or pay a token to an address ("send
  50 USDC to 0x...", "pay 0.1 ETH to", "transfer"), or asks what a wallet holds.
  Uses the Squidlor MCP tools get_wallet_overview and quote_send. quote_send
  returns an UNSIGNED transaction for the user to sign with their own wallet;
  nothing here can sign or move funds.
---

# Squidlor transfers

`quote_send` builds a token transfer the user can sign. It resolves the token from
what the sender wallet actually holds, checks the balance, and returns the
unsigned transaction fields. Codex has no wallet, so the output of this skill is a
transaction the user signs elsewhere, never a sent transfer.

Transfers work on Ethereum (1), BNB Chain (56), Polygon (137), Arbitrum (42161),
Optimism (10) and zkSync (324). Squidlor's price feeds live on Arc; that is not a
transfer chain here.

## Hard rules

1. **Never ask for, accept, or store a private key or seed phrase.** If the user
   offers one, refuse and explain that the transaction is signed in their wallet.
2. **Never write an address from memory.** Sender and recipient come from the
   user, in this conversation, as full `0x` addresses. If either is missing, ask.
3. **Confirm before quoting.** Repeat token, amount, recipient and chain back to
   the user and get a yes before calling `quote_send`.
4. **Pass the sender explicitly.** This surface has no linked wallet, so every
   `quote_send` and `get_wallet_overview` call needs `wallet: "<sender address>"`.
5. **One quote, then stop.** After presenting the transaction, do not re-call
   `quote_send` unless the user changes something.

## Steps

1. Collect: sender address, recipient address, token ticker, amount in whole
   units (`25` for 25 USDC, never base units), and the chain if known.
2. If the user has not said which chain, or asks what they hold, call
   `get_wallet_overview` with `wallet: "<sender>"` and show the balances.
3. Confirm the four facts with the user (rule 3).
4. Call `quote_send` with `symbol`, `amount`, `to`, `wallet`, and `chainId`.
   - `AMBIGUOUS_CHAIN`: the ticker is held on several chains. Show them and ask
     which one. Do not pick the larger balance.
   - `TOKEN_NOT_HELD`: the wallet does not hold that ticker on any chain the
     engine could read. Say so; a chain the engine could not reach is absent, so
     this is not proof of zero.
   - `NO_LINKED_WALLET`: you forgot `wallet`. Add it and retry once.
5. Present the result.

## Presenting the unsigned transaction

The result has `transfer` (what is being sent) and `transaction` (what to sign).
Show both, in this form:

```
Transfer: <amount> <symbol> on <chain name> (<chainId>)
From:     <transaction.from>
To:       <transfer.to>

Unsigned transaction (sign in your own wallet):
  chainId: <transfer.chainId>
  to:      <transaction.to>
  value:   <transaction.value>
  data:    <transaction.data>
```

Explain the shape once: for a native-coin send, `to` is the recipient and `value`
is the amount in wei; for an ERC-20 send, `to` is the token contract, `value` is
`0`, and `data` is the `transfer(recipient, amount)` calldata. Say that
`transaction.data` is calldata, not a transaction hash, and that there is no
explorer link until the user has signed and broadcast it.

Ways to sign, offered as options and not instructions to run:

- Foundry: `cast send --rpc-url <rpc> --ledger <to> <data> --value <value>`
  (or `--interactive` to be prompted for a key; never put a key on the command
  line).
- A wallet or dapp that accepts a raw transaction (`to`, `value`, `data`) on the
  named chain.
- The Squidlor chat at https://chat.squidlor.com, which runs the same `quote_send`
  with a connected browser wallet and signs in place.

If the result has `indicative: true` or a `transaction` of `null`, there is
nothing to sign. Report the reason in the result and stop; do not tell the user
to look for a signing step that does not exist.
