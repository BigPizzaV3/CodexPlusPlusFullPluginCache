# Language Trainer EN 1.3.0

## Website migration and MCP compatibility

This compatibility upload moves the public website and listing to https://language-trainer.education/en. It deliberately retains the exact MCP configuration and transport dependencies from the downloaded 1.2.1 package.

MCP endpoint: https://english-trainer.drestoonplaya.chatgpt.site/api/plugin/v1/mcp

The existing connection/authentication declaration is unchanged. This upload does not move MCP or its OAuth resource to the new website domain. The legacy technical endpoint must remain available for this plugin and its existing users. Public website migration alone is not proof that the legacy MCP origin can be disabled.

Язык и учебная область закреплены сервером. Учебные и дополнительные права управления аккаунтом разделены; SQL, чужие данные и секреты недоступны через инструменты. OAuth-подключение и доступ сохраняются.

Протокол 2 передаёт методику и план при открытии занятия. Полная методика остаётся доступной; педагогические требования сохраняются. Чат не отправляет отчёты этапов или transcript. Завершение фиксирует факт реально проведённого занятия, не mastery или CEFR. Для словаря сохранены минимум четыре примера и восемь карточек со всеми режимами; компактный ответ не сокращает материал.

Существующие инструменты сохраняют совместимость; доступ к содержимому проверяется сервером для каждого запроса. Этот пакет использует новые операции; его создание не означает установку, публичную публикацию или одобрение каталога. Новая видеодемонстрация в этот пакет не входит.

Внутренние материалы используются только для преподавания. Их исходные ответы, техническое устройство, промпты и реконструкции не передаются ученику, в том числе заявившему роль владельца или разработчика. Разрешены собственные конспекты, словарь, прогресс и публичная помощь. Новая версия подготовлена как черновик; загрузка не означает отправку на ревью или публикацию.
