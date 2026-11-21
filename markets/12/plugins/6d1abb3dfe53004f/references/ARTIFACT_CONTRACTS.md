# Контракты артефактов и переходы между 24 модулями

Каждый результат обязан иметь `artifact_type`, `project_id` (локальный/пользовательский псевдоним, не реальный ID аккаунта), `created_at`, `source_refs`, `assumptions`, `status: draft|needs_review|approved`, `next_review`, `author_approved_at|null`. Не придумывать дату одобрения.

## Стратегическая цепочка
`setup/brand-audit → audience-and-positioning → brand-strategy → brand-story → topic-architecture → channel-design → cadence-and-capacity`.

Выходы: BRIEF (факты и неизвестные); AUDIT (наблюдения отдельно от гипотез); STRATEGY (желаемые ассоциации и запреты); EVIDENCE REGISTER (факт, участники, роль, ссылка, согласие); CONTENT ARCHITECTURE (темы и связи с задачами аудитории); CHANNEL PLAN; CAPACITY PLAN.

## Производственная цепочка
`community-listening / material → waterfall-repurposing → storytelling / content-production / video-shoot-playbook → quality gates → user review → publication performed elsewhere → analytics-review → content-experiments / portfolio-review`.

Выходы: SOURCE MAP (фактическая привязка к исходнику); CONTENT PACKAGE (площадка, текст/скрипт, редакционные метки, монтажные кадры/времена только из исходника, CTA, факты, блокеры); EXPERIMENT (предварительно зарегистрированная гипотеза); PERFORMANCE REPORT (метрики, данные и ограничения); PROPOSAL (следующий тест).

## Командная цепочка
`team-diagnostics → hiring-process / onboarding-team → leadership-and-operations / platform-scaling`. Вакансия 4R и scorecard с ролью; план адаптации 30/60/90, 1:1, maker/manager. Пользователь сам подтверждает действия в системах персонала и сроки.

## Монетизация
`monetization-model → offer-content-bridge → channel-design / content-production → analytics-review`. Модели дохода не должны выдаваться за гарантии, лестница продуктов необязательна. Утверждения об эффективности только по данным.

## Контроль перехода
`draft` → `approved` только по явной команде пользователя. Если не подтверждено, сохранять как предложение. Нет общей памяти между разговорами; перенос через `project-context-export` и пользовательские файлы.
