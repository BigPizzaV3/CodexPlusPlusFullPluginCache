# Existing-project upgrade protocol

## 1. Resolve scope and authority

Distinguish report-only requests from implementation requests. For an implementation request, keep the audit and plan concise and continue into safe in-scope changes without a second approval pause. Identify the project root and confirm editable source is present. Read applicable repository instructions and inspect Git status before edits.

## 2. Establish the baseline

Discover install, development, test, build, migration, preview, and deployment commands from the repository. Use the project's existing package manager and lockfile. Run safe existing checks and record pre-existing failures. For a user interface, start the app and inspect representative routes at desktop and mobile widths before changing it.

## 3. Build the preservation map

Map entry points, routes, page shells, shared components, services, data models, authentication and authorization, integrations, configuration, assets, tests, deployment, and critical journeys. List behaviors, APIs, schemas, URLs, analytics, SEO, brand elements, content, and persistent data that must remain stable. Identify stateful or irreversible operations.

## 4. Prioritize the work

Rate findings by user impact, confidence, effort, and regression risk. Separate functional defects and incomplete setup from design preferences. Classify work as must fix, recommended, or optional redesign. Ask only about unresolved choices that materially change the result; choose reasonable reversible defaults for the rest.

## 5. Implement in controlled phases

Prefer stabilization before redesign, shared foundations before page-level polish, and measurable checks after each phase. Preserve the project's stack unless replacement is requested or required for a demonstrated blocker. Avoid combining a framework migration with a visual redesign unless the user clearly authorized both.

For setup work, repair existing configuration and scripts rather than generating a parallel project. Keep the current package manager, environment conventions, routes, and deployment target. Document environment-variable names but never expose or invent secret values. For database or API changes, define compatibility, migration, backup, and rollback before mutation.

## 6. Verify and finish

Run project-native checks, exercise affected critical journeys and error states, and inspect rendered interface changes. Fix in-scope failures and rerun affected checks. Document implemented changes, evidence, pre-existing failures, remaining blockers, new commands, migrations, environment-variable names, deployment steps, and rollback. Do not present recommendations as completed work.
