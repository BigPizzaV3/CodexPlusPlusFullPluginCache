# Connected backends

For persistence beyond per-block `sup.state`, use a backend the customer owns, registered under **Settings → Integrations →
Connected backends** (Supabase today). Supersimple mints a short-lived token per viewer, so the
backend's own rules (Postgres RLS) decide what each person may read or write — no service keys, and
nothing to store in the app.

```yaml
# app.yaml
app:
  name: pilot-notes
  backends: [supabase-customer-data]     # names from the workspace registry; required to reach them
```

```js
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2';

const db = createClient(SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY, {
  accessToken: () => sup.auth.getToken({ backend: 'supabase-customer-data' }),
});
// Run a write from an explicit user action, and surface errors:
const { error } = await db.from('notes').insert({ body: 'hi' });
if (error) throw error; // runs as the viewer, guarded by the configured RLS
```

The URL and publishable key are safe in app code; the viewer's identity comes from the minted token.
Tokens expire after five minutes. `sub` is the workspace membership ID, not a Supabase auth uid;
claims also include `email`, `role: authenticated`, and `aud` set to the backend ID. Design RLS
around these claims.
A declared backend the admin has not registered renders as a setup message instead of the app. Apps
can fetch only declared, registered backend origins. Configure the backend to trust Supersimple's
viewer tokens and apply suitable RLS policies; adding the manifest entry alone does not grant data
access. Never embed a service-role key or Supersimple API token in the app.
