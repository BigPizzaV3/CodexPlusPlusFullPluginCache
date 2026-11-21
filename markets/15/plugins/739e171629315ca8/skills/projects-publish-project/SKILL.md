---
name: projects-publish-project
description: Publish one PropBot project to the marketplace after confirmation. For builders and developers.
---

Use this skill for that request.

Permission: propbot.projects.write and propbot.projects.publish.

1. Show the project id and title. Ask them to confirm this project should become public. Then call projects_private_project_publish. If publish is not granted, stop.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
