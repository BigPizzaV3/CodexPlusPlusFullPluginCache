# Default conventions

The conventions the **public edition** ships under the skill name `juicylucy`,
in place of the agency's own (`workspace/juicylucy/`). Same five files, same
keys, same shape — the `ad-naming` tool and every engine skill read both
without knowing which they have — with generic values where the agency's are
its own: no uploader-specific folder tokens, no legacy author initials, no
pointer to a live planning document.

The skill name stays `juicylucy` on purpose. The naming tool resolves the
conventions by that catalogue name, every engine skill cites it, and a public
user overrides it exactly the way a teammate does — a copy under the same name
in `~/.agents/skills`. Renaming it for the public edition would have meant two
names for one slot.

Both editions are built from `build/build-plugin.mjs`; the internal one takes
`workspace/`, the public one takes this directory, and neither ever sees the
other. A test holds the two skills to the same JSON keys, so a key added to
one without the other fails the build rather than the first public user.
