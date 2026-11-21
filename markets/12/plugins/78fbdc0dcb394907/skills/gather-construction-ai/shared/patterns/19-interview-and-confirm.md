# Pattern 19: Interview-and-Confirm (Shared Skeleton)

Skills that create a local rates/facts profile the user owns (`commercial-profile`,
`contract-profile`, and any future producer of a Pattern-13/14-style file) follow the same
five-step skeleton. Cite this pattern instead of restating the steps; the producer skill's own
workflow.md holds only its specific question groups and file schema.

**1. Resolve the project.** Use Pattern 1. If a Gather connection exists, verify the resolved
name against `getMyProjects`/`getProjects` so the profile's `project` field matches Gather
exactly; without a connection, proceed with the name given — these skills work standalone.
Determine the filename: `<profile>.md` for a single project worked on in this directory, or
`<profile>-<project-slug>.md` once more than one project is in play (existing slugged files, or
the user naming more than one project, are the trigger). If a profile already exists for this
project, switch to Update Mode (targeted questions about what changed) instead of a fresh
interview.

**2. Interview in one grouped message.** Ask every question the schema needs under headings in
a single message — never as a drip of separate questions. Each heading names the skill(s) that
consume that group, and the user may skip any group; a skipped group means the corresponding
skill runs degraded (quantities-only, standard-form, etc. — per the relevant profile pattern),
never blocked. Keep the question count proportionate: enough to populate the schema, no
speculative or "nice to know" fields.

**3. Confirm as a table.** Before writing, render everything captured back as a table (or
grouped list matching the interview headings) and ask for confirmation or corrections. Never
write straight from the interview answers without this check — transcription errors in rates
and contract terms are exactly the failures this profile exists to prevent.

**4. Write the local file.** Only the producer skill writes it (never a consuming skill). Use
the file convention and schema from the specific profile's own pattern (13, 14, …). Include the
profile date. Where the content is commercially or legally sensitive, remind the user to keep
it out of shared repositories.

**5. Next steps.** Name the consuming skills that now unlock priced/amended-form output, and
point to Update Mode for later changes. Do not run a consuming skill automatically — the user
invokes it next.
