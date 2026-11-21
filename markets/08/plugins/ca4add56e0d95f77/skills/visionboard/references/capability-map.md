# VisionBoard MCP capability map

The plugin points to the same production OAuth MCP endpoint used by standalone MCP clients. It does not maintain a separate Goal-only tool list. Available calls always depend on the installed server contract, the person's fresh OAuth grant, Vision scope, current role, entitlement, and object state.

Every host in this list — Codex, ChatGPT Work, Claude Code, Claude Desktop, and other MCP clients — reads the same contract through the same consent. Only the presentation below differs by host; the tools, scopes, and human decision boundaries do not.

## Conversation workspace

- `show_visionboard` renders compact Direction, Goals, Library, Boards, Goal work, or one quiet end-of-work status check inside a host that draws it, such as a compatible Codex or ChatGPT conversation.
- The renderer carries identifiers only. It re-reads through the canonical tools below and has no independent database, permission model, object copy, or write path.
- For creating an image with existing references, `show_visionboard` with `view: "references"` opens a visible multi-image gallery in the verified Vision. Optional `referenceIds` are candidate canonical Image IDs, not selected files. People choose up to six approved pictures and explicitly transfer them together when the host supports file attachment; generator support remains a separately verified host capability.
- Hosts that render tool results as text, including coding agents such as Claude Code, keep every capability below. They carry the same single outcome in a written summary with the exact identifiers, state, and scoped VisionBoard link. Check the tool list instead of assuming which kind of host is connected.
- Safe actions return to the connected model and use the ordinary governed tool. Exact human approval uses the same immutable Approval Bundle whether shown as a card, written out in text, or opened on VisionBoard.
- Use exactly one completion surface: status when the pinned Direction is still current and no strategic object changed, the Approval Bundle for an exact Review, or the focused Goal Run for one human decision or Definition-of-Done check.
- The full product remains available for spatial editing and dense administration through progressive disclosure; opening it is not required for routine reads and governed Draft work.

## Approved direction and complete-context accounting

- Discover Visions and current priorities.
- Read approved context, Direction, Brand Guidelines, Products, Goals, assets, strategy and Board briefs.
- Inventory every visible and withheld element through the context manifest.
- Page through exact permitted representations without treating search, summaries, or embeddings as completeness proof.

## Governed Library work

- Create and revise attributed Draft Notes, Goals, written Documents, and supported exact Markdown, text, or safe SVG Documents.
- Read exact revisions and diffs, request human Review, and inspect Review state.
- Create and revise complete Brand Kits, Products, and Images through the structured Library contract.
- Read and compare exact structured Library revisions.

## Boards and collaboration

- Read complete Board graphs with canonical references, geometry, provenance, and Review state.
- Create editable Draft Boards and propose exact Board revisions.
- Read the Board template catalog (`visionboard://board-templates`) and recommend a picture template. A person applies it in VisionBoard through the returned link; `create_draft_board` cannot create native template picture slots.
- What an approved Board's cards say is part of searchable Vision context, so a retrieval result may come from a Board rather than a Document. Cite the Board it came from, and still read the Board graph when the exact composition matters.
- List open comments and reply as the identified connected AI for the commissioning person.
- Inspect durable Action Receipts and pending governed actions.

## Human decision boundaries

- Prepare and inspect exact approval bundles; a person approves or declines through the protected decision surface.
- Prepare and inspect a strategic Vision creation request; a person authorizes the exact proposal before creation.
- Prepare evidence for Goal Done or reopen; a person decides the lifecycle change.
- Never infer approval, creation authority, access changes, or completion from ordinary chat text.

## Long-running Goals

- List and inspect human-activated Goal Runs.
- Claim one due leased cycle, perform bounded aligned work, checkpoint evidence, and exit.
- Pause for changed Direction, contradiction, or one strategic human decision.
- Ask the person to verify Definition of Done; never mark the Goal Done autonomously.

## Provenance

- Preserve the connected AI identity and commissioning person on every generated or edited object.
- Attach non-secret repository provenance only when the server releases that capability and the grant includes it.
