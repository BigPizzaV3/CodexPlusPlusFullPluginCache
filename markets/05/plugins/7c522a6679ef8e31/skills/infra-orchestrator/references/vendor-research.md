# Vendor Research Module

Use when a conclusion materially depends on current supportability, compatibility, exact versions/builds, firmware/driver combinations, licensing, upgrade paths, EOL/EOS, known issues, version-sensitive or state-changing commands, uncertain syntax, or best practices that affect production reliability.

Do not require live research for stable concepts or harmless read-only commands unless uncertainty exists.

## Source order
1. Official vendor compatibility/support matrix.
2. Official release notes, upgrade guides, command references, advisories, and KBs.
3. Official validated designs / field guides where applicable.
4. Professional vendor/community sources as secondary evidence, clearly distinguished from official support statements.

## Verification rules
- Verify the exact product, version/build, platform, firmware/driver, and topology when the claim depends on them.
- Do not infer support from memory, "it probably works," or a different release.
- Check freshness when an older official document may no longer represent current support.
- If authoritative verification is unavailable or inconclusive, state `Not verified` and keep any useful engineering reasoning clearly labeled.
- Never fabricate a source, citation, document title, URL, support statement, command, or compatibility result.
- Keep official evidence distinct from community experience and engineering inference.

## Citation discipline
When citations are supported and the claim is release/supportability-sensitive:
- cite the authoritative source used;
- prefer the most specific source for the exact claim; and
- include publication/update date or date checked when freshness materially affects the conclusion.

## Output proportionality
For engineering supportability/compatibility decisions or production approval, use a structured result when useful: `Supported`, `Unsupported`, `Conditional`, or `Not verified`; exact scope; prerequisites/limitations; relevant known issues; upgrade path/minimum version when applicable; and source-backed commands.

For a small vendor-backed factual or syntax question, answer concisely. Do not force the full supportability schema when it does not help.
