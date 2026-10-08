# Recovery and continuity design

## Loss scenarios to assess

Test only scenarios relevant to the declared scope, but explicitly consider:

- primary laptop/phone loss, theft, destruction, encryption, or hardware failure;
- owner, employee, contractor, administrator, or key adviser unavailable;
- password manager, authenticator, email, phone number, or identity-provider loss;
- cloud drive, repository host, SaaS, domain registrar, DNS, hosting, database, payment, or communication provider outage/suspension;
- accidental deletion, corrupted sync, ransomware, malicious insider, or compromised account;
- source code, design source, media master, database, configuration, or documentation loss;
- expired domain, certificate, license, subscription, card, contract, permit, insurance, or key rotation;
- legal ownership dispute, vendor failure, client departure, merger, insolvency, or project abandonment;
- extended pause that makes versions, instructions, contacts, or assumptions stale.

## Continuity matrix

For every critical capability capture:

- service/capability and business impact;
- owner and alternate owner;
- dependencies and single points of failure;
- current source of truth;
- minimum viable continuation state;
- recovery time objective (`RTO`) or explicitly `not defined`;
- recovery point objective (`RPO`) or explicitly `not defined`;
- backup/export method, location class, and custody;
- lawful account/access recovery path;
- fallback process or alternative provider;
- last successful backup/export;
- last restore/recovery drill;
- verification evidence;
- stop/escalation conditions;
- residual risk and next improvement.

Do not invent RTO/RPO values. Help the user define them from impact and tolerance.

## Backup rules

For critical information, evaluate version history, independent copy, geographic/provider separation, encryption, key custody, retention, immutability, export portability, corruption detection, and restore verification. A synchronized folder is not automatically a backup. A backup visible in a dashboard is not proven restorable.

Record evidence without exposing encryption keys or recovery secrets.

## Account recovery design

For each critical account, record provider, organization/workspace, service purpose, account owner, administrative role coverage, billing owner, verified recovery email/phone category, MFA category, approved password-manager item reference, domain/identity dependencies, vendor support route, ownership evidence location, alternate administrator, and last review date.

Never initiate password reset, disable MFA, invite admins, change permissions, export private data, or contact support without explicit authorization at action time.

## Replacement-device and workstation recovery

For any device-dependent work, record the supported operating system and architecture, required applications and verified versions, license source and owner, package/toolchain managers, configuration source, browser/profile-independent bookmarks or service map, fonts and media components, drivers, peripherals, external storage, trusted certificates and signing identities by reference, local-only data, synchronization prerequisites, security baseline, bootstrap order, expected checks, and disposal/containment requirements for a lost device.

Prefer reproducible configuration and approved exports over screenshots of settings. Do not copy device secrets, browser sessions, keychains, authentication databases, or licensed files into the second brain. Mark any step that still depends on the lost device as a continuity blocker.

## Recovery sequence design

Order by dependency rather than convenience. A typical chain may be:

1. establish incident authority and secure communications;
2. contain active security or safety impact;
3. restore identity, email, password-manager access, and trusted devices through approved channels;
4. restore domain/DNS and core cloud/repository access;
5. verify integrity and select a clean last-known-good point;
6. restore data, configuration, services, and integrations in dependency order;
7. run verification and business smoke tests;
8. reopen normal operations gradually;
9. retain incident evidence and update the second brain.

This is a pattern, not permission or a universal sequence. Adapt it to actual dependencies.

## Runbook quality

Each runbook requires trigger, authority, prerequisites, safe workspace, dependency order, numbered actions, expected observations, verification, stop condition, escalation, rollback, evidence capture, communication boundary, owner, estimated duration, and last test result.

Where executing the runbook could be destructive, public, financial, legal, security-sensitive, or externally communicative, stop before the action and obtain explicit authorization.

## Clean-room continuity test

Give an authorized tester only the second-brain package and the declared approved tools. The tester must be able to:

- identify scope and authority;
- find canonical current state in under the agreed navigation target;
- identify last known good and exact next action;
- map critical dependencies and owners;
- locate approved access-recovery references without seeing raw secrets;
- reproduce one representative critical process or build in an isolated environment;
- restore one representative backup or verify a permitted restore drill;
- report gaps without consulting the originating chat or operator.

Record tester, date, environment, exact scope, result, evidence, time taken, assistance required, failures, and corrective actions.
