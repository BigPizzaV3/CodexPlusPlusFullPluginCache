# Dispro licensing decisions — approved scope

The publisher approved free use of the proprietary toolkit and, separately,
users' ability to modify, distribute and sell audio plugins they generate.
The root LICENSE and OUTPUT-LICENSE.txt implement that separation.

| Material | Permission |
|---|---|
| Dispro builder, runtime, CLI/MCP, skill, docs and branding | Free unmodified personal/commercial use; necessary use/installation/backup copies. No toolkit modification, redistribution, sublicensing, sale or rebranding grant. |
| First-party template source, generated metadata and compiled output | Modify, incorporate, distribute, sell and sublicense as part of audio plugins, including source or closed-source binaries. No royalties, revenue limits or forced source disclosure. Preserve the output notice. |
| Independently authored user work | Existing ownership and rights remain unaffected. |
| LV2 core header and COPYING | Original ISC terms and notices apply unchanged. |

Generated scaffolds and bundles carry the output licence as LICENSE and
OUTPUT-LICENSE.txt plus LV2-COPYING. They do not carry the toolkit's restrictive
licence as their own licence. The installed builder retains its own LICENSE.
The output permission does not extend to the reusable generator, validation
or packaging code. Model-generated additions require their own provenance and
validation; this licence cannot grant rights in other people's material.

JUCE, AAX and ASIO are absent. Adding any SDK requires reviewing the exact
version's access and redistribution terms. No promise of universal platform,
DAW, signing or directory readiness follows from a licence or compile pass.

The public directory and website release still require publisher review of
the finished pages/package, site-owner integration, verified listing URLs and
applicable platform submission requirements. Platform permissions should be
handled in the publisher's distribution agreement, not invented as a general
toolkit redistribution grant to end users. Readable source is not a technical
secrecy boundary; the toolkit's restriction is a licence restriction.

The old permissive rc.1 candidate remains withdrawn. This records the current
publisher decision and does not purport to revoke upstream rights or rights
in any unknown externally distributed earlier copy.
