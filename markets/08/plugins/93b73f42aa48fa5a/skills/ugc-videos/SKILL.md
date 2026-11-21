---
name: ugc-videos
description: Generate UGC product videos through UGCBuilder from a product image, scene direction, and dialogue.
---

Use current UGCBuilder MCP schemas and OAuth connection flow. Preserve supplied product references, script, dialect, character requirements, and duration. When drafting dialogue, use the requested language and only supported product claims.

Call generate_ugc_video with the product attachment or public HTTPS image URL, full script, requested duration, and appropriate scene/character direction. Use high quality; do not substitute Standard or Grok. Pass the full requested dialogue and desiredDurationSeconds. Requests above 7 seconds use extensions, with the full cost shown in the card. Use the current tool's supported duration limits and pricing. The interactive card collects portrait/landscape selection and approval for the full total. It starts generation after approval; do not call again to start or duplicate the job.

Reuse request keys for retries with identical inputs. Use the returned request ID with get_landing_page_request to check status when needed. Share returned downloadMarkdown promptly. Never claim generation completed while approval is pending, and never spend additional credits merely to retrieve downloads.
