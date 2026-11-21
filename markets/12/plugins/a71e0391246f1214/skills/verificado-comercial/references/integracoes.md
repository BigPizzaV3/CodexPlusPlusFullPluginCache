# Integrações e caminhos oficiais

Descobrir esquemas das ferramentas antes de chamar. Preferir conectores ao navegador quando suficientes. Usar apenas uma variante de cada serviço por ação.

| Intenção | Ferramenta ou caminho | Evidência que fornece |
|---|---|---|
| Consultar registro | GNG `gng_verified_check_domain` | Situação, domínio, identificador e validade retornados |
| Diagnóstico gratuito | GNG `gng_verified_precheck_site` | Sinais técnicos públicos; não aprova selo |
| Diagnosticar instalação | GNG `gng_verified_diagnose_installation` | Correspondência com registro e sinais no HTML |
| Localizar planos | Vendedor G `search_products`, `get_product_details` | Catálogo e condições atuais |
| Comparar e orçar | Vendedor G `compare_products`, `generate_sales_quote` | Comparação e orçamento informativo, sem pedido persistido |
| Criar link | Vendedor G `create_checkout_link` | URL derivada do produto, sem criar carrinho/pedido/pagamento |
| Solicitação e planos | https://gazetanewsguarulhos.com.br/gng-verificado/ | Página comercial; conferir antes de recomendar plano |
| Portal | https://verified.gazetanewsguarulhos.com.br/app | Navegação do serviço |
| Analisar meu site grátis | https://verified.gazetanewsguarulhos.com.br/app#analisar | Formulário de diagnóstico |
| Solicitar verificação | https://verified.gazetanewsguarulhos.com.br/app#solicitar | Explicação e acesso à loja |
| Acompanhar solicitação | https://gazetanewsguarulhos.com.br/minha-conta/orders/ | Área autenticada do titular |
| Instalar meu selo | https://verified.gazetanewsguarulhos.com.br/app#instalar | Orientação; código individual fica no pedido aprovado |
| Instruções | https://verified.gazetanewsguarulhos.com.br/instalacao | Guia da instalação |
| Consultar certificado | https://verified.gazetanewsguarulhos.com.br/app#certificado | Formulário por domínio; usar URL individual retornada pelo registro |
| Suporte | https://verified.gazetanewsguarulhos.com.br/support | Canal de atendimento oficial |

Não inventar botões interativos no ChatGPT: apresentar links Markdown com esses rótulos quando pertinentes. Só declarar componente ou botão embutido se a ferramenta efetivamente o retornar.

As ferramentas públicas GNG não compram, aprovam ou emitem selos. As ferramentas Vendedor G listadas não executam pagamentos. Uma skill organiza o uso das capacidades presentes; não cria APIs comerciais nem concede acesso administrativo. Descobrir novas capacidades e validar seus limites antes de utilizá-las.
