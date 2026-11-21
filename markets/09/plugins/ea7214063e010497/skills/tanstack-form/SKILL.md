---
name: tanstack-form
description: Introduce, add, debug, or migrate TanStack Form for typed form state, field validation, and submission.
---

# TanStack Form

Typed form state, field validation, and submission.

Use it for: Interactive forms with touched state, dynamic fields, validation, or reusable field components.

Usually unnecessary for: A simple native form that can submit without client-side state.

## Install and try

Use the project's framework and package manager. These examples target the current official documentation checked on September 30, 2026. Match installed versions before copying them into an existing project.

```sh
npm install @tanstack/react-form
```

Minimal example, paste into an existing React app:

```tsx
import { useForm } from '@tanstack/react-form'
export function NameForm() {
  const form = useForm({ defaultValues: { name: '' }, onSubmit: async ({ value }) => console.log(value) })
  return <form onSubmit={event => { event.preventDefault(); event.stopPropagation(); void form.handleSubmit() }}>
    <form.Field name="name">{field => <label>Name <input value={field.state.value}
      onBlur={field.handleBlur} onChange={event => field.handleChange(event.target.value)} /></label>}</form.Field>
    <button type="submit">Save</button>
  </form>
}
```

Validate at the timing the user needs. Display errors tied to the relevant field and validate again on the server. Inspect reactive form state through framework subscriptions, not a plain property read. Add schema libraries only when useful.

## Implement, debug, or migrate

Read the project's package manifest and lockfile before changing dependencies. Load version-matched TanStack Intent guidance with `npx @tanstack/intent@latest list`, then `npx @tanstack/intent@latest load` followed by a concrete identifier returned by the list. Do not invent skill names or assume every version includes skills. If no relevant skill is packaged, use the installed version's official docs and source. Current web docs can describe a newer API than the lockfile.

For an existing project, reproduce the failure and change the smallest relevant integration. For migration, read the version-specific migration guide and preserve behavior through a small verified slice before migrating the rest. Run the project's relevant build and checks, then verify the user-visible feature. Do not add unrelated TanStack packages.

In ChatGPT without a shell or repository tools, use the connected documentation tools and provide the code and exact commands for the user to run. Never claim files were edited, packages installed, or checks passed without execution evidence.

[Official docs](https://tanstack.com/form/latest/docs/framework/react/quick-start) · [Version-matched guidance](https://tanstack.com/intent/latest/docs/overview)
