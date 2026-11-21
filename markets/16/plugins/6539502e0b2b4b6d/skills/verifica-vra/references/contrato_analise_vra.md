# Contrato interno de auditoria da VRA já preenchida e geração do relatório

Este contrato é produzido **pela própria skill**, após auditar a VRA já preenchida contra os autos, e **não** constitui arquivo a ser preparado pelo usuário. O gerador somente materializa registros documentais; não lê autos nem valida a veracidade das evidências. Entrada interna: JSON em UTF-8 com os seguintes campos:

## Raiz (obrigatórios)

- `process_id`: número do processo administrativo.
- `vra_title`: título/versão ou movimento da VRA examinada.
- `cutoff_at`: data/hora da conclusão, preferencialmente **ISO 8601 com fuso** (`2026-10-07T12:40:00-03:00`). Se só houver data comprovada (`2026-10-07`) e **nenhuma inferência de hora for permitida**, informar `cutoff_precision: DATE_ONLY` e `date_only_resolution` com a justificação documental; evidência juntada no mesmo dia deve trazer `before_cutoff_by_institutional_order: true`, comprovada por ordenação institucional confiável. Não inventar horário.
- `cutoff_source`: origem da evidência da assinatura/conclusão, com movimento/documento e localizador.
- `decision`: exatamente `APROVACAO_DOCUMENTAL`, `NECESSIDADE_DE_CORRECOES` ou `IMPEDIMENTO_TECNICO`.
- `executive_summary`: síntese fundada no cotejo.
- `scope`: definição do âmbito documental.
- `coverage_statement`: completude dos autos e movimentos até o corte.
- `conclusion`: conclusão de competência exclusivamente documental.
- `items`: array completo dos itens da VRA, sem amostragem (um objeto por pergunta real).

## Controle de cobertura adicional (obrigatório para decisões substantivas)

- `expected_items_count`: inteiro positivo correspondente ao inventário do checklist real; exigir `len(items) == expected_items_count`. Nunca derivar contagem apenas dos itens que o modelo conseguiu analisar.

## Raiz (adicionais)

- `object`, `unit`, `vra_location`, `signatures`, `generated_at`, `files` (array), `limitations` (array), `coverage_note`, `human_review`, `skill_version`, `file_integrity`, `excluded_after_cutoff` (array), `uninspected_references` (array), `material_gaps` (array), `coverage_blocked` (boolean), `technical_block` (texto quando decisão técnica), `findings` (array), `sources` (array).

## Manifesto de corpus e prova negativa (obrigatório nas decisões substantivas)

- `source_inventory`: objeto com `total_pages`, `max_movement_number`, `movements[]` e `reviewed_page_ranges[]`. Deve retratar **o PDF integral realmente aberto**; se for apenas extrato, marcar `corpus_incomplete: true` e declarar `IMPEDIMENTO_TECNICO` quando faltar parte material. Proibir confundir data de exportação com timestamps dos movimentos.
- `source_inventory.movements[]`: cada registro contém `number`, `page_start`, `page_end`, `joined_at`, `temporal_status: ELIGIBLE|EXCLUDED_AFTER_CUTOFF`, `review_status: REVIEWED|PARTIAL|NOT_REVIEWED|EXCLUDED`, `review_note`. Listar movimentos existentes, inclusive os posteriores excluídos, sem empregá-los como prova. Para decisões substantivas não admitir lacunas de enumeração nem movimento material elegível parcialmente/não revisado.
- `absence_claims`: array de declarações explícitas de **ausência de documento**. Cada uma exige `item_id`, `document_type`, `searched_movement_ids`, `searched_page_ranges`, `search_methods`, `counterevidence_review`, `conclusion`. Na ausência de comprovação integral, não é permitido usar "não consta dos autos"; registrar apenas lacuna de leitura, e impedir decisão de falta documental.
- `search_methods` distingue busca de palavras-chave de leitura contextual do original. Busca sem retorno não demonstra, sozinha, inexistência.
- **Certidão positiva com efeitos de negativa:** registrar conteúdo e efeito jurídico; não reduzir à categoria "certidão negativa inexistente" ou "certidão positiva impeditiva" por mera nomenclatura.
- **Custo remuneratório e patronal:** verificar demonstrativos de impacto e minutas, não apenas o TR.
- **Titulação:** separar Lattes, certidão/diploma e norma que imponha forma de comprovação, sem presumir exigência exclusiva de diploma.

## Cada `items[]`

