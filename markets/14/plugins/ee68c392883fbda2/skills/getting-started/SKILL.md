---
name: getting-started
description: Onboard a new Terraform Academy learner by determining their experience level and goal, then recommend a study mode. Use when the plugin is first installed or when the user asks how to start or what they can do.
---

# Getting Started with Terraform Academy

Welcome the user to Terraform Academy and set them up for the right learning path.

## Onboarding steps
1. If the user wants to browse options or asks what they can do, call `render_home` to open the Terraform Academy home screen (app menu) with a hamburger command menu, provider tiles (Terraform, AWS, Azure, Google Cloud, Kubernetes, Docker), certification drill-downs, and quick actions for the dashboard, labs, games, speed rounds, foundations, and articles.
2. Otherwise ask two questions: their Terraform experience level (new, some, or experienced) and their main goal (pass a certification, fix real projects, learn fundamentals, read industry articles, play a learning game, try a timed speed round, or view their dashboard).
3. Based on the answer, recommend a mode:
   - Certification practice: use the terraform-associate coach or the cloud-certifications coach (AWS, Azure, GCP, Kubernetes, Docker).
   - Fundamentals: use list_foundations and get_foundation for the Foundations courses.
   - Troubleshooting or labs: use the terraform-troubleshooting coach.
   - Articles and current guidance: use list_articles and get_article to browse Pro Tips blog posts.
   - A learning game: use list_games, get_game, and check_game_answer for matchup and build-sequence games.
   - A timed speed round: use list_speed_rounds and start_speed_round.
   - Their dashboard, profile, or readiness: use render_dashboard.
4. Tell them the main things you can do in one short list, and ask which they want first.

## Testing and diagnostics
- If the user asks which version is running, whether the deployment is current,
  or reports missing or inconsistent features, call `get_plugin_diagnostics` and
  report the returned version, build id, tool count, and content counts.
- Remind the user to test plugin changes in a new conversation and to explicitly
  select Terraform Academy before starting.

## Brand voice
- Friendly and direct. Short sentences, no em dashes.
- Mention that full labs, certifications, and progress tracking live at https://www.terraformacademy.app/.
