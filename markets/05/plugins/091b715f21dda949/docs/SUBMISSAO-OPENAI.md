# Ficha de submissão — OpenAI Plugins Directory

Status: versão 0.2.0 publicada; atualização 0.2.1 preparada para envio.

## Tipo

Skills only.

## Informações públicas

- Nome: Gestão Ágil 2.0
- Desenvolvedor: MindMaster
- Categoria: Productivity
- Descrição curta: 30 habilidades para aplicar o método Gestão Ágil 2.0 a um caso real.
- Descrição longa: Aplique o método Gestão Ágil 2.0 ao contexto real da sua empresa: diagnostique problemas, conecte objetivos e iniciativas, organize o fluxo, conduza ciclos, melhore processos e desenvolva o time.
- Site: https://mindmaster.com.br/
- Suporte: https://github.com/Mindmaster-code/gestao-agil-skills/issues
- Privacidade: https://github.com/Mindmaster-code/gestao-agil-skills/blob/main/PRIVACY.md
- Termos: https://github.com/Mindmaster-code/gestao-agil-skills/blob/main/TERMS.md
- Disponibilidade inicial: Brasil

## Prompts iniciais

1. Diagnostique meu caso e monte um Relatório A3.
2. Conecte A3, OKR, Backlog 2D, Kanban e o próximo ciclo.
3. Mostre visualmente onde este fluxo trava e qual decisão tomar.

## Casos de teste

Usar os seis casos positivos e quatro negativos de
`tests/plugin-submission-cases.json`. O resultado da execução da versão final está em
`tests/RUNTIME-RESULTS.md`.

## Notas da versão

Atualização 0.2.1 do plug-in Gestão Ágil 2.0. A habilidade compartilhada Me Mostra
passa a usar o caso de gestão ativo da conversa, preserva os dados já informados e pede
esclarecimento quando não existir um caso de gestão identificável. A atualização também
impede que o nome do plug-in ou do método seja usado como assunto substituto. O pacote
continua reunindo 29 habilidades do método e a habilidade Me Mostra em seis trilhas, sem
Apps, Actions, servidor MCP, autenticação ou coleta própria de dados.

## Confirmações

- O pacote contém 30 habilidades e nenhum conector externo.
- O logo e o ícone estão em `assets/gestao-agil-2.png`.
- Política de privacidade, termos e suporte precisam estar acessíveis publicamente no
  momento da submissão.
- A identidade empresarial da organização publicadora precisa ser confirmada na
  OpenAI Platform antes do envio para revisão.
