# DIGG.IA: Assistente de Contratos Públicos

**Versão do pacote:** 0.7.1  
**Método técnico preservado:** MAE v3.1.0 (conteúdo histórico de janeiro/2026)  
**Nome de exibição no portal:** DIGG.IA: Contratos Públicos  
**Identificador:** `diggia-assistente-contratos-publicos`  
**Categoria:** Business & Operations

## Escopo
Apoio técnico à análise de contratos públicos, termos aditivos e editais com Lei 14.133/2021, citações documentais, auditoria formal, matriz de riscos e propostas de ajuste. Não substitui revisão humana nem é parecer vinculante. Fontes do TCU incluídas têm data própria e não constituem consulta em tempo real.

## Links fornecidos
| Campo | URL |
| --- | --- |
| Website | https://www.digg.ia.br |
| Suporte | https://www.digg.ia.br |
| Política de privacidade | https://digg.ia.br/privacy.html |
| Termos de serviço | https://digg.ia.br/terms.html |

**Ressalvas:** o suporte aponta à homepage; as políticas publicadas descrevem principalmente o catálogo de links DIGGIA e sua cobertura para o plugin precisa ser conferida antes da publicação.

## Estrutura
- `plugin.json`: configuração portátil e metadados.
- `skills/instructions/SKILL.md`: instruções operacionais e limites.
- `skills/instructions/agents/openai.yaml`: apresentação da skill.
- `skills/instructions/lookup/knowledge-index.json`: índice de referências.
- `skills/instructions/references/`: PDFs, YAML, JSONL, textos, HTML e engine Python.

## Notas de atualização
- Identidade pública corrigida, com abreviação apenas em campos limitados a 30 caracteres.
- Links institucionais, categoria e exemplos inseridos no manifesto.
- Recursos jurídicos e PDFs preservados sem alteração; nenhuma consulta em tempo real é alegada.
- Scanner SSTI corrigido para reconhecer marcadores literais benignos `{{campo}}`, mantendo detecção de expressões não permitidas; teste heurístico não equivale a auditoria de segurança completa.
- Correção de declaração de validação W3C/WCAG não demonstrada.

## Implantação
Enviar este ZIP na OpenAI Platform em Plugins. Escolher a identidade verificada e observar os Findings. Este arquivo não foi instalado nem publicado automaticamente. Atualizações de um plugin já existente devem preservar a identidade original registrada pela plataforma; o novo identificador é apropriado apenas para criação de plugin independente.

## Atualização 0.7.0 — LGE 2.10.2

Foi incorporada uma **segunda skill portátil**, `skills/loop-graph-engineering/SKILL.md`, com o YAML de origem integral e inalterado em `skills/loop-graph-engineering/references/skill_LGE_v2_10_2.yaml`. A skill governa a **arquitetura dos fluxos** de contratos públicos quando houver dependências, estados, ciclos de validação, decisões condicionais ou ações sujeitas a gate humano; não substitui o MAE jurídico nem é obrigatória para análises contratuais pontuais.

**Roteamento:** a skill principal `instructions` continua sendo a entrada para análise jurídico-contratual. Quando a demanda envolver arquitetura de fluxo de trabalho, deve consultar a LGE; em tarefas simples, não construir grafos.

**Rastreabilidade:** a versão 0.6.2 é a base; os PDFs, JSONL, YAMLs originais, motor Python, HTML, ícone e links são preservados integralmente. Os testes incluídos no YAML da LGE são especificações de teste e não constituem resultados de execução.

**Dependências:** Ask User Question é dependência opcional conforme a necessidade da LGE e não foi adicionada ao pacote; o fallback documentado é solicitar diretamente o mínimo esclarecimento bloqueante.

**Validação:** somente a validação estática e os testes locais indicados no relatório foram realizados; importação, testes comportamentais e aprovação pública pela OpenAI Platform continuam pendentes.


## Atualização 0.7.1 — prompt inicial personalizado

A alteração feita pelo responsável no `plugin.json` foi preservada **sem qualquer mudança de texto**:

> 🚦 Ponto de Partida: Apresente sua questão ou descreva sua demanda para começarmos. 🚀

O campo `extensions.com.openai.interface.defaultPrompt` mantém exatamente o tipo **array de uma string** existente no arquivo anexado. A apresentação da skill principal em `skills/instructions/agents/openai.yaml` foi sincronizada com esse mesmo texto, para evitar mensagem inicial divergente.

A release é um **patch de metadados** sobre a versão 0.7.0. O método MAE, a skill LGE 2.10.2, o conteúdo de `references/`, o ícone e a identidade técnica foram preservados. Os testes locais não constituem validação comportamental nem aprovação da OpenAI Platform.
