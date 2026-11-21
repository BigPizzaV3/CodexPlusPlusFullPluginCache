# Personal permissions

Version: 3.1.0. The server checks account access, ownership and scopes on each request. Workspace features require current server eligibility, an active FCC PRO plan and the relevant personal tool permissions. Installing a package does not grant permissions or make another account eligible.

1. office:read reads the existing personal FCC context and permitted private results. office:write saves existing private drafts, goals and supported personal records. Neither permits public sending or a personal approval.
2. office:contacts reads one selected minimal owned contact. It does not export phone, email, private notes or the full CRM.
3. office:workspace:read reads permitted own work, sources, revisions and evidence. office:workspace:write prepares private proposals. Important changes remain pending personal portal review.
4. office:contacts:history adds a selected owned structured relationship history. It remains separate from office:contacts and does not expose old free text notes, phone or email. Due selections stay bounded by current permission and ownership.
5. office:comments reads the owner's independently connected public comment source. Together with office:write it prepares typed replies, never approval or sending. A private connection belonging to someone else cannot be borrowed.
6. office:contacts:import stages photo or text import proposals. It does not export the existing address book or authorize a final import.
7. office:team:read reads only the currently permitted FCC team and current member sharing choices. It never includes private CRM, messages, phone, email or drafts. Missing information is not inactivity. Nested team CC values are not added together.
8. office:catalog:read and office:recommendations:write support the exact market, approved facts and the owner's recommendation draft. They do not authorize claims, publication or a purchase.

If a new scope is missing, the server returns insufficient_scope. Ask for the relevant new personal authorization through FCC. Do not edit an OAuth URL, collect a credential or silently reuse another account. Revocation prevents future reads; already copied chat text cannot be remotely erased.