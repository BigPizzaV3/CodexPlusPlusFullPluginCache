> **Not a schema.** This file shows browser (JavaScript) SDK installation and client-
> initialization examples for In-App Calling. For SDK method signatures and initialization
> options, refer to the canonical `developers.sinch.com` docs linked from the parent
> [SKILL.md](../SKILL.md) before writing code or prose that states payload structure.

# SDK Installation — In-App Calling (Browser / JavaScript)

In-App Calling uses the **Sinch RTC SDK** — a separate client-side SDK from `@sinch/sdk-core`. Authentication is handled via JWT tokens generated on your backend using Application Key + Application Secret credentials.

## Add the SDK

Add the SDK via CDN script tag in your HTML `<head>`:

```html
<!-- Trusted first-party CDN: cdn.sinch.com is owned by Sinch -->
<script src="https://cdn.sinch.com/latest/sinch-rtc-min.js"></script>
```

## Service Worker for Push Notifications

Add a service worker file (`sw.js`) for handling push notifications:

```javascript
this.addEventListener("push", (event) => {
  console.log("ServiceWorker Push: ", event);
  const body = event.data.json();
  event.waitUntil(
    clients
      .matchAll({ includeUncontrolled: true, type: "window" })
      .then((clients) => {
        clients.forEach((client) => {
          client.postMessage({
            visible: client.visibilityState === "visible",
            data: body,
          });
        });
      })
  );
});
```

## Initialize the SinchClient

Use the wrapper class pattern from the [official getting-started guide](https://developers.sinch.com/docs/in-app-calling/getting-started/javascript/create-app.md):

```javascript
const APP_KEY = "YOUR_APPLICATION_KEY";
const ENVIRONMENT_HOST = "ocra.api.sinch.com";

class SinchClientWrapper {
  constructor(userId, ui) {
    this.userId = userId;
    this.ui = ui;

    const sinchClient = Sinch.getSinchClientBuilder()
      .applicationKey(APP_KEY)
      .userId(userId)
      .environmentHost(ENVIRONMENT_HOST)
      .build();

    sinchClient.addListener(this.#sinchClientListener());
    sinchClient.setSupportManagedPush();
    sinchClient.start();

    this.sinchClient = sinchClient;
  }

  #sinchClientListener() {
    return {
      onCredentialsRequired: async (sinchClient, clientRegistration) => {
        // The backend derives the Sinch user ID from the session cookie, not from the request.
        try {
          const res = await fetch("/api/sinch-token", { method: "POST", credentials: "same-origin" });
          if (!res.ok) throw new Error(`HTTP ${res.status}`);
          const { token } = await res.json();
          clientRegistration.register(token);
        } catch (error) {
          clientRegistration.registerFailed();
          console.error("Sinch registration token request failed:", error.message);
        }
      },

      onClientStarted: (sinchClient) => {
        console.log("Sinch - Start client succeeded");
      },

      onClientFailed: (sinchClient, error) => {
        console.log("Sinch - Start client failed");
        console.error(error);
      },
    };
  }
}
```

> **Note:** `setSupportManagedPush()` should almost always be enabled in production — without it, incoming calls cannot be received while the app is unfocused.

## Key Points

- `environmentHost` is the REST API endpoint the SDK targets (`ocra.api.sinch.com` for production)
- `userId` is the user identifier registered within your application
- `SinchClient` is a **singleton per user session** — create one instance and retain it for the entire app lifetime
- The `onCredentialsRequired` callback fires on start and when the registration TTL nears expiry
- **Never embed the Application Secret in client-side code** — generate JWTs on your backend
- WebRTC requires HTTPS — ensure your site is served over a secure context
- Supported browsers: Chrome, Firefox, Safari, Edge
- For more complex examples, see the [reference app](https://github.com/sinch/rtc-reference-applications/tree/master/javascript) or the [SDK documentation](https://developers.sinch.com/docs/in-app-calling/js-cloud.md)

## Links

- [In-App Calling Overview](https://developers.sinch.com/docs/in-app-calling/overview.md)
- [JavaScript Getting Started: Create App](https://developers.sinch.com/docs/in-app-calling/getting-started/javascript/create-app.md)
- [JavaScript Getting Started: Make a Call](https://developers.sinch.com/docs/in-app-calling/getting-started/javascript/make-call.md)
- [JavaScript SDK Documentation](https://developers.sinch.com/docs/in-app-calling/js-cloud.md)
- [Authentication & Authorization (JS)](https://developers.sinch.com/docs/in-app-calling/js/application-authentication.md)
- [SDK Downloads](https://developers.sinch.com/docs/in-app-calling/sdk-downloads.md)
- [Reference Applications (GitHub)](https://github.com/sinch/rtc-reference-applications)

## Backend: JWT Token Generation (Node.js)

Your backend generates JWT tokens using the Application Secret. **Never expose the secret to client code.**

Use [`assets/registration-token-server.mjs`](../assets/registration-token-server.mjs) (Node.js 18+, no dependencies, verified against the Sinch test vectors). It sets the `kid` header to `hkdfv1-<UTC YYYYMMDD>`, uses the `//rtc.sinch.com/applications/...` `iss`/`sub` format, derives the signing key from the UTC date, and defaults to a 600-second token lifetime (Sinch requires at least 60 seconds; 600 is an example, not a Sinch maximum).

```javascript
import http from "node:http";
import { handleTokenRequest } from "./registration-token-server.mjs";

// Replace with your real session check. Return the Sinch user ID this session may use, or null.
async function authenticate(req) {
  return lookUpSessionUserId(req.headers.cookie);
}

http
  .createServer((req, res) => {
    if (req.method === "POST" && req.url === "/api/sinch-token") {
      handleTokenRequest(req, res, authenticate).catch(() => {
        res.writeHead(500);
        res.end();
      });
      return;
    }
    res.writeHead(404);
    res.end();
  })
  .listen(3000);
```

Serve this behind HTTPS. Load `SINCH_APPLICATION_KEY` and `SINCH_APPLICATION_SECRET` from your secret store, and do not log tokens or the secret.

*(Summary only — confirm exact names/encoding/enums against the authoritative [Authentication & Authorization (JS)](https://developers.sinch.com/docs/in-app-calling/js/application-authentication.md) doc before implementing.)*
