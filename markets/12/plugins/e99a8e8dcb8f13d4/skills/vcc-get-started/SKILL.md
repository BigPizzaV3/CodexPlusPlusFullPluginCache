---
name: vcc-get-started
description: Help people set up Vibe Coding Control after installation or when they ask what VCC does, how to start, connect an account or computer, or add a first project. Also handles «Что делает VCC?», «Как начать?» and «Как подключить компьютер?» when asked about VCC.
---

# Get started with VCC

Use this skill during plugin setup or for an explicit VCC help question. Answer in the user's language. Lead with the next action, offer the full guide link, and keep routine project requests in `vcc-workflow`. Setup is read-only. Never create a task, start work, change permissions, or ask for passwords, tokens or pairing codes in chat.

## English

Vibe Coding Control shows your AI development tasks, progress and decisions. The plugin connects this chat to your VCC account. The website shows your projects and their history. VCC Connector is the program that links project folders on your computer.

1. [Open VCC](https://vibecodingcontrol.com/app) and sign in or register. When this client asks to connect VCC, authorize the same account.
2. If you already have a VCC project, ask **“Show my VCC projects”** and choose it. You can read it without installing Connector.
3. For your first project folder, open [Connector and computers](https://vibecodingcontrol.com/connect) on that computer. Install Connector for your OS, or open it if it's already installed. Confirm the connection in the browser. Under [Projects](https://vibecodingcontrol.com/projects), choose **Connect an existing project** or **Create a new project**. If you already see projects, select **Add project** first. For an existing working folder, check the folder and name, choose **LOCAL**, then select **Connect project**.
4. Ask **“What is happening in my VCC project?”** Open the same project under **Projects** on the website to see tasks, history and any decisions waiting for you.

[Full guide](https://vibecodingcontrol.com/how-it-works#first-project) · [Instructions for each AI client](https://vibecodingcontrol.com/integrations#choose-your-client)

[Manage chat access to VCC](https://vibecodingcontrol.com/mcp/connections).

## Русский

Vibe Coding Control показывает задачи, ход разработки с ИИ и решения по проекту. Плагин подключает этот чат к аккаунту VCC. На сайте видны проекты и их история. VCC Connector подключает папки проектов на компьютере.

1. [Откройте VCC](https://vibecodingcontrol.com/app) и войдите или зарегистрируйтесь. Когда клиент предложит подключить VCC, разрешите доступ к тому же аккаунту.
2. Если проект уже есть в VCC, попросите **«Покажи мои проекты VCC»** и выберите его. Для просмотра устанавливать Connector не нужно.
3. Для первой папки проекта откройте [Connector и компьютеры](https://vibecodingcontrol.com/connect) на этом компьютере. Установите Connector для вашей ОС или откройте его, если он уже установлен. Подтвердите подключение в браузере. В разделе [Проекты](https://vibecodingcontrol.com/projects) выберите **«Подключить существующий проект»** или **«Создать новый проект»**. Если список уже содержит проекты, сначала нажмите **«Добавить проект»**. Для существующей рабочей папки проверьте её и название, выберите **LOCAL** и нажмите **«Подключить проект»**.
4. Спросите **«Что сейчас происходит в моём проекте VCC?»** Откройте тот же проект в разделе **«Проекты»** на сайте, чтобы увидеть задачи, историю и решения, которые ждут вас.

[Подробная инструкция](https://vibecodingcontrol.com/ru/how-it-works#first-project) · [Инструкции по ИИ-клиентам](https://vibecodingcontrol.com/ru/integrations#choose-your-client)

[Управлять доступом чатов к VCC](https://vibecodingcontrol.com/mcp/connections).

## Pick the next step

- General help can be answered without tools. If the user wants to see their projects or check that the chat is connected, use the remote `vcc_projects` read tool when available. On a project status request, read the selected project's `vcc_context` with its explicit ID. If there are several projects and the user hasn't chosen one, ask them which one.
- If the tool is unavailable or returns an authorization error, explain how to enable or reconnect VCC in this client and sign in to the same account. An unavailable tool cannot confirm whether authorization succeeded.
- If the project list is empty, direct the user to **Projects** to check the account and add a project. An empty list says nothing about the computer or Connector.
- For local work, direct the user to **Connector and computers** to check whether the relevant computer is connected and online. If it's offline, start Connector on that computer and finish account confirmation if needed. Remote VCC cannot determine the computer's status from the project list.
- ChatGPT and Claude use an account connection. Codex and Claude Code can also work locally through Connector. For local work, open the linked folder in that tool and use its Connector integration. If the tool is already connected, skip setup. Use the client guide for the exact route.
