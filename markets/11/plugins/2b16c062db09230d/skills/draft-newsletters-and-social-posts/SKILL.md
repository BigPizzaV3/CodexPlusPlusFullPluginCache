---
name: draft-newsletters-and-social-posts
description: Draft newsletters and social media posts in Aveiro for a person to review and send, for example to announce a new blog post. Use when the user asks to write or revise a newsletter, an email campaign, or social posts.
---

# Draft newsletters and social posts

Aveiro never sends a newsletter or publishes a social post from here: a person approves, schedules and sends it in the Aveiro dashboard. If the user asks to send or post now, say so and offer to prepare the draft. Explicit instructions from the user take priority over these steps.

## Source material

If the draft is about the user's own content, read it first: find the page with `aveiro_list_pages` and read it with `aveiro_get_page`. Use only facts from the source or from the user. Don't invent news, numbers, dates or quotes.

## Newsletter

1. Call `aveiro_newsletter_list_campaigns` to see recent campaigns and avoid repeating one. To match an earlier campaign's tone or structure, read it with `aveiro_newsletter_get_campaign`.
2. Call `aveiro_newsletter_create_draft` with a subject, preview text and the body in `html_content`.
3. Revise it with `aveiro_newsletter_update_draft` when the user asks for changes.
4. Tell the user the draft is ready to review and send from the Aveiro dashboard.

## Social posts

1. Call `aveiro_social_list_accounts`. If no accounts are connected, ask the user to connect them in the Aveiro dashboard and stop.
2. Ask which accounts to post to, unless the user already said.
3. Write a caption that fits the strictest platform you target, or give a platform its own caption in `platform_overrides`. Put links in `first_comment` when a platform handles links in captions badly. A Reddit target needs a subreddit, and the post needs a Reddit title in `platform_titles`.
4. For images, reuse an asset from `aveiro_social_list_media` or `aveiro_social_list_org_media`, or register a public image or video URL with `aveiro_social_register_media`. `aveiro_social_generate_media` and `aveiro_video_create_mockup` use AI credits: ask before calling them, and for `aveiro_video_create_mockup` pass `estimate_only` true first and share the cost.
5. Call `aveiro_social_create_draft` with the targets and media. Use `submit_for_review` false while the user is still editing. Revise with `aveiro_social_update_draft`.
6. Tell the user a person approves and schedules the post in the Aveiro dashboard.
