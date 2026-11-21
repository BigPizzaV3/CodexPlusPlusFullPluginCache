# Verifica VRA — pacote 0.2.0 para ChatGPT

**Objeto:** auditoria documental de segunda camada de VRA **já preenchida**, mediante confronto com os autos que existiam até sua assinatura/conclusão. Não produz nem altera nova VRA. Resultados são relatórios de conferência assistida, sem homologação administrativa.

## Componentes

- `plugin.json`: manifesto Agent Plugins 1.0; identidade `verifica-vra`.
- `skills/verifica-vra/SKILL.md`: missão, P0/P1, corte temporal, defesa contra alegações de ausências não comprovadas, formato e Google Docs.
- `skills/verifica-vra/assets`: modelo de relatório editável com matriz integral.
- `skills/verifica-vra/scripts`: ferramentas **locais e opcionais** de contagem/hash de PDFs, segmentação, validação de registros e FMT-01.
- `skills/verifica-vra/tests`: testes locais e cenários sintéticos, NÃO evidência de auditoria institucional.
- `skills/verifica-vra/references`: contrato, schema e histórico da migração Gemini→ChatGPT, preservados para rastreabilidade.

## Caminho de uso

1. No ChatGPT, anexar a VRA preenchida e os autos completos; solicitar auditoria do preenchimento sem geração de VRA nova.
2. Exigir verificação física da contagem total e acesso efetivo aos trechos relevantes (incluindo imagens), inventário total e corte histórico; declarar impedimento técnico diante de qualquer falha material.
3. Elaborar a matriz item a item preservando a resposta original e comprovação elegível, com classificação material e do preenchimento.
4. Exigir gate FMT-01. Com Google Docs autorizado, criar **documento Google nativo**, escrever e ler o resultado para conferir a integridade; sem isso, entregar Markdown completo, editável e informar que não houve criação no Drive.

**Importante:** o plugin é `skills-only`: nenhum servidor MCP, credencial ou integração Google Docs está incluído. O uso de Google Docs depende da conexão externa legítima já acessível à sessão. Scripts não se executam automaticamente ao instalar o ZIP.

## Testes locais

`python -m unittest discover -s skills/verifica-vra/tests -v`

Exemplo **sintético** de geração local de relatório:

`python skills/verifica-vra/scripts/validar_e_formatar_vra.py --dados skills/verifica-vra/tests/analise_sintetica.json --saida /tmp/relatorio_vra_sintetico.md`

Para confirmar hashes de arquivos reais, acrescente `--autos /caminho/autos.pdf --vra /caminho/vra.pdf`; se os respectivos SHA-256 estiverem declarados no JSON, qualquer divergência bloqueia a saída. O pré-voo de PDF requer PyMuPDF/fitz.

**Validação local != auditoria concluída.** Os testes verificam estruturas, limites e contratos. A conferência semântica dos autos, acesso integral e criação de Google Docs precisam de testes de aceitação no ambiente institucional autorizado.

## Atualização de metadados e identidade visual — 0.1.2

- `websiteURL`: https://www.digg.ia.br
- `supportURL`: https://www.digg.ia.br (a página principal ainda não identifica um canal de suporte exclusivo do plugin).
- `privacyPolicyURL`: https://digg.ia.br/privacy.html
- `termsOfServiceURL`: https://digg.ia.br/terms.html
- Ícone `assets/icon.png`: imagem fornecida pelo autor (`favicon.png`), normalizada para 512 × 512 px (PNG).
- Versão elevada para `0.1.2`, sem alteração de regras normativas da auditoria ou dos scripts operacionais.

### Pendências para submissão pública

Estes endereços estão configurados no manifesto, mas a política de privacidade e os termos atualmente publicados são apresentados para o **catálogo de links DIGGIA**, não necessariamente para os recursos, dados e riscos da skill Verifica VRA. O website também não identifica suporte específico ao plugin. Antes da submissão pública, o autor deve adequar as páginas aos fluxos reais de arquivos administrativos, incluindo dados pessoais, acesso aos autos, eventual gravação no Google Docs, finalidades, compartilhamento e retenção, e disponibilizar contato ou suporte identificável. URLs válidas não garantem aprovação jurídica ou editorial.

A versão continua sendo **skills-only**, sem integração MCP própria, e os testes de estrutura não comprovam execução operacional no ChatGPT nem criação real no Google Docs. Materiais de regressão podem conter identificação de processos e pessoas e devem ser inspecionados pelo responsável antes da submissão pública.

## Correção técnica da release 0.1.3

- Caminhos normalizados para ZIP com `plugin.json` e `skills/` na raiz.
- Versão do manifesto sincronizada com a release 0.1.3 para criar novo rascunho após 0.1.2.
- Nenhuma regra de auditoria, script operacional, fixture, contrato ou documento de referência foi alterado.
- Aceitação efetiva na OpenAI Platform e testes de execução ChatGPT permanecem pendentes.


## Integração LGE 2.10.2 — release 0.2.0

- Segunda skill portátil **`skills/loop-graph-engineering/SKILL.md`**, com os gatilhos de uso e limites de competência.
- Especificação original **`skills/loop-graph-engineering/references/skill_LGE_v2_10_2.yaml`**, idêntica em bytes ao arquivo fornecido pelo responsável (SHA-256: `bc42f3f95432bffd8fa54fd2de1c6f26880b34ee8f3bfde096919fcb60db10da`).
- A skill principal e a referência normativa VRA 2.4.0 apontam agora para a **LGE 2.10.2**; a LGE 2.10.1 permanece apenas como histórico passivo em `references/`, sem roteamento ativo.
- O contrato de auditoria da VRA, seus gates P0/P1, scripts, modelo de Google Docs, evidências de regressão e arquivos institucionais permanecem funcionalmente preservados.
- O conjunto de testes passa a incluir controles de reconhecimento e versão da nova skill. Não constitui auditoria institucional executada nem teste do runtime do portal.
- **`defaultPrompt` preservado exatamente**, inclusive pontuação, tipo array e ordem original. Identificador `verifica-vra`, categoria, links institucionais e ícone inalterados.

**Status:** verificação estática local; aceitação e teste comportamental na OpenAI Platform pendentes. A LGE 2.10.2 é `implementation_candidate` e não implica autorização para execução autônoma de ações externas.
