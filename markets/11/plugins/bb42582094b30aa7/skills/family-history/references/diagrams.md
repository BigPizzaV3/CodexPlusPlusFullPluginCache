# Diagram examples

Use the current tool schema and real immutable IDs resolved from the connected tree. All IDs below are illustrative variables, not stored people or default lookup targets. These are read-only presentation requests, never instructions to create records.

## Natural follow-ups

After a tree summary, “Show me some of it” uses show_tree with the established treeId, direction ancestors, generations2 and limit15, followed by visible image output of unchanged SVG when that host channel exists. Otherwise use render_family_diagram for the compact MCP Apps selector. Omit rootPersonId when the linked/focal person is intended. Do not ask the user to repeat “colourful” or “visual”, or rebuild prior prose as native graphics. “Highlight those two” reuses the known IDs and scope, then calls the renderer again. “Summarise the research gaps” remains a conversational answer rather than an automatic tree.

## Named people and overlapping groups

```json
{
  "treeId": "known_tree_id",
  "rootPersonId": "known_reference_id",
  "direction": "ancestors",
  "generations": 3,
  "limit": 60,
  "highlightGroups": [
    {"label": "Compare records", "colour": "pink", "personIds": ["known_ada_id", "known_edward_id"]},
    {"label": "Next research", "colour": "amber", "personIds": ["known_edward_id"]}
  ],
  "dimOthers": true
}
```

Edward retains both labels and the first group's pink outline. Use highlightPersonIds for an unnamed attention mark. An eligible ID outside the current view appears in offViewPersonIds; highlighting never silently expands the view. Explain that briefly, then refocus if requested. Protected/unavailable IDs fail generically and must not become hidden-person placeholders.

## Descendants coloured by research work

```json
{
  "treeId": "known_tree_id",
  "rootPersonId": "known_ada_id",
  "direction": "descendants",
  "generations": 3,
  "limit": 60,
  "colourBy": "research",
  "highlight": {"researchBelow": 50}
}
```

Exactly50% does not match the strict threshold. Research percentage counts completed recorded review checks. It is not confidence, evidence quality or a guarantee of exhaustive research. Keep complete recorded dates and all returned panels. A confirmed identity may still have0% research coverage.

## Close family with uncertain identities

```json
{
  "treeId": "known_tree_id",
  "direction": "neighbourhood",
  "generations": 2,
  "limit": 25,
  "colourBy": "identity",
  "highlight": {"identityStatuses": ["Probable", "Candidate", "Unidentified"]},
  "dimOthers": true
}
```

Neighbourhood counts graph links, including siblings/partners. The renderer derives actual genealogical rows from typed parent links. Do not call it a complete two-generation pedigree. Identity colours do not prove relationships. Blue/purple branch colours are the default when no different colour meaning is requested.

## Recorded path with an uncertain direct link

```json
{
  "treeId": "known_tree_id",
  "rootPersonId": "known_ada_id",
  "targetPersonId": "known_grace_id",
  "direction": "connection",
  "generations": 5,
  "limit": 60,
  "colourBy": "connection",
  "highlight": {"connectionStates": ["uncertain"]}
}
```

This displays one shortest recorded route within five links. A missing route within that bound does not prove no family relationship. get_connection assesses evidence independently and can select a different route. A documented alternative route does not prove a disputed parent link; preserve each dashed direct edge and its label.

## Rule semantics and intersections

To mark factual disagreements use highlight.conflicts="facts"; identity/relationship conflicts use "material"; either kind uses "any". Multiple supplied rules, explicit IDs and group membership combine with OR. For example identityStatuses=["Candidate"] plus researchBelow=50 marks Candidates **or** profiles below50%, not only Candidates below50%. For a requested intersection, use a focused structured read to resolve the matching displayed IDs and pass highlightPersonIds instead. Do not fetch every profile separately for styling.

## Bounds and unsupported requests

Up to four groups,100 eligible profiles,1–5 steps and50 compact panels are supported. Render all returned panels as visible images under their titles, or through the compact app selector; do not claim private/deeper records are included. Re-render at a requested deeper scope rather than using only names already in chat. Report complete/reason/limitReached and no-match notes honestly. Cycles or inconsistent constraints must not be turned into invented generations. The schema rejects unsupported options; explain an actual limitation rather than promising arbitrary layouts or altering genealogy to arrange boxes.

Search, clickable profile inspection and zoom/pan belong in open_family_workspace when requested. A static diagram is not an editor. Exact prepared SVG is the inline visual. Deterministic rasterization into visible image output preserves it; do not hand-redraw it, generate an illustration, print text art or duplicate the full workspace.

## Capability check before static rendering

Only an explicitly user-visible image-output tool qualifies for native image delivery. A background shell/command/container, Python or CairoSVG installation, IPython display import, saved PNG and subagent preview do not qualify. If no visible image channel is present, call render_family_diagram directly with the same arguments instead of running background rasterization or claiming a command displayed the tree.
