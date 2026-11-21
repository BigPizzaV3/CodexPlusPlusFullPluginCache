# Generated QI project conventions

These requirements are mandatory for generated applications. The standard stack is React,
TypeScript, Vite, shadcn/Radix, Tailwind CSS, React Router, ASP.NET Core 8, SQLite, and EF Core.

## Before the first write

- Build on the template already present at `/workspace/code`; do not recreate the project.
- Read `README.md`, `MyApp.csproj`, `Program.cs`, `appsettings.json`, `Data/AppDbContext.cs`,
  `ClientApp/src/App.tsx`, `ClientApp/src/index.css`, `ClientApp/src/services/api.ts`, and the
  Header, Sidebar, MobileTabNav, and ThemeProvider components.
- Preserve QI authentication, DataPack, connector, branding, preview, static-file, and SPA fallback integration.
- Derive a feature/completeness checklist from the request before implementation.

## Architecture and data

- Store domain records through the generated ASP.NET API, EF Core, and SQLite database at `/data/app.db`.
- Use browser storage only for non-domain UI preferences such as the selected theme.
- Implement complete create, read, update, and delete flows for entity-based apps unless read-only was explicitly requested.
- Use typed frontend API services; do not put persistence or all application logic in one large React component.
- Keep SQLite-compatible model types and prefer attribute-based EF configuration.
- Create migrations with `add_ef_migration`; never hand-write migrations or edit the model snapshot.
- Do not add starter, sample, demo, mock, or seeded records unless the user explicitly requested them.

## React and design

- Retain and extend the template Header, Sidebar, mobile navigation, ThemeProvider, and branding variables.
- Use shadcn/Radix components, Tailwind utilities, and Lucide icons consistently.
- Use semantic colour, accessible labels and controls, keyboard support, responsive layouts, and readable light/dark modes.
- Provide designed empty, loading, error, success, and confirmation states with a clear branded primary action.
- Remove the Weather demo only after replacing it with the requested complete feature.

## Completion

- Call `check_project_standards` and fix every blocking violation.
- Run `check_ef_migrations` when models are involved.
- Run `build_project`, fix all build errors, then run `verify_project`.
- Do not read, write, or infer production data, credentials, protected configuration, or generated directories.
