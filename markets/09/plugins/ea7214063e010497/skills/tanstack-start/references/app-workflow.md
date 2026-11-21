# App workflow

## Create or continue

Start with the requested product and inspect the workspace. In a new empty project, use the current CLI blank preset from the skill. In an existing project, preserve its scripts, package manager, lockfile, deployment adapter, and architecture. Use CLI add-on discovery before selecting an integration, inspect its details and requirements, then add only the needed integration. Do not reinstall Start merely to add a page.

Load matching Intent skills before changing routes, data loading, server functions, middleware, authentication, execution boundaries, or deployment. Routine JSX and CSS can follow existing patterns without loading unrelated guidance. List and detail routes can be siblings such as `items.index.tsx` and `items.$id.tsx`; an `items.tsx` parent must render an `Outlet` for its children.

Build one useful screen first, then complete the requested behavior. Use real actions and explicit empty, loading, error, and success states where needed. Keep every visible sentence useful, remove starter slogans and redundant labels. Headless TanStack libraries provide behavior rather than finished visual components.

## Preview

Run the project's development command in a retained session. Use the exact healthy server URL from its output. If the host provides a browser or `open_in_codex`, open that URL and keep the server alive during edits. Otherwise provide the URL as a local preview and explain which machine it runs on. A localhost URL is not a public deployment.

Check the rendered result using available browser tools: primary interaction, keyboard access, narrow screen layout, page navigation, and visible errors. Remove redundant interface copy. If browser access is absent, complete compilation and behavior checks that are available and state that visual behavior is unverified.

## Validate

Run the existing build command and the project's type, lint, and test checks appropriate to the change. Do not assume a bundler build type-checks TypeScript. Check at least one server-rendered route and a browser navigation when the tooling permits. For server functions, test valid and invalid input and permission boundaries. Keep server secrets out of the client bundle. Check generated route tree changes rather than editing them manually. Fix the cause of failures instead of disabling checks or substituting a mock for requested production behavior.

## Host

Use the user's selected hosting provider and its current Start guide. Deployment is conditional on available hosting tools, account access, and user authorization. Inspect the project's existing adapter and provider configuration before changing them. For a new target, use current CLI deployment options shown by `create --help` and the provider's official guide, do not assume all providers emit the same server files.

If OpenAI Sites and compatible TanStack Sites building/hosting skills are available, load those skills and follow their current adapter, packaging, resource, secret, preview, and deployment requirements. Their tools are a separate host capability, not included in this docs plugin. Do not copy machine-specific cache paths or depend on local picker/initializer scripts. If that workflow is unavailable, use another authorized provider or deliver the validated app plus the exact missing deployment action.

Before deploying, complete the production build, verify required environment keys and persistence resources, and ensure the selected runtime supports the server code. Server functions require a compatible server runtime unless the app is deliberately configured for a supported static/SPA mode. Local file writes are not a portable database. Store durable records in the chosen supported backend.

Deploy to a dedicated or explicitly selected project using the provider's supported command/tool. Preserve unrelated deployments. Verify the returned public URL, route loading, static assets, and relevant server behavior. Report a deployed URL only after deployment evidence exists, and distinguish a preview from production. Never place deployment credentials in app source or artifact bundles.

For migration details use the official [Next.js migration guide](https://tanstack.com/start/latest/docs/framework/react/migrate-from-next-js) and current Intent skills where applicable; do not pretend a guide exists for every framework.
