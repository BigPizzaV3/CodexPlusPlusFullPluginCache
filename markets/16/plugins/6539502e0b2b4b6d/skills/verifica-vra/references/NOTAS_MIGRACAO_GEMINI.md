# Migração da saída Verifica VRA para Google Docs — v2.2.0

## Decisão de compatibilidade

A saída final da skill é um relatório editável em Google Docs, não PDF ou DOCX.
Trata-se de alteração MAJOR do contrato de saída anterior 1.1.0.
Os arquivos de entrada dos autos e da VRA podem continuar sendo PDF, ODT, DOCX ou outras formas legíveis.

## Rotas compatíveis

1. **Direta, somente quando comprovada:** integração com capacidade autorizada de criar e ler Google Docs. Exigir resultado de criação, link real e inspeção de conteúdo. Não inferir autorização a partir da existência da Skill.
2. **Padrão Gemini Apps:** emitir UMA resposta exclusivamente com o relatório integral conforme `assets/modelo_relatorio_vra_google_docs.md`. O usuário aciona **Compartilhar e exportar → Exportar para: Documentos Google** na resposta. O Gemini informa que essa ação cria um novo documento no Drive. Antes desse clique, o documento NÃO foi criado pela Skill.
3. Se nenhuma rota estiver disponível, entregar relatório textual com limitação explícita, sem alegar exportação nem apresentar URL inventada.

## Justificativa do modelo Markdown

Títulos e blocos individuais por item preservam identidade, localizador e prova melhor que tabelas largas, cujo formato pode mudar durante a exportação para Docs. A matriz permanece integral, itemizada e editável. `JSON` é apenas registro interno; HTML/CSS/PDF não são rotas de saída.

## Proteções

- Corte histórico na conclusão da VRA (opção A).
- Conferir 100% dos itens reais; nenhuma fonte posterior ao corte.
- Aprovação somente sem lacuna material e com referências corretas.
- Insuficiência de prova não equivale a irregularidade comprovada.
- `DOCUMENTO_CRIADO_E_VERIFICADO` difere de `PRONTO_PARA_EXPORTACAO`.
- Não usar scripts para requisições externas; Skills Gemini Apps não permitem scripts com acesso a sites externos.
- Conferência assistida não homologa atos administrativos.

## Referências oficiais consultadas em 27/10/2026

- Exportar respostas para Docs: https://support.google.com/gemini/answer/14184041?hl=pt-BR
- Criar e gerenciar Skills: https://support.google.com/gemini/answer/17094296?hl=pt-BR
- Tarefas Gemini: https://support.google.com/gemini/answer/17094507

## Validação

Testes locais de JSON/Markdown e análise estática do ZIP não significam que o Gemini realizou exportação de um documento Google Docs editável. Para aceitação operacional, executar um caso real e conferir, no Google Docs criado, a presença de todos os itens e da cadeia de evidências.

## Mudança v2.1.0: auditar VRA já preenchida

Objeto auditado = VRA original já preenchida; fonte da prova = autos históricos elegíveis; saída = relatório de auditoria, NÃO outra VRA. Cada item inclui localizador na VRA e resposta ORIGINAL. A recomendação de ajuste pertence a achado proposto para revisão humana. Não há preenchimento, assinatura ou protocolo de VRA pelo Gemini.

## v2.2.0 — Incidente de falsa ausência em autos extensos

Regressão obrigatória: autos 202600512653 (441 páginas); VRA 2026010338274 (mov. 20), última assinatura 17/09/2026 10h15. O movimento 4 contém 277 páginas e **inclui** as declarações e certidões de Emerson (páginas 340-351); movimentos 9, 15, 16 e 17 também precedem o corte. Documento do mov. 14 é certidão positiva com efeitos de negativa. O impacto do mov. 9 é R$ 1.710,00, remuneratório TR R$ 1.425,00. Não alegar ausência dessas peças e não concluir pendências financeiras apenas com leitura do TR. O diploma formal de DOUTOR EM DIREITO de Emerson está no mov. 4, páginas 298 e 299, inclusive registro no verso. São páginas digitalizadas em imagem, praticamente sem texto extraível: comprovação da necessidade de inspeção visual. Mov. 21 e posteriores são excluídos. Este registro de regressão **não equivale a auditoria integral homologada** dos 42 itens.

## Revisão v2.2.0 — Falha material de FORMATO no Gemini

A resposta observada ao caso 202600512653 apresentou apenas síntese narrativa dos Quadros I, II, III, IV e VI. **Rejeitada pelo formato:** não seguiu o relatório de nove seções, não entregou matriz individual de 42 itens, não preservou por item a resposta ORIGINAL e localizador VRA, nem rastreabilidade completa, não permitiu conferir as duas classificações, e não houve confirmação de documento editável criado no Google Docs.

O gate FMT-01 exige **relatório iniciado pelo título institucional, seções 1–5, 7–9 na ordem e seção 6 quando pertinente, um bloco por item e todas as provas**. Não autoriza resposta resumida como produto final. O Gemini Apps padrão exporta a RESPOSTA final para Google Docs por ação nativa do usuário; essa ação não pode ser declarada executada pela skill. Só declarar documento criado com integração autorizada + retorno real + inspeção.

**Regressão de conteúdo:** foi constatado diploma formal de Emerson no mov. 4, páginas 298–299 (imagem); a resposta incorretamente alegou que somente o currículo Lattes demonstrava sua titulação.

**Erro adicional de transcrição do formulário original:** o item I(k) da VRA de referência foi assinalado "Não se aplica" (página 2 da VRA); II(f) e III(f)/III(g) também apresentam N.A. Portanto, afirmações resumidas de que os quadros estão inteiramente marcados "Sim" são incompatíveis com a VRA original.


## Pós-v2.2.0: violação observada e estratégia v2.3.0

No teste do usuário, o Gemini afirmou equivocadamente que o PDF de 441 páginas terminava na página 216, não detectou diploma visual na página 298, nem declarações e certidões nas páginas 340–351, nem peças dos movimentos 9, 15 e 16. Também não entregou a matriz de 42 itens. Repetição apesar da v2.2.0 demonstra que o comportamento do modelo **não está validado**.

O gate P0 agora bloqueia por completo conclusão substantiva quando leitura integral e inspeção de provas materiais não estão demonstradas. O gate P1 exige o modelo integral. Ambos são contratos de comportamento e não atestados de controle determinístico sobre Gemini Apps. Para PDF idêntico, usar apenas como roteiro de falsificação o fixture `tests/regressao_202600512653.json`, nunca como substituto de cotejo de fontes.
