# English / Русский

This source tree uses the existing `localization.json` for user-facing EN/RU
descriptions, capabilities, connection help and prompts. It is a source resource,
not an extension to the platform manifest schema. The 0.1.4 candidate includes
the bilingual `vcc-get-started` skill for setup or explicit help.

The workflow skill answers in the user's language and preserves original project
names, task text, comments, notes, evidence and owner quotations. Server MCP uses
client locale metadata (`openai/locale`, legacy `webplus/i18n`, or `locale`), then
Accept-Language; initialized session locale is retained. No metadata defaults to
English. Clients without locale metadata can still send Russian or English requests;
the workflow skill follows their language. Installed Connector MCP falls back to
the OS language. Locale changes presentation only, never rights or saved history.

Example requests:

| English | Русский |
|---|---|
| How do I get started with VCC? | Как начать работу с VCC? |
| Show my VCC projects | Покажи мои проекты VCC |
| What is happening in my VCC project? | Что сейчас происходит в моём проекте VCC? |

Connect to **https://vibecodingcontrol.com/mcp**, sign in to the existing VCC account
and review permissions. Remote VCC cannot read local files or deploy. Never share
passwords or Connector tokens in chat. Tool identifiers, arguments, enum values
and idempotency keys are the same in both languages.

## Русский

Существующий `localization.json` содержит EN/RU описания, подсказки подключения
и примеры запросов. Инструкции отвечают на языке пользователя. Сервер учитывает
язык, переданный клиентом; при его отсутствии использует EN. Клиенты без передачи
локали принимают запросы на обоих языках — инструкции выбирают язык ответа по запросу.
Локальный MCP установленного Connector использует язык ОС как резервный вариант.

Подключитесь к **https://vibecodingcontrol.com/mcp**, войдите в существующий аккаунт
и проверьте права. Не передавайте пароли и токены в чате. Перевод затрагивает только
известные системные сообщения и описания; оригинальные записи не переписываются.
Имена `vcc_*`, аргументы, enum, права, авторизация и протоколы одинаковы.

Кандидат OpenAI берёт английский текст из манифеста. Русский и английский тексты
инструкции входят в пакет. Для карточки подключения Claude подготовлены
`shortDescription`, `longDescription` и примеры в `localization.json`.
При согласованном обновлении карточки используйте доступные поля каталога и
ссылку на руководство. Подсказки самого подключения Claude поступают от Remote MCP.
