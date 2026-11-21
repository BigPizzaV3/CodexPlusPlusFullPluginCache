---
name: smart-content
description: Create interactive Smart Content (quizzes, flashcards, slides, games) and save it to the EduChat Library. Use when the user wants lessons, exercises or games for a class.
---

# Create Smart Content

1. Call `smart_content_guide` for the rules and `list_smart_templates` for available templates.
2. If a template fits, use `create_smart_content_from_template`. Otherwise use `create_smart_content_html` (single-file HTML, no network calls or external resources).
3. Organize with `create_library_folder`, `rename_library_item`, `move_library_items`; find items with `browse_library` and `get_library_item`.
4. After creating, give the user the `viewUrl` (preview) and `libraryUrl` as clickable links. There is no delete or publish-to-Hub tool; point users to the app for that.
5. To assign to a class, use `create_task` with `libraryItemIds`, following the confirmation rule in the teacher-assistant skill.
