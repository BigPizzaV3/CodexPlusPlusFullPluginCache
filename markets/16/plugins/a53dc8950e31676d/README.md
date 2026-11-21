# DIGG.IA: Assistente de gestão de rotinas

**Versão do pacote:** 0.12.1  
**Nome resumido de catálogo:** DIGG.IA: Gestão de Rotinas  
**Identificador técnico:** `diggia-assistente-gestao-de-rotinas`  
**Especialidade:** mapeamento, gestão e melhoria de rotinas e processos administrativos do MPGO.

## Estrutura
- `plugin.json`: manifesto Agent Plugins 1.0 e metadados de catálogo.
- `assets/gpt-icon.png`: identidade visual original (preservada).
- `skills/instructions/SKILL.md`: instruções de execução, documentação em nove blocos e cuidados com evidência.
- `skills/instructions/agents/openai.yaml`: interface associada à skill.
- `skills/instructions/lookup/knowledge-index.json`: índice dos recursos anexos.
- `skills/instructions/references/`: base normativa, modelos, documentos, scripts e LGE v2.7.1 legada preservados byte a byte.
- `skills/loop-graph-engineering/SKILL.md`: nova skill operacional LGE 2.10.2, independente e descoberta pela plataforma.
- `skills/loop-graph-engineering/references/skill_LGE_v2_10_2.yaml`: especificação 2.10.2 integral e idêntica ao arquivo fornecido.

## Atualização 0.12.0 — integração da LGE 2.10.2

A LGE 2.10.2 passa a ser a referência **operacional vigente**, por uma skill independente. Antes de cada demanda é verificada sua aplicabilidade; o acionamento efetivo ocorre somente para fluxos, dependências, estados, validações, ciclos ou orquestração que justifiquem Value Add. Demandas simples permanecem atendidas diretamente. A LGE não cria novos agentes, conexões a sistemas, autoridade decisória ou homologação institucional. Seu arquivo YAML foi copiado sem qualquer alteração e permanece com estado `implementation_candidate`.

A especificação 2.7.1 não foi removida para manter a origem auditável, mas não é mais a fonte operacional. O índice de conhecimento aponta também para a nova skill. Recursos MPGO, regimento, `engine.py`, HTML, ícone e endereços institucionais foram mantidos.

## Funcionamento e limites
O plugin é **skills-only** e não configura servidor MCP. O arquivo `engine.py` é um recurso de referência; sua presença não significa execução automática pela OpenAI Platform. O HTML é um modelo que requer aplicação e validação antes de uso operacional.

O Regimento Interno e as citações normativas necessitam verificação de vigência e de pertinência ao caso concreto. Não se deve afirmar que um fluxograma foi validado no Mermaid Live sem teste efetivo. Não presumir prazos normativos.

## Proveniência e atualização
Este pacote deriva do arquivo fornecido `plugin (4).zip`. A versão anterior declarada era `0.11.1+bundle.b819382c9debb255f38d81e56151c0fd` e o antigo nome técnico era `gpt-4732ba19d0401801d1d63600d69a53ad`. O identificador técnico foi normalizado para o nome do novo pacote; **para atualizar uma instalação existente, confirme que esse identificador corresponde à identidade registrada no Portal**. Os recursos técnicos da pasta `references` e o ícone não foram modificados.

## Links institucionais fornecidos

| Finalidade | Campo de configuração | Endereço |
|---|---|---|
| Site institucional | `websiteURL` | [DIGG.IA](https://www.digg.ia.br) |
| Suporte | `supportURL` | [Site DIGG.IA](https://www.digg.ia.br) |
| Política de privacidade | `privacyPolicyURL` | [Política de Privacidade – DIGGIA](https://digg.ia.br/privacy.html) |
| Termos de serviço | `termsOfServiceURL` | [Termos de Uso – DIGGIA](https://digg.ia.br/terms.html) |

Fonte dos endereços: `website(7).txt`, fornecido pelo usuário. Os quatro campos já estavam preenchidos na versão 0.11.2 e **foram mantidos sem mudança** nesta versão.

## Preparação para publicação

Os endereços foram verificados em consulta pública em 29/10/2026, mas isso não constitui aprovação da OpenAI Platform nem comprova suficiência jurídica. O URL de suporte aponta para a página inicial e deve ter um canal de atendimento claramente identificável. A política de privacidade e os termos de uso descrevem principalmente o **catálogo** DIGGIA; o responsável deve confirmar a aplicabilidade específica ao plugin e atualizar as páginas quando necessário.

Esses endereços não constituem fonte normativa do MPGO e não substituem a verificação de vigência de atos institucionais. A consulta e a disponibilidade das páginas podem mudar.

Pacote 0.12.0 validado estaticamente; **não equivale a importação, execução de testes comportamentais, homologação institucional ou aprovação pela OpenAI Platform**.


## Atualização 0.12.1 — prompt inicial personalizado

Esta versão preserva, **sem modificações**, o campo `extensions.com.openai.interface.defaultPrompt` fornecido pelo responsável, no formato original **array com uma string**:

> 🚦 Ponto de Partida: Apresente sua questão ou descreva sua demanda para começarmos. 🚀

O mesmo texto foi sincronizado com `skills/instructions/agents/openai.yaml` (`interface.default_prompt`), cujo contrato exige uma string; `review.prompts` já reproduzia o texto informado e permaneceu intacto. A versão do manifesto e as referências à versão corrente da documentação foram atualizadas.

Esta é uma atualização de patch, **sem mudança funcional** na skill principal ou na LGE 2.10.2. Não foram alterados os arquivos normativos, a base de conhecimento, o `engine.py`, o modelo HTML, o ícone ou os endereços institucionais. A versão 0.12.0 permanece registrada acima como marco histórico de integração da LGE.

**Limitações:** apenas inspeção e validação estática local; a importação na OpenAI Platform, o comportamento em runtime, a validação das fontes normativas e a homologação institucional permanecem não verificados.
