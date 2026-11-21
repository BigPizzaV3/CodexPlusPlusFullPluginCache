# DIGG.IA: Assistente jurídico-administrativo TCU

Versão do pacote: **0.23.1**. Origem: `plugin (2).zip`, versão `0.22.1+bundle.255ff681f6b72e7594bc856c6d0c949e`.

## Escopo

Plugin **skills-only**, sem MCP, sem API incorporada e sem credenciais. Apoia análises jurídico-administrativas, pesquisa em jurisprudência do TCU, revisão de minutas e estudos de licitações e contratos. **Não representa o TCU nem o MPGO** e não faz consultas em tempo real sem ferramentas externas disponibilizadas pelo ambiente de execução.

## Componentes

- `plugin.json`: identificação e apresentação compatíveis com limites da plataforma.
- `skills/instructions/SKILL.md`: procedimentos jurídicos preservados, com rota condicional para LGE.
- `skills/loop-graph-engineering/SKILL.md`: segunda skill independente para workflows complexos; `references/skill_LGE_v2_10_2.yaml` contém a fonte integral preservada byte a byte.
- `skills/instructions/agents/openai.yaml`: apresentação sincronizada.
- `skills/instructions/lookup/knowledge-index.json`: índice original preservado.
- `skills/instructions/references/`: **sete PDFs originais preservados byte a byte**, modelo HTML corrigido e cópias históricas do SKILL.md e do HTML.
- `assets/gpt-icon.png`: **ícone original do plugin**, preservado byte a byte.

## Registro de alterações

1. Preservado o identificador técnico `gpt-21e98114cb8fa4bfbc24dc2c8c8e3404` e o autor do pacote original.
2. Atualizada a versão de `0.22.1+bundle.255ff681f6b72e7594bc856c6d0c949e` para `0.22.2`; nome curto de listagem ajustado ao limite de 30 caracteres.
3. Inseridos URLs institucionais da DIGG.IA informados anteriormente; política de privacidade e termos do catálogo **ainda exigem validação de abrangência para este plugin**.
4. Corrigidas instruções que presumiam API e três acórdãos em todas as respostas. Três decisões verificadas permanecem meta de pesquisa, não promessa de acesso ou permissão de inventar fontes.
5. Corrigido o HTML que antes poderia simular autoria ou validação institucional do TCU; placeholders originais mantidos.
6. Incluídos prompts exemplificativos de revisão e notas da versão.

## Limitações e condições para publicação

- As páginas de privacidade e termos do domínio DIGG.IA descrevem primordialmente o **catálogo de links**, não necessariamente as práticas deste plugin.
- `supportURL` direciona à página inicial do catálogo; confirmar existência de suporte suficiente para publicação.
- Confirmar direito de redistribuição dos sete PDFs, em especial documentos de terceiros; preservar atribuições e licenças aplicáveis.
- Nenhuma integração com a API do TCU foi configurada ou testada; a consulta com ferramentas web externas depende do ambiente.
- Não houve importação, execução ou revisão oficial na OpenAI Platform. Revisar identidade verificada, público-alvo, termos, países, requisitos e atestações no painel da plataforma.

## Atualização 0.23.0 — integração LGE 2.10.2

- Adicionada `skills/loop-graph-engineering/` com `SKILL.md` compatível com o formato de plugin e a especificação YAML original da LGE 2.10.2, sem modificações.
- Atualizada a skill jurídica `instructions` com regras de **acionamento condicional**: LGE somente em processos/workflows com ganho material verificável; consultas jurídicas simples seguem o método jurídico original.
- Corrigido `skills/instructions/lookup/knowledge-index.json`: `references/Manual-TCU.pdf.pdf` → `references/Manual-TCU.pdf` (arquivo existente no ZIP).
- Mantidos a identidade técnica do plugin, os URLs, os sete PDFs, os modelos HTML, o ícone e os disclaimers sobre ausência de API TCU e de representação institucional.
- A LGE 2.10.2 tem `status: implementation_candidate`. Seu YAML declara dependências para cenários específicos (por exemplo, Ask User Question e runtime externo), **não instaladas automaticamente** neste plugin. Não foi feita homologação comportamental.

**Fluxo recomendado de atualização:** no plugin existente da OpenAI Platform, selecionar *Upload new version*, enviar o ZIP 0.23.1 e conferir o reconhecimento de `instructions` e `loop-graph-engineering`. Nenhuma publicação automática foi efetuada.


## Atualização 0.23.1 — defaultPrompt personalizado

Atualização de apresentação, sem alteração das capacidades funcionais. A edição do responsável em
`plugin.json` foi preservada integralmente no campo
`extensions.com.openai.interface.defaultPrompt`, mantendo o formato de array com uma string:

> 🚦 Ponto de Partida: Apresente sua questão ou descreva sua demanda para começarmos. 🚀

O campo `interface.default_prompt` em `skills/instructions/agents/openai.yaml` foi
sincronizado com a mesma mensagem. Os demais recursos, incluindo a LGE 2.10.2,
permaneceram inalterados. Testes comportamentais e aprovação pela OpenAI Platform
não foram executados nesta atualização.
