# Listin3D

Listin3D is a marketplace where products are presented in interactive 3D. This plugin connects your assistant to your Listin3D account and teaches it how to bring 3D models and scenes into your listings.

## Use it

- Search published products and open their 3D pages: "Find sofas in Istanbul I can explore in 3D."
- Manage saved products and follow your listing requests and team feedback.
- Update your display name and language, and create or update your public seller store after approval.
- Prepare or edit a private seller draft: the assistant asks for missing details, reads its current version, imports only the photos/PDF plans you select and asks about content rights before submitting for staff review.
- Send 3D: "Make a Three.js scene of my lamp and send it to my listing." The `listin3d-3d-scenes` skill builds a GLB model or single-file HTML scene that follows Listin3D's rules, checks it, asks you to confirm your rights, and sends it with the connector. Listin3D staff review, place and publish it.

Connect your existing account with OAuth when prompted; choose permissions and switch accounts on the consent screen. No API key is needed. Set-up help: https://listin3d.com/connections. The onboarding skill guides this workflow and the connected account's workspace provides links to its authorized web features.

## Data

The plugin sends the requests you make and the selected listing/3D files to Listin3D at `https://listin3d.com/mcp`. Public catalog, stores and conceptual demonstrations are accessible without signing in. Private account tools read only the connected account's favorites, store and listing requests. Uploaded proposals remain private until staff publish them. You can revoke access at any time on https://listin3d.com/connections. Privacy policy: https://listin3d.com/privacy. Support and deletion requests: https://listin3d.com/support.

The plugin offers discovery and listing workflows. Purchases, payment and delivery use external sellers' websites. Staff moderation, publishing, role administration and credential changes use the authenticated Listin3D website.
