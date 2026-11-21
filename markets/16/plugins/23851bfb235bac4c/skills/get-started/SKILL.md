---
name: get-started
description: Open Animeify onboarding after installation when the user chooses setup, requests a generation form, or wants to generate without the required prompt/input.
---

Call open_animeify to show the onboarding/generation form. This is read-only and must not create a sample image on installation.

If the active user request already provides the required generation prompt/image and asks to generate, call create_animeify directly instead. Use the original defaults for unspecified settings and let the SDK show generation progress and the result. Do not make the user complete onboarding or click Generate a second time.

Use create_animeify with an actual attached photo or a user-supplied public HTTPS image URL. Choose retro, pop, lively, classic, vibrant, or soft. Keep preserve_composition enabled unless requested otherwise. Custom instructions can contain up to 150 characters.
