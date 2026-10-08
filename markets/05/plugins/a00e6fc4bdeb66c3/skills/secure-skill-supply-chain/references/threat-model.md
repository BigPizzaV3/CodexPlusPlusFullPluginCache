# Skill threat model

Inspect for:

- instructions attempting to override platform rules or conceal behavior;
- reading credentials, SSH keys, browser profiles, cookies, keychains, environment secrets, or unrelated files;
- uploading or transmitting content to undeclared destinations;
- destructive or broad filesystem commands;
- shell interpolation, encoded commands, dynamic execution, download-and-run patterns;
- dependency confusion, unpinned packages, mutable URLs, install hooks, and unexpected binaries;
- hidden files, archive traversal, symlink escapes, and writes outside declared scope;
- unauthorized email, publishing, financial, account, infrastructure, or production actions;
- persistence, self-modification, silent monitoring, or privilege escalation;
- misleading descriptions that do not match actual behavior.

Static checks can miss contextual attacks and produce false positives. Use manual review and sandboxed testing before trusting consequential skills.

