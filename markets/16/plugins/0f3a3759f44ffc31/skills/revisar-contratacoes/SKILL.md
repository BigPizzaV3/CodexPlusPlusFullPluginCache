---
name: revisar-contratacoes
description: Use para revisar DOD, ETP ou TR, verificar conformidade, identificar omissões e comparar a consistência entre documentos de contratações públicas.
---

# Auditoria documental e consistência entre DOD, ETP e TR

1. Confirmar documentos efetivamente fornecidos, ano/modelo e escopo. Não alegar auditoria integral de anexos não lidos.
2. Abrir referência de cada modelo em `../contratacoes-publicas/references/modelos_institucionais.json` e cotejar seções e subcampos preservados no PDF original.
3. Aplicar checklist de `../contratacoes-publicas/references/protocolo_documental.md`, incluindo objeto, justificativa, compatibilidade com PCA, quantidade e memória, valor e formação de preço, cronograma, requisitos, parcelamento, gerenciamento, orçamento, riscos e anexos quando pertinentes.
4. Distinguir irregularidade documental comprovada, informação ausente, risco e divergência interpretativa. Não presumir obrigatoriedade de elementos legalmente excepcionáveis sem analisar o regime.
5. Para múltiplos documentos, comparar cada dimensão em uma matriz: `[DOD | ETP | TR | STATUS | EVIDÊNCIA | RECOMENDAÇÃO]`. Status restritos: COERENTE; DIVERGENTE; AUSENTE; NÃO APLICÁVEL COM JUSTIFICATIVA; VERIFICAÇÃO PENDENTE.
6. Fundamentos legais somente após consulta verificável, com dispositivo, redação aplicável e data. Precedentes TCU/TCE: indicar órgão, processo/acórdão e limites de pertinência.
7. Produzir relatório item a item, recomendações de saneamento e ressalva de revisão humana. Se os documentos não estiverem anexados, orientar a análise sem inventar resultado.
