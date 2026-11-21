---
name: lge-v2-10-2
description: "Projetar ou auditar workflows, loops, grafos, dependências e etapas de validação; aplicar apenas quando uma revisão documental exigir engenharia operacional, e não em revisão textual simples."
---

# Loop and Graph Engineering — LGE 2.10.2

Quando o usuário solicitar projeto ou auditoria de workflows de revisão textual, validação documental em múltiplas etapas, estado/versionamento, coordenação de responsáveis, grafos, loops ou recuperação operacional, avalie a ativação desta habilidade pela regra de **Value Add e primeiro nível suficiente**.

Antes de aplicar, **leia integralmente** [`references/skill_LGE_v2_10_2.yaml`](references/skill_LGE_v2_10_2.yaml) (especificação original preservada) e siga sua triagem de segurança, ativação e não ativação; seus contratos de entrada/saída e seus critérios aplicáveis. Este SKILL.md é o ponto de entrada para descoberta do plugin, não uma substituição da especificação.

## Limites e interoperabilidade

- Para apenas revisar, corrigir ou padronizar texto oficial, a LGE **não deve ser ativada**; siga `../instructions/SKILL.md`.
- Se o problema exigir desenho operacional, escolha a solução mais simples suficiente. Loop, grafo, multiagente, persistência, recuperação e validações adicionais só são elegíveis mediante ganho material e condições de segurança/autoridade adequadas.
- Preserve conteúdo jurídico, nomes, datas, valores, referências normativas e estrutura documental, sem alterar mérito ou presumir vigência de normas. O fluxo elaborado é proposta de apoio e não substitui a validação humana.
- Não declare execução de ferramenta, recuperação de estado, validação independente, aprovações institucionais nem conexões externas que não tenham evidência verificável.
- O YAML fornecido declara `status: implementation_candidate` e `production_readiness: blocked_until_behavioral_runtime_human_and_comparative_validation`. Sua incorporação ao ZIP **não transforma** essa condição em homologação.
- Falhas ou lacunas materiais devem ser sinalizadas, e ações externas de alto impacto exigem autorização prévia. Não introduzir arquitetura paralela apenas para atender formalmente à existência desta skill.
