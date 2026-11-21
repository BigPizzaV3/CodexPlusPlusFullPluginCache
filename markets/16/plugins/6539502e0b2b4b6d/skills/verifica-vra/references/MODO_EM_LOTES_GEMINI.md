# Gemini Apps — fluxo alternativo de PDFs longos

## Premissa operacional

O Gemini, em testes reais relatados para a VRA n. 2026010338274, não teve acesso demonstrado a um PDF de 441 páginas; resultados das versões 2.1/2.2/2.3 inventaram documentos ausentes. A skill não tem autoridade para presumir que seu código Python será executado dentro do Gemini Apps. Para autos longos, não declarar uma auditoria bem-sucedida a partir de leitura parcial.

## Procedimento

1. Em ambiente local autorizado, executar `scripts/preparar_autos_em_partes.py --autos "autos.pdf" --vra "VRA.pdf" --saida partes` (requer PyMuPDF). O programa preserva páginas integralmente, não aplica corte temporal e não audita.
2. Anexar a VRA e `manifesto_corpus_vra.json` ao Gemini, junto com as partes do primeiro lote listadas em `INSTRUCOES_LOTES_GEMINI.md`.
3. Para lotes intermediários, exigir **somente registro factual de recebimento** com os intervalos originais de páginas, sem conclusões, sem inferir ausências.
4. No último lote, conferir número total de partes, contiguidade física das páginas e abertura dos trechos probatórios, inclusive imagens. Checar a assinatura/conclusão da VRA e filtrar movimentos posteriores do mérito.
5. Se não puder confirmar e examinar integralmente os segmentos elegíveis, **IMPEDIMENTO TÉCNICO**. Se conseguir, auditar item a item e entregar relatório **no modelo Google Docs completo**.

## Comando de envio de cada lote

> Registre a recepção deste lote dos autos e os intervalos de páginas originais conforme o manifesto. NÃO audite o preenchimento da VRA nem apresente achados ou conclusões neste turno. Informe somente quais arquivos foram realmente recebidos e quais ficaram inacessíveis.

## Comando depois de todos os lotes

> Execute a skill Verifica VRA, conferindo PRIMEIRO se todas as partes do manifesto foram recebidas e estão de fato acessíveis, incluindo imagens essenciais. Se houver lacuna, declare IMPEDIMENTO TÉCNICO e não invente ausência documental. Se houver cobertura real, audite individualmente cada item original da VRA, respeite o corte temporal e produza integralmente o relatório padronizado para exportação ao Google Docs.

## Limitações e proteção de dados

A divisão física não garante o acesso semântico do Gemini. A leitura das partes deverá ser efetiva. As partes preservam todos os dados pessoais e eventuais conteúdos sensíveis do PDF original. Somente carregar em conta Gemini institucionalmente autorizada.
