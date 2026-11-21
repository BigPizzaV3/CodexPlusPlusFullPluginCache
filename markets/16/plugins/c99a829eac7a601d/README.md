# DIGG.IA: Assistente de revisão de textos oficiais

Versão **0.12.2**. Plugin skills-only para apoiar revisão de textos oficiais, com ênfase no MPGO.

- **Identificador técnico:** `diggia-assistente-revisao-textos-oficiais`
- **Nome de exibição:** `DIGG.IA: Revisão de Textos` (limite de 30 caracteres do portal).
- **Skill:** `skills/instructions/SKILL.md`
- **Referências:** quatro manuais PDF preservados do ZIP de origem.
- **Categoria:** Communication.
- **Não há servidor MCP configurado.** Pesquisa externa ou integração institucional não são capacidades garantidas deste pacote.

Este ZIP contém `plugin.json`, `skills/` e `assets/` diretamente em sua raiz e pode ser apresentado ao fluxo de upload de plugins da OpenAI Platform. A aceitação e a avaliação editorial dependem do portal.

## Avisos de publicação

- A política de privacidade e os termos atualmente fornecidos em `digg.ia.br` descrevem principalmente o catálogo de links DIGGIA; verificar sua cobertura específica para este plugin antes da revisão pública.
- O link de suporte aponta para a página inicial, não para atendimento dedicado.
- Confirmar a legitimidade de redistribuição dos PDFs de referência.
- Alteração do identificador técnico em relação ao antigo `gpt-...`: se o objetivo for atualizar um plugin já instalado com o identificador antigo, verificar antes a restrição de correspondência de nome do portal.


## Atualização 0.13.0 — LGE 2.10.2

Adicionada a skill complementar `skills/lge-v2-10-2/SKILL.md`, com a especificação original preservada em `skills/lge-v2-10-2/references/skill_LGE_v2_10_2.yaml`.

**Acionamento seletivo:** a skill principal `skills/instructions/SKILL.md` mantém a revisão e padronização de textos oficiais. A LGE só se aplica a solicitações de desenho/auditoria de workflow, validação em múltiplas etapas ou coordenação operacional materialmente complexa. Revisão textual simples não exige LGE. A especificação LGE 2.10.2 está classificada como candidata à implementação e não tem certificação comportamental, de runtime ou humana neste pacote.

**Compatibilidade:** manifestos na raiz, identidade técnica preservada, sem MCP novo, sem alteração dos PDFs, índice de conhecimento ou ícone.
