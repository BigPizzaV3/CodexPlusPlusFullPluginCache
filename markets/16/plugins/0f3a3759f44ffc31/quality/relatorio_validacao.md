# Relatório de implementação e verificações — DIGG.IA: Assistente de Contratações Públicas

**Data:** 29/10/2026 (America/Sao_Paulo)  
**Versão:** 0.1.1 (revisão de metadados do pacote skills-only)  
**Estado:** testes estáticos locais APROVADOS; **ingestão de 0.1.0 observada na captura do Developer Portal (4 skills em checking); execução e validação de 0.1.1 no Developer Portal NÃO TESTADAS**.

## Diagnóstico da origem
ZIP de GPT customizado com **17 arquivos**, sem `plugin.json`/skills. Componentes: 2 instruções, JSONL 16 registros, HTML de framework, documento markdown, 5 modelos MPGO PDF, 2 atos PGJ, 1 decisão do TCE-GO, lei 14.133 em PDF escaneado, manual TCU 5ª edição (1.013 páginas), manual de redação e ícone. **16/16 hashes declarados na KB inválidos como SHA-256**, embora o original os rotule como hashes; indicadores de desempenho da KB e rótulos "validated" não vieram acompanhados de protocolo ou logs de teste.

## Arquitetura, adaptações e preservação
- Denominação institucional integral `DIGG.IA: Assistente de Contratações Públicas` preservada em descrição, instruções e documentação. Nome de interface abreviado para **`DIGG.IA: Contratações Públicas` (30 caracteres)**, por limite documentado para listagem pública da OpenAI. Slug técnico separado.
- 4 skills operacionais: entrada, redação, revisão documental e consulta de fontes.
- 16 arquivos originais preservados **byte a byte**, além do ícone; catálogo SHA-256 real com origem.
- KB curada com 16 itens: campos métricos e estado de validação original mantidos somente como metadados não verificados.
- 5 modelos oficiais em PDF íntegros, mais estrutura seccional transcrita e minutas auxiliares com indicação de pendências.
- Extrações normativas com paginação do manual TCU, modelos, atos, manual de redação e decisão TCE-GO. `lei_14133.pdf` sem OCR: verificação de redação deve ocorrer em fonte oficial atualizada.
- Protocolo com classificação de fonte, checagem de vigência, dados ausentes, LGPD, distinção TCU/TCE, controle humano e comparação DOD–ETP–TR.
- HTML original arquivado sem falsear sua função: é template de especificação GPT, não renderer de DOD/ETP/TR.
- Sem MCP, endpoints, credenciais, comandos externos ou integrações com SEI/Atena inventadas.

## Testes locais
Total de checagens de projeto: **19/19 aprovadas** (checagens estáticas/estruturais). Em amostras sintéticas, renderização de seções e pendências de DOD, ETP completo, ETP simplificado, TR e TR terceirização foi verificada. Fixture artificial detectou divergência de quantitativo de 12 versus 13 unidades entre DOD/ETP/TR. **Essas amostras NÃO foram produzidas por modelo LLM e não validam qualidade jurídica das respostas.**

## Resultado individual

- **APROVADO** — Manifesto Agent Plugins, schema e SemVer
- **APROVADO** — Nome oficial completo na descrição e nome abreviado <=30
- **APROVADO** — Identificador kebab-case
- **APROVADO** — Subtítulo <=30 caracteres
- **APROVADO** — Ícone quadrado >=48 <=4096, <=5MB (1254x1254, RGB)
- **APROVADO** — 4 skills operacionais <=1 MiB
- **APROVADO** — Fontes originais preservadas (16 fontes originais + ícone mantidos)
- **APROVADO** — TCU 1.013 páginas com índice íntegro
- **APROVADO** — KB curada 16 registros parseáveis
- **APROVADO** — 5 modelos MPGO com títulos sequenciais
- **APROVADO** — Minuta estrutural DOD
- **APROVADO** — Minuta estrutural ETP_COMPLETO
- **APROVADO** — Minuta estrutural ETP_SIMPLIFICADO
- **APROVADO** — Minuta estrutural TR
- **APROVADO** — Minuta estrutural TR_TERCEIRIZACAO
- **APROVADO** — Fixture DOD-ETP-TR coerente
- **APROVADO** — Fixture detecta divergência quantitativa
- **APROVADO** — Sem configuração MCP fictícia ou app binding
- **APROVADO** — Hashes originais inválidos identificados (16 de 16 hashes não verificáveis; novo inventário SHA-256 real criado)

## Revisão 0.1.1 — metadados para submissão
Os quatro endereços entregues em `website(5).txt` foram inseridos em `plugin.json`, sob `extensions.com.openai.interface` (chaves: `websiteURL`, `supportURL`, `privacyPolicyURL`, `termsOfServiceURL`). Os endereços responderam a consultas públicas em 29/10/2026; a página principal não evidencia acesso direto a suporte; política e termos de 18/09/2025 são dirigidos ao catálogo DIGG.IA, não ao plugin. Ver `quality/verificacao_urls_publicacao.json`. **Não é possível afirmar que a revisão jurídica/editorial das páginas esteja concluída.** A captura da versão 0.1.0 mostra quatro findings de URL e `0 of 4 skills checked` em processamento; isso não é prova de falha ou aprovação das skills. A 0.1.1 ainda precisa ser enviada ao draft existente para reprocessar os findings.

## Pendências antes da publicação
1. Enviar a versão 0.1.1 como nova versão no **mesmo draft já existente**, sem criar outro plugin, e verificar a ingestão dos skills e dos arquivos de referência, especialmente PDFs volumosos (a integridade local não comprova ingestão).
2. Executar ensaios **reais** com o modelo ChatGPT para DOD, ETP completo/simplificado, TR e terceirização, incluindo informações ausentes, correlação de documentos e prompt injection em anexos.
3. Revisão humana jurídico-administrativa e normativa pelo MPGO. Confirmar vigência e eventuais alterações dos Atos PGJ 80/2023 e 14/2016 e atualidade dos modelos; confirmar dispositivos citados no caso concreto.
4. Confirmar autorização de disponibilização, publicidade de documentos e direitos de uso de materiais institucionais. Avaliar se o público externo deve acessar cópias dos atos/modelos fornecidos.
5. Adequar o conteúdo das páginas de website/suporte, privacidade e termos especificamente ao plugin; conferir no portal os quatro findings após reupload. Confirmar se o nome abreviado de interface é aceito e vincular `developerName` à identidade verificada do publicador (atualmente `DIGG.IA`, como marca provisória). Cumprir demais declarações da plataforma; **não foi executada publicação ou criação de plugin na conta**.
6. Para geração automatizada de DOCX/PDF, recuperação RAG garantida ou integrações com processos/SEI, projetar e testar recursos adicionais com permissões explícitas. Não atribuir essas capacidades ao skills-only.

**Veredito:** Pacote estrutural de desenvolvimento pronto para tentativa de upload e validação do portal, mas **NÃO certificado como publicado, integrado ou aprovado juridicamente**.
