# MyBI IA (0.1.19)

Grade integrada ao Automático: todas as linhas recebidas pelo componente, colunas
aprovadas, medidas com nomes estáveis e texto formatado ou valor bruto. Sem scripts
livres ou bibliotecas externas. Consulte htmlGrid em references/html.md na Skill.

Personalização explícita sem estética fixa; preservação de INI geral e individuais;
datas por componente; cálculos DECIMAL; nomes estáveis no Automático e períodos
relativos em filtros novos e existentes. Consulte references/personalizacao.md na Skill.
Inclui Matriz, seletores, filtro de data, abas, DRE contábil/gerencial e regras
condicionais de texto, fundo, ícones, faixas e escalas. Também atualiza propriedades
e regras de componentes existentes, preservando a fonte e os demais elementos.
O contrato e os limites estão em references/componentes-nativos.md.

Referência offline em skills/criar-dashboard-mybi/references/mybi-plugin-contract:
7 páginas Web e 1 Windows, contrato portátil, exemplos sintéticos e pendências.
Nomes amigáveis nas propostas; HTML é apresentado como Automático.
Datas exigem confirmação da apresentação e granularidade antes da geração.

Logo e ícone vetoriais quadrados incluídos no manifesto para upload no portal.

Consulta aos manuais públicos para cores, fontes e aparência nos formatos nativo,
HTMLTemplate e JavaScript automático, respeitando os limites do gerador.

Reconhece sinônimos de componentes e solicita o formato quando não informado.
Inclui indicador circular padrão e grades.
Outros modelos prontos de segmentos e o gauge nativo ainda não têm paridade
com o gerador web. Consulte as limitações em references/escolha-componentes.md.

Ao editar um XML existente, preserva seu nome de arquivo e título original. As seções
do formatacao.ini acompanham o nome do XML.

A entrada pode ser imagem, esquema copiado do MyBI ou ambos. Se a fonte já existe, a
habilidade pede também o XML atual do dashboard e o usa como base: preserva DataSources,
consulta ou procedure, parâmetros, cálculos e itens existentes, acrescentando os novos
componentes. Sem fonte existente, cria o dashboard completo. Nenhuma credencial é inventada.

O ZIP gerado inclui formatacao.ini sem estilo obrigatório. Cores, imagens, fontes,
transparência e dimensões são preservadas ou seguem o pedido/referência aprovada.
Arquivos individuais de formatação podem ser preservados. Validar a aparência após importar.

As aprovações são solicitadas somente por mensagens normais do chat, sem formulários
interativos. A habilidade inclui metadados próprios de interface para substituir o
rascunho genérico em inglês por uma solicitação curta e pertinente em português.

Plugin de skill, sem MCP, servidor, autenticação nem chave de IA. A conversa analisa
o pedido e os materiais; Python valida e monta um ZIP contendo DashboardWeb/dashboard1.xml.
O modo principal gera componentes separados, como Criar Dashboard com IA sem marcar HTML.

## Conteúdo

- `skills/criar-dashboard-mybi/SKILL.md`: fluxo com aprovações.
- `references/catalog.json`: tipos e bindings extraídos do MyBI, com hashes de origem.
- `references/contrato.md`: regras, escopo e diferenças conhecidas.
- `assets/serializer-reference.xml`: referência criada pelo serializador DevExpress 24.2.5.
- `scripts/mybi_package.py`: gerador/validador offline, biblioteca padrão Python 3.10+.

O ZIP deste plugin NÃO é o ZIP de dashboard: não importá-lo no MyBI.
O ZIP gerado pela skill é que vai para a importação de dashboards do cliente.

## Uso e teste

No ambiente que carregar a skill, peça "Crie um dashboard MyBI" e siga as aprovações.
Python é necessário para arquivos; Node.js é necessário apenas para validar sintaxe de JS
do modo Dashboard HTML. Nenhum dos dois executa chamadas ao MyBI ou a modelos.
Sem esquema copiado, o cliente deve vincular a fonte lógica à sua tabela/view e conexão.
Com esquema de fonte existente, o XML-base é obrigatório para evitar substituir a fonte
por um documento incompleto.
Não existe fonte real ou registro demonstrativo embutido.

O manifesto `.codex-plugin/plugin.json` serve ao scaffold; `plugin.json` é o manifesto
portátil skills-only. No teste web inicial, o usuário carregou o ZIP em
Plugins > Habilidades > + e abriu Chat pelo menu da habilidade. A conversa apresentou
propostas e link de download. Cada nova versão ainda precisa de teste visual no MyBI.
Não pedir instalação de runtimes no computador do usuário web: scripts executam no
ambiente da conversa, quando disponível. Ainda não publicado no diretório público.

## Limites da versão

O catálogo é fechado. CalculatedFields numéricos têm suporte restrito em calculos.md.
Filtros nativos e propriedades visuais arbitrárias não são compilados; não prometer paridade com todo o editor MyBI.
Detalhes e alternativas aprováveis estão em contrato.md. O HTML é opcional e secundário.
Os scripts validam a estrutura, não a qualidade visual nem dados do cliente.
Validar importação/renderização em ambiente de teste antes de distribuir em produção.

## Manutenção no repositório MyBI

`scripts/tests/DashboardPlugin.Smoke/export_catalog.py` exporta os bindings do runtime.
`scripts/tests/DashboardPlugin.Smoke/` contém testes Python e roundtrip DevExpress;
as DLLs do MyBI/DevExpress não são distribuídas neste plugin.
Mudanças no catálogo exigem revisão e novos testes, não atualização cega dos hashes.
