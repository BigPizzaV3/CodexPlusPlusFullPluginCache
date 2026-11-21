# Nova Creative brand media

These are the creator-supplied product and brand resources included in this plugin. Relative paths below are from this reference file.

| Resource | File | Details |
| --- | --- | --- |
| Product promo | `../../../assets/nova-creative-promo-1080p.mp4` | Final 56-second 1920 × 1080 H.264/AAC film, 30 fps, unchanged from the supplied original. |
| Promo poster | `../../../assets/nova-creative-promo-poster.png` | An actual frame from the supplied film. |
| Theme-independent icon | `../../../assets/nova-brand-icon-f20c59.png` | White planet and pink orbit on a near-black #0E0B14 rounded tile; transparent outer corners. Used on both light and dark surfaces. |
| Original orbit vector | `../../../assets/nova-symbol.svg` | Original colours and vector paths from the Nova Creative website. |
| Horizontal logo | `../../../assets/nova-creative-logo.svg` | Current Nova Creative wordmark and orbit symbol. |

For an explicit request to watch the promo, attach or preview the bundled MP4 using the host's supported file mechanism. Resolve the file from the installed plugin directory. In Codex desktop, render the local video with Markdown image syntax and its resolved absolute filesystem path; this creates the video preview. Use an absolute path for the poster preview as well. If the host cannot display a bundled video, explain that limitation and provide the available file attachment or the product website rather than inventing a hosted video URL.

For product information, use https://creative.novastorm.ai/mcp/ . The MCP transport endpoint is https://app.creative.novastorm.ai/mcp and uses the host's OAuth connection flow.

## Verified originals

The bundled film is unchanged from the creator-supplied `nova-creative-promo-1080p.mp4` (SHA-256 `d7310145f2b7081c2e165f68995eda2ed32d28f4416856e89d30723338edaeaf`). Its poster is an actual film frame.

The full logo and original orbit SVG match the current landing-page files:

- https://cdn.novastorm.ai/video-generator-landing/brand/nova-creative-logo.svg
- https://cdn.novastorm.ai/video-generator-landing/brand/nova-symbol.svg

The manifest uses `assets/nova-brand-icon-f20c59.png` for `logo`, `logoDark`, `composerIcon` and `composerIconDark`. The same badge remains legible when a host uses its default icon on a dark surface. The horizontal SVG and original vectors remain unchanged.

The icon uses the original Nova brand pink `#F20C59`, background `#0E0B14`, white `#FFFFFF` and edge `#2A2F3D`.
