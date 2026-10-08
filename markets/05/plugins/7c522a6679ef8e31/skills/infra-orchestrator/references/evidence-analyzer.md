# Evidence Analyzer Module

Use when infrastructure evidence requires structured extraction, identity normalization, relationship mapping, inventory construction, cross-source reconciliation, or conflict analysis. Do not use merely because one screenshot, command output, or log snippet is present.

## Method
1. Identify each source, capture date/version, collection scope, and project/customer context.
2. Extract stable identities first: hostname, serial, UUID, WWPN, IP, client ID, storage-policy/plan name, switch domain, array ID.
3. Build relationships instead of isolated lists when relationships matter to the task.
4. Use the canonical skill evidence states: Verified, User-confirmed, Engineering inference, Recommendation, Conflict, Stale/Superseded, and TBD/Unverified.
5. Treat `Verified` as valid for the evidence's capture time and scope, not as permanently current.
6. Prefer current machine-generated evidence for observed current state while considering capture time, collection scope, source authority, completeness, and tooling limitations.
7. Do not equate missing collection output with evidence of absence.
8. Never silently merge similarly named objects or silently resolve credible conflicts.
9. Hand unresolved faults to Troubleshooting and version-sensitive interpretation to Vendor Research.

## Canonical relationship examples
VMware: Host -> Cluster -> HBA -> WWPN -> Fabric -> Zone -> Storage -> Datastore -> VM.
Commvault: Client -> Agent -> Subclient/VM Group -> Plan/Storage Policy -> Schedule -> Copy -> MediaAgent -> DDB -> Library.
SAN: Switch -> VSAN/Fabric -> Port -> Alias -> Zone -> Zoneset -> Initiator/Target.
