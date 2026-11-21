---
name: set-up-my-diet
description: Save the diets, allergies and dislikes of someone who has just started using ChefSense, then suggest a dinner that fits. Use when a user new to ChefSense says what they eat, avoid or are allergic to.
---

The user found ChefSense moments ago and knows nothing about it yet. They've told you what they eat or avoid. Save it once, then show in the same reply that it works.

1. Save their diets, allergies and dislikes with `update_diet_profile`. Anything ChefSense doesn't recognise comes back in `skipped`; tell them and suggest the closest match.
2. If they mention other people they cook for, account for those people's needs in this conversation too. Don't ask them to set anything else up now.
3. Suggest one dinner that fits. Write it yourself, and say in a line how it fits each need they mentioned.
4. Say in a sentence what ChefSense did: it now knows what they eat, and every recipe it makes for them will respect that, in any chat.
5. Offer one more thing to try now: save this dinner to their ChefSense recipe book with `save_recipe`, or tell you three things in their fridge and ChefSense will make three recipes that fit their diet.

Diet changes can be reversed with `undo_last_change`. ChefSense can't guarantee a recipe is safe for an allergy, so remind them to check labels.
