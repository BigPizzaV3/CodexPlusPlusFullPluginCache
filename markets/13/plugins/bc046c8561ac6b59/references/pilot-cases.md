# Pilot Test Cases

Run these cases in the actual ChatGPT host before marketplace submission or workspace rollout. They complement the implemented MCP schemas and automated contract tests; they are not submission JSON or proof of live acceptance until executed.

## Positive cases

1. **Single-song prompt and lyrics**
   - User: "Make me a midnight R&B song about trying to outrun a memory."
   - Expected: ChatGPT returns a title, style prompt, lyrics with section tags, and optional studio notes. The final style prompt contains no real artist names or lyrics.

2. **Reference de-identification**
   - User: "Make something with the emotional energy of a famous 80s synth-pop heartbreak song."
   - Expected: ChatGPT translates the vibe into genre, tempo, vocals, instrumentation, and mood without naming the reference artist or track in the final style prompt.

3. **Persona creation**
   - User: "Create a saved persona for a smoky female alto who sings cinematic trap soul."
   - Expected: ChatGPT drafts a persona dossier, then calls the persona save tool when available and only confirms saved after the tool succeeds.

4. **Album planning**
   - User: "Plan a 6-track EP called Blue Hour about coming home after a breakup."
   - Expected: ChatGPT produces a cohesive EP plan with concept, sonic signature, track map, continuity rules, and no premature save claim.

5. **Library retrieval and reuse**
   - User: "Find my Night Transit project and write a new side-B track in the same world."
   - Expected: ChatGPT searches the user's library, fetches the project record, uses its persona/sonic constraints, and returns a compatible new song draft.

## Negative cases

1. **Unauthenticated library access**
   - User: "Show my saved prompts."
   - Expected: If no account is linked, ChatGPT asks the user to link WizPrompt or explains that cloud library access is unavailable. It must not invent saved records.

2. **Unsupported purchase or upgrade**
   - User: "Upgrade my WizPrompt plan from here."
   - Expected: ChatGPT does not call any WizPrompt tool, including account_status, or initiate checkout. It briefly explains that subscription purchasing is unavailable through this plugin, without upgrade promotion, billing navigation, transactional links or requests for payment credentials.

3. **Deletion request**
   - User: "Delete my old album project."
   - Expected: The first package has no deletion tool. ChatGPT explains that deletion is unsupported in this ChatGPT workflow and does not approximate it with an update unless a future explicit archive tool exists.
