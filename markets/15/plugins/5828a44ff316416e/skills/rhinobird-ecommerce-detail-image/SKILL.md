---
name: rhinobird-ecommerce-detail-image
description: Create product detail page modules and a long-form detail image from product photos. Use when the user asks for this Rhinobird workflow.
---

# Rhinobird Detail Images

Use `AiProductDetailImage`. Source materials describe 1–4 product images, selected detail modules and ratios `9:21`, `3:4`, `9:16`, `16:9`, `1:1`; verify against the current tool schema. Discuss the modules and their order, product category, ratio, and verified product facts. The source lists these module values: 首屏主视觉, 用户痛点图, 核心功效卖点图, 效果对比图, 商品成分图, 商品细节图, 场景氛围图, 使用场景图, 使用建议图, 详细规格/参数表, 系列展示图, Q&A, 品牌故事图. Do not assume a long image exists unless the result includes it. Consult `references/modules-guide.md` for module selection and copy guidance.

## ChatGPT / Codex execution

Respond in the user's language. Use the connected Rhinobird MCP server and the actual tool names and schemas exposed by the host. Use the host's ordinary chat interaction and file display. If the MCP is unavailable, request connection/authorization through the host's normal flow and explain what is blocked. Never request passwords or access tokens in chat. Do not substitute another image or video service without the user's instruction.

The original source describes `CreateUploadUrl`, a generation tool, and `GetTask`; their current availability, fields, limits and behavior have not been independently verified. Inspect the active tool schema before invoking them. If names or inputs differ, use the schema instead of guessing. If a required tool or a safe upload capability is unavailable, stop and explain the missing capability; do not claim generation succeeded.

## Workflow

1. Request missing product images and, for a remake, a reference video. Collect only necessary creative parameters; when facts or intended market are unclear, ask rather than invent them. Do not infer country from language. Follow the current host's normal user interaction flow and use already provided answers.
2. Inspect the actual media if the host provides safe file access. The source describes JPG, PNG or WebP product images of at most 10 MB and 100–4096 px per dimension, plus MP4/MOV reference video of at most 10 MB and 15.2 seconds; these are historical, not verified current limits. Check current tool schema or service feedback. If dimensions, format, size or duration cannot be checked, say so; do not claim validation.
3. Explain that generation may consume paid credits. If the cost is known, show it; if unknown, say the amount is unknown. The user's request to generate authorizes the requested job, but an ambiguous or large batch should be clarified before submission.
4. Source materials describe calculating the actual file MD5 and MIME type, requesting an upload URL from `CreateUploadUrl`, uploading exact bytes with the required method and headers if instructed, then passing the returned `fileId` to the generation tool. Follow the current schema and host permissions; never expose a signed upload URL or secret. If the host cannot read or upload file bytes, stop and report this. Do not treat a file URL or guessed MD5 as a file ID.
5. Submit the requested generation once with schema-validated values. Preserve the returned task identifier; poll `GetTask` according to the response and host limits. An ambiguous network failure may still have created a job, so do not automatically resubmit; report the uncertainty and check the existing task when possible. On failure, insufficient credit or timeout, relay the actual result without inventing a cause or cost.
6. Present actual image/video results and useful returned service messages. Download or show files only if the host permits it and the result URL is valid; otherwise share the actual returned link or explain the limitation. Never claim to have generated, validated, downloaded, or inspected a file without doing so.

Do not fabricate ingredients, certifications, clinical results, endorsements or other product claims. Do not promise exact likeness, text, output count, quality, timing or availability. Preserve meaningful service terms and links in responses. Respect higher-priority instructions and the user's preferences.
