# Piloto e publicação do plug-in

## Escopo da primeira versão

- Plug-in somente de habilidades.
- Trinta habilidades incluídas: 29 do método e `ga2-me-mostra`.
- Nenhum MCP, App, Action, conector ou autenticação externa.
- O repositório continua sendo a fonte única do conteúdo.

## Piloto controlado

1. Validar o pacote com `scripts/validar.py` e o validador oficial de estrutura.
2. Gerar o arquivo de distribuição com `scripts/empacotar_plugin.py`.
3. Instalar em um ambiente de teste e iniciar uma conversa nova.
4. Executar os dez casos de `tests/plugin-submission-cases.json`.
5. Repetir cada falha após ajustar somente a habilidade responsável.
6. Testar a jornada A3 → OKR → Backlog 2D → Kanban → ciclo → review → melhoria.
7. Fazer um piloto com alunos usando dados fictícios ou anonimizados.

## Metadados preparados

- Nome: Gestão Ágil 2.0
- Desenvolvedor: MindMaster
- Categoria: Productivity
- Site: https://mindmaster.com.br/
- Suporte: https://github.com/Mindmaster-code/gestao-agil-skills/issues
- Privacidade: https://github.com/Mindmaster-code/gestao-agil-skills/blob/main/PRIVACY.md
- Termos: https://github.com/Mindmaster-code/gestao-agil-skills/blob/main/TERMS.md
- Logo: `assets/gestao-agil-2.png`

## Publicação pública

A submissão pública deve ocorrer somente depois do piloto. Ela exige identidade de
desenvolvedor ou empresa verificada, materiais públicos válidos, cinco testes
positivos, três negativos e aprovação da revisão da OpenAI.

Documentação oficial:

- https://learn.chatgpt.com/pt-BR/docs/build-plugins
- https://developers.openai.com/plugins/deploy/submission

O envio para revisão e a publicação são ações separadas. Não publique automaticamente
ao terminar os testes.
