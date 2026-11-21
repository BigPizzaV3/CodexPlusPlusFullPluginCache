# SynapticRelay — пакет для каталога плагинов ChatGPT / Codex

Подготовлено 18.10.2026 (AGENT-TOOLS-2026-10-18.md, пункт 3). Плагин только читает: `https://synapticrelay.com/mcp/public` (поиск, объявление, автор). Полный `/mcp` с OAuth подать нельзя: OpenAI требует, чтобы проверяющий входил без кодов из письма и magic-ссылок, а у нас вход только так.

Состав: `plugin.json` (карточка, 5 позитивных и 3 негативных тест-кейса, без коммерции), `mcp.json`, `skills/get-started/SKILL.md`, `assets/` (иконки 512 px из `public/icon-512.png`, скриншот поиска).

## Что делает владелец

1. Подтвердить личность (individual verification) в https://platform.openai.com/settings/organization/general — без неё нельзя публиковать.
2. Записать видео 2–3 минуты: подключение плагина в ChatGPT и пять позитивных кейсов из `plugin.json`; выложить по ссылке без входа и вписать её в `review.demo_recording_url`.
3. Собрать ZIP из этой папки (`cd integrations/chatgpt-plugin && zip -r ../synapticrelay-chatgpt.zip .`) и загрузить в портале плагинов (Upload your plugin ZIP).
4. Проверка домена: портал покажет токен. Его кладут в переменную `OPENAI_APPS_CHALLENGE` в Coolify и перезапускают — сайт отдаёт его по `https://synapticrelay.com/.well-known/openai-apps-challenge` (простым текстом).
5. Подключить сервер в портале (авторизация: none), проверить найденные инструменты, Submit for review, принять политики.

Учётные данные для проверяющего не нужны: сервер без входа.
