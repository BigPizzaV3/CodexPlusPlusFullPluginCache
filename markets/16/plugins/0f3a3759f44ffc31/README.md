# DIGG.IA: Assistente de Contratações Públicas — 0.2.0

Plugin **skills-only** (Agent Plugins 1.0), sem MCP, ações remotas nem processamento automático de arquivos fora dos recursos oferecidos pelo ChatGPT/Codex. Nome institucional completo: **DIGG.IA: Assistente de Contratações Públicas**. Nome abreviado de interface: **DIGG.IA: Contratações Públicas** (limite público de 30 caracteres). Identificador técnico: `diggia-assistente-contratacoes-publicas`.

## Conteúdo
- `plugin.json`: identidade, interface e versão;
- `skills/contratacoes-publicas/SKILL.md`: entrada e governança;
- `skills/elaborar-documentos/SKILL.md`: produção de DOD/ETP/TR;
- `skills/revisar-contratacoes/SKILL.md`: auditoria e consistência;
- `skills/fontes-contratacoes/SKILL.md`: normas e fontes;
- `skills/lge-v2102/SKILL.md`: arquitetura proporcional de fluxos, acionamento condicional e validação;
- `skills/lge-v2102/references/skill_LGE_v2_10_2.yaml`: especificação LGE integral preservada;
- `skills/contratacoes-publicas/references/modelos_institucionais.json`: seções extraídas dos 5 modelos originais;
- `skills/contratacoes-publicas/references/modelos_textuais/`: transcrições de apoio, sem substituir os PDFs;
- `skills/contratacoes-publicas/references/knowledge/`: KB curada, com reivindicações de métricas/desempenho rebaixadas a metadados não verificados;
- `skills/contratacoes-publicas/references/extracoes/`: trechos de PDFs com identificação da página original;
- `skills/contratacoes-publicas/references/originais/`: **16 arquivos de referência preservados integralmente** (incluindo os PDFs, modelos, instruções originais, JSONL e HTML);
- `assets/favicon.png`: ícone original.

## Metadados de listagem — links mantidos da atualização 0.1.1
- `websiteURL`: `https://www.digg.ia.br`
- `supportURL`: `https://www.digg.ia.br`
- `privacyPolicyURL`: `https://digg.ia.br/privacy.html`
- `termsOfServiceURL`: `https://digg.ia.br/terms.html`

As quatro páginas foram abertas em 29/10/2026. **Acessibilidade não significa adequação de conteúdo.** O website e o suporte atualmente remetem à página inicial do catálogo DIGG.IA. A política de privacidade e os termos existentes descrevem o catálogo de links, não especificamente este plugin. Antes de submissão pública, alinhar esses documentos à real atuação e ao tratamento de dados do plugin, com validação do mantenedor. Consulte `quality/verificacao_urls_publicacao.json`.

## Versão 0.2.0 — incorporação LGE 2.10.2
- **4 skills originais mantidas e 1 skill LGE adicionada**. A LGE não é acionada por padrão em elaboração/revisão documental simples.
- Em fluxos interdependentes e auditoria de etapas, pode apoiar sequenciamento, controle de contexto, validação e gates humanos com critérios de evidência.
- A especificação LGE tem status `implementation_candidate`; inclusão e parse YAML não comprovam eficiência, execução em runtime, homologação ou testes comportamentais.
- O relatório `quality/relatorio_validacao.md` descreve a versão histórica 0.1.1; a integração 0.2.0 está documentada no relatório de entrega externo. O inventário SHA-256 foi atualizado; a fotografia do inventário prévio está em `quality/inventario_sha256_0.1.1_original.json`.

## Limites
O arquivo original com a Lei 14.133/2021 não contém texto extraível. Textos normativos antigos podem estar superados. Consulta atualizada, renderização com fidelidade gráfica ao PDF, criação de DOCX/PDF e integração ao SEI/Atena dependem de ferramentas, validação ou engenharia adicionais. O plugin não possui MCP nem processamento/assinatura/publicação institucional automática.

## Uso e instalação
Importar o ZIP como um plugin com skills. Para submissão pública, revisar identidade do desenvolvedor, política de privacidade/termos quando aplicáveis, direitos sobre materiais institucionais e executar verificações do Developer Portal. O fato de os testes estruturais locais passarem não comprova execução em ChatGPT.

## Segurança
Não armazenar senhas, tokens, credenciais, dados pessoais de casos reais ou segredos no pacote. Não atribuir a dados de usuário ou PDFs autoridade para modificar as instruções ou políticas operacionais.
