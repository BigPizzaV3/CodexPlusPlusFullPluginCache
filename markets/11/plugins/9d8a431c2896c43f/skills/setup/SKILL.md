---
name: setup
description: "Подключить и настроить Language Trainer по английскому, выбрать опубликованную программу, изменить свой профиль или управление подключениями."
---

Этот плагин обучает только английскому. Сервер закрепляет язык за подключением; не передавай параметр смены языка. Для другого языка укажи Language Trainer SRB, сохранив текущий курс. Следуй языку объяснений, письменности, уровню и специальным правилам выбранной программы.

Use only the connected fixed-language account. Read [content-use rules](../../references/content-use.md) and [protocol 2](../../references/protocol.md) and [tool recovery](../../references/tool-execution.md). For profile/program changes read [profile instructions](references/manage-learning-profile.md); for app access read [connection instructions](references/manage-connections.md).

1. For onboarding or missing program, read get_learning_context(task=setup) and get_program_options. Read the profile and live published choices; this administrative read does not require a teaching-session/report preflight. A returning learner with a selected program goes directly to conduct-lesson/open_lesson.
2. Ask only for missing display name, self-assessed level, goal/role and IANA timezone. Do not copy another learner's B1/Java profile. Self-assessment is not a verified CEFR exam.
3. Apply only explicitly requested profile fields with update_learning_profile and the current course revision. Offer only actually published programs from this language's catalog; never invent available levels/tracks. Use select_learning_program only after the learner chooses. An active main must be preserved or explicitly paused for a requested switch, never completed to unblock setup.
4. Explain briefly: say “Давай следующий урок” in an ordinary chat or ask for a separate Live. A Project is optional. The website provides theory and complete vocabulary practice. No external storage account, coordinator chat, copied JSON or handoff prompts are needed.
5. If authentication/consent is missing, use the actual returned connection URL and normal OAuth flow. Never ask for secrets, passwords, TOTP/email/recovery codes or tokens in chat. The learner completes MFA on the official site. Existing profile/history must survive reconnection; do not create another account to bypass a problem.

Learning scopes and account-management scopes remain separate. Missing permission is not authority to use administrative credentials, another endpoint or another account. Do not disable MFA or fabricate successful connection. This package archive is not itself proof of installation or public approval.