- **Sempre**: `item_id`, `vra_item_locator` (página/quadro/localizador na VRA original), `item_text` (pergunta literal), `answer_raw` (resposta ORIGINAL, inclusive vazia quando efetivamente em branco), `declared_references` (referência ORIGINAL ou `Não indicada`), `material_status`, `filling_status`, `rationale`, `evidence` (fontes examinadas nos AUTOS). Não substituir `answer_raw` pela conclusão da auditoria.
- **Quando presente**: `original_justification` contém a observação/justificativa literal do responsável; não misturar proposta da IA. A correção proposta fica apenas em `findings[].remediation`.
- `material_status` em: `CONFORME`, `NAO_CONFORME`, `EVIDENCIA_INSUFICIENTE`, `NAO_APLICAVEL`, `ANALISE_IMPOSSIBILITADA`.
- `filling_status` em: `ADEQUADO`, `RESPOSTA_INCORRETA`, `REFERENCIA_INCORRETA`, `OMISSAO_DE_PREENCHIMENTO`, `NAO_DETERMINADO`.
- Se `EVIDENCIA_INSUFICIENTE`: `evidence_gap` detalha as buscas e lacunas.
- Se `NAO_APLICAVEL`: `na_basis` descreve razão fática documental, não bastando o N.A. assinalado.
- Se `ANALISE_IMPOSSIBILITADA`: `block_reason` descreve a causa técnica.
- Para `CONFORME`, `NAO_CONFORME` ou `NAO_APLICAVEL`, o array `evidence` **não pode ser vazio**. Só classificar não conformidade por evidência positiva ou ausência comprovável em autos relevantes completos.

## Cada `items[].evidence[]`

- `movement` e/ou `document`: origem efetivamente inspecionada.
- `page` ou `locator`: página ou trecho localizável.
- `excerpt`: trecho curto quando útil; não substituir a análise pela citação isolada.
- `eligible_by_cutoff`: booleano **true somente se a anterioridade documental foi examinada e comprovada**.
- `temporal_basis`: descrição objetiva de como foi comprovado que a evidência já integrava os autos antes do marco (carimbo, movimento com timestamp, ordem institucional comprovada).
- `joined_at`: timestamp ISO com fuso, quando extraído; se posterior ao corte, a validação local bloqueará a formatação do relatório. Em corte apenas por data, registro do mesmo dia exige `before_cutoff_by_institutional_order: true` com fundamento de sequenciamento institucional descrito em `temporal_basis`.

## Cada `findings[]` (um por item afetado, mínimo)

- `id`, `item_id` existente em `items`, `issue` (distinguir irregularidade, erro e falta de prova), `evidence_text`, `criterion`, `remediation`, `priority` (`ALTA`, `MEDIA`, `BAIXA`), `priority_reason`, `review_criterion`.
- **Obrigação:** cada item cuja situação não é `CONFORME`/`NAO_APLICAVEL`, ou cujo preenchimento não é `ADEQUADO`, precisa de ao menos um `finding` em `NECESSIDADE_DE_CORRECOES`.
- `APROVACAO_DOCUMENTAL` bloqueada se houver item pendente, achado, lacuna material ou cobertura bloqueada.

## Cada `sources[]`

- `movement`, `document`, `page` ou `locator`, `function`. Somente fontes efetivamente abertas/inspecionadas; referências não examinadas pertencem a `uninspected_references`. Uma decisão substantiva exige `sources` preenchido.

**Princípio de segurança:** a passagem no validador comprova **coerência estrutural do JSON**, não que a prova citada exista realmente nos autos. A skill deve executar o cotejo e confrontar o relatório integral (resposta ou Google Docs realmente criado) com as fontes antes de entregar.


## Relatório de auditoria da VRA preenchida → Google Docs

A saída é **um relatório nativo e editável em Google Docs**, ou, na ausência de criação direta autorizada, uma **resposta integral única** que o usuário exportará pelo comando **Compartilhar e exportar → Exportar para: Documentos Google** no Gemini Apps. O template obrigatório é `assets/modelo_relatorio_vra_google_docs.md`.

**Rota direta:** criar e ler um documento somente se o ambiente oferecer integração Google Docs autorizada. Exigir retorno observável com documento/URL real e inspeção de todos os IDs antes de declarar `DOCUMENTO_CRIADO_E_VERIFICADO`.

**Rota Gemini Apps:** formatar o relatório completo em uma única resposta e registrar `PRONTO_PARA_EXPORTACAO`; esta condição não é prova de documento criado. Não usar PDF, DOCX, HTML ou JSON como entrega alternativa silenciosa.

**Indisponibilidade:** relatar `ERR_GOOGLE_DOCS_EXPORTACAO_INDISPONIVEL` quando a UI de exportação não existir para a conta, e nunca inventar um link Google Docs.

A passagem de um JSON no script `scripts/validar_e_formatar_vra.py` prova somente consistência estrutural e formatação textual. O script **não se conecta ao Google Docs**, não lê os autos e não comprova a validade material das evidências.

