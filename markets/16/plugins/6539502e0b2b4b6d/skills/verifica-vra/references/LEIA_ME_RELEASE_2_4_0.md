# Verifica VRA — release 2.4.0

**Mudança motivada por falha real persistente no Gemini Apps:** versões anteriores 2.1–2.3 não conseguiram acessar adequadamente um PDF de 441 páginas e inventaram ausências em documentos que constavam das páginas 298–351. A versão 2.4.0 adiciona uma estratégia operacional **externa**, opcional ao Gemini, de segmentação verificável dos autos. Isso NÃO constitui correção empírica do motor Gemini.

Para PDFs longos, usar `scripts/preparar_autos_em_partes.py` com PyMuPDF (executor autorizado), fornecer as partes e o manifesto em lotes. Sem prova de acesso, a saída correta é IMPEDIMENTO TÉCNICO. Não improvisar relatório com base em trechos iniciais.

A skill NÃO pode executar automaticamente o script se o Gemini Apps não oferecer esse ambiente. Os arquivos `.pdf` derivados dos autos contêm informações potencialmente sensíveis; aplicar controles institucionais de privacidade antes de fazer uploads.

A saída, quando integralmente auditada, continua Google Docs editável, com 42 itens neste caso de teste, ou outro total real conforme o formulário. Validação local não é teste runtime Gemini.
