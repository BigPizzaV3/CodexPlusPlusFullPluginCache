---
name: build-integration
description: Write working code that calls IPGeolocation.io APIs in any programming language, using the published documentation and API specification. Use when the user asks for a code example, how to call the IP Geolocation, IP Security, ASN, Abuse Contact, Time Zone, or User Agent API, or how to add geolocation, VPN detection, or localization to an app.
---

# Build an IPGeolocation.io integration

1. For curl, JavaScript, Python, PHP, or Go, start with `generate_api_example`. It builds the request from the published API specification.
2. For any other language, use `search` and `fetch` to read the matching documentation page, confirm the endpoint, parameters, and response fields, then write the code.
3. Read the API key from an environment variable or a secret store. Never put a key in the code, and never ask the user to paste one into the chat.
4. Use the exact field names from the documentation, request only the fields or modules the app needs, set a request timeout, and handle error responses.
5. Link the documentation page the code is based on.