## Invariante de objeto auditado

A VRA preenchida é a **declaração auditada**, nunca um formulário a ser preenchido pela IA. Preserve cada resposta original e seu localizador; contraste com evidência independente dos autos; aponte a divergência e recomende correção humana sem gerar nem alterar outra VRA. O Google Docs contém o **relatório de auditoria**, não um checklist refeito.

## Gate de inspeção visual e de saída conforme modelo (v2.2.0)

- `source_inventory.image_only_pages`: lista de páginas relevantes de leitura textual ausente ou deteriorada; `source_inventory.visually_inspected_pages`: páginas inspecionadas visualmente (subset da numeração real). Decisão substantiva requer inspeção de todas as image-only pages materiais que amparem ausência ou confirmação de requisito, ou impedir a decisão se inacessíveis.
- Ausência documental não pode ser afirmada com base só em busca textual; conferir páginas que contêm imagens, inclusive diplomas assinados e verso/registro.
- Relatório final tem início, seções, matriz e critérios do `assets/modelo_relatorio_vra_google_docs.md`; **gate FMT-01 obrigatório**. Saída só pode ser considerada pronta se os 100% IDs inventariados constarem da seção 5, com conteúdo e fontes, se os achados estiverem individualizados e se não houver placeholders.
- Recusar como saída final qualquer resumo como “Quadro I: Em conformidade / Quadro II: falta documentação”, mesmo com fatos corretos.
- Um documento Google Docs só existe depois de criação efetiva pela integração autorizada ou de exportação nativa pelo usuário; a resposta integral pronta é `PRONTO_PARA_EXPORTACAO`, e não `DOCUMENTO_CRIADO_E_VERIFICADO`.


## Admissão P0 e recusa de corpus não verificado — v2.3.0

Nenhum objeto `source_inventory` preenchido pela IA constitui prova independente de leitura. Antes de decisão substantiva, usar metadados observáveis do arquivo recebido (contagem real de páginas), registros concretos de abertura em início/meio/fim e inspeção contextual dos documentos materiais. Na indisponibilidade dessas capacidades, decisão exclusiva `IMPEDIMENTO_TECNICO`, relatório de bloqueio sem juízo material e sem alegações de ausência documental. Recomendação de nova juntada é vedada quando a origem do problema é somente leitura incompleta da IA.

`source_inventory.pdf_pages_observed`, `page_count_provenance`, `first_middle_last_samples` e `access_proof` devem ser associados à fonte efetivamente consultada. Na execução local com PDF acessível, `scripts/verificar_pdf_entrada.py` fornece contagem e SHA-256 e o formatador pode conferir `--autos`; isso **não** atesta leitura semântica/visual.


## Contrato corpus segmentado e acesso real — v2.4.0

Campos complementares, quando houver fracionamento externo: `corpus_manifest` com `schema`, SHA-256 do arquivo original, `pdf_pages` originais e lista de `parts`; `chunk_receipts` com o que foi de fato recebido; `pages_actually_inspected` com referências a páginas e métodos usados. Manifesto prova divisão física, não leitura semântica.

- Nenhum conjunto incompleto de `parts` autoriza afirmar ausência de documento.
- Se a contagem real de páginas não for observável, nunca adotar 216/220 páginas da visualização parcial como total.
- Inviabilidade de leitura de qualquer segmento pertinente acarreta `IMPEDIMENTO_TECNICO`, sem achados substantivos.
- A saída para Google Docs só pode ser relatório integral após o gate probatório e o gate de formato.


## Controles adicionais do pacote ChatGPT 0.1.1

- `source_inventory.unassigned_page_ranges` e `unassigned_pages_note`: declaração justificada de quaisquer páginas físicas fora dos intervalos dos movimentos. O gate P0 bloqueia decisão substantiva se houver página que não pertença a nenhum movimento e não esteja explicitamente atribuída e revisada. Páginas com movimentação temporal não resolvida impedem conclusão de mérito.
- `source_inventory.source_pdf_sha256` e `vra_pdf_sha256` (opcionais): fingerprints do PDF integral dos autos e da VRA original, respectivamente. Só declarar checagem física se o operador executar a conferência contra arquivos reais.
- Quando `movement` e `page` forem números inequívocos, o validador exige que a página PDF esteja no intervalo do movimento inventariado e que o movimento seja elegível no corte. Page numbers internos de anexos exigem um localizador PDF rastreável separado: verificações não podem converter números internos em ordinais sem fundamento.
- O validador local atua sobre registros informados: não atesta exaustividade da leitura, elegibilidade histórica real nem eficácia no ambiente ChatGPT.
