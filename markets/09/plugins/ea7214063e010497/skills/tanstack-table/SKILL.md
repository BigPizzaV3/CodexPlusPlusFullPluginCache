---
name: tanstack-table
description: Introduce, add, debug, or migrate TanStack Table for headless row, column, and table feature logic.
---

# TanStack Table

Headless row, column, and table feature logic.

Use it for: Sortable, filterable, selectable, or paginated data tables with custom markup.

Usually unnecessary for: A short static HTML table. Table does not fetch data or supply visual styles.

## Install and try

Use the project's framework and package manager. These examples target the current official documentation checked on September 30, 2026. Match installed versions before copying them into an existing project.

```sh
npm install @tanstack/react-table
```

Minimal example, paste into an existing React app:

```tsx
import { tableFeatures, useTable } from '@tanstack/react-table'
import type { ColumnDef } from '@tanstack/react-table'
const features = tableFeatures({})
type Row = { name: string }
const data: Row[] = [{ name: 'Tanner' }]
const columns: ColumnDef<typeof features, Row>[] = [{ accessorKey: 'name', header: 'Name' }]
export function People() {
  const table = useTable({ features, data, columns })
  return <table><thead>{table.getHeaderGroups().map(group =>
    <tr key={group.id}>{group.headers.map(header => <th key={header.id}>
      {header.isPlaceholder ? null : <table.FlexRender header={header} />}
    </th>)}</tr>)}</thead><tbody>{table.getRowModel().rows.map(row =>
    <tr key={row.id}>{row.getAllCells().map(cell =>
      <td key={cell.id}><table.FlexRender cell={cell} /></td>)}</tr>)}</tbody></table>
}
```

This is the current v9 API. Installed v8 uses useReactTable and getCoreRowModel instead. Do not silently upgrade an existing table to v9. v9 features and row models are opt-in through tableFeatures. Keep data and column references stable. Add Virtual only when rendered row count warrants it.

## Implement, debug, or migrate

Read the project's package manifest and lockfile before changing dependencies. Load version-matched TanStack Intent guidance with `npx @tanstack/intent@latest list`, then `npx @tanstack/intent@latest load` followed by a concrete identifier returned by the list. Do not invent skill names or assume every version includes skills. If no relevant skill is packaged, use the installed version's official docs and source. Current web docs can describe a newer API than the lockfile.

For an existing project, reproduce the failure and change the smallest relevant integration. For migration, read the version-specific migration guide and preserve behavior through a small verified slice before migrating the rest. Run the project's relevant build and checks, then verify the user-visible feature. Do not add unrelated TanStack packages.

In ChatGPT without a shell or repository tools, use the connected documentation tools and provide the code and exact commands for the user to run. Never claim files were edited, packages installed, or checks passed without execution evidence.

[Official docs](https://tanstack.com/table/latest/docs/framework/react/quick-start) · [Version-matched guidance](https://tanstack.com/intent/latest/docs/overview)
