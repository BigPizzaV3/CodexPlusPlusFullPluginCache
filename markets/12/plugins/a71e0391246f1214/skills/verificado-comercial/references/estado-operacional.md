# Estado operacional registrado em 01/11/2026

Usar como ponto de partida histórico, não como consulta atual do serviço.

- Plugin GNG Verificado 1.1.1 publicado. Esta skill pessoal é separada: não inferir que foi incorporada ao pacote público do plugin.
- Checkout de produção /finalizar-compra/ corrigido para formulário clássico WooCommerce; campos GNG, Pix e PayPal apareceram. Isso não comprova captura nem entrega.
- Teste Sandbox na homologação gerou pedido 27206 e transação, mas permaneceu em revisão manual/PENDING; não marcou pagamento confirmado.
- Retorno PayPal gerado com /gng-homologacao/ duplicado. Um pedido foi recuperado manualmente; correção automática e nova prova integral ainda pendentes.
- Rota da homologação foi separada do Worker principal, que removia token. Não alterar outras rotas como parte do atendimento.
- Nova compra de homologação 27220: WooCommerce processing, total BRL 997, date_paid 01/11/2026 14:13:36, transação preenchida e nota automática de pagamento. Retorno automático à confirmação funcionou. O pedido foi para PENDING_REVIEW sem aprovação do selo. Não confundir esse resultado com o teste anterior pendente.
- Em 01/11/2026, descrições dos produtos WooCommerce de produção foram atualizadas: Verificado (997/ano), Verificado Premium + Instalação Assistida (1997/ano), Verificado Authority (2997/ano). Valores são registro histórico; consultar catálogo atual antes de ofertar. Landing page e pacote público podem continuar com conteúdo anterior.
- Fluxo integral pagamento confirmado → análise/aprovação → entrega protegida/certificado ainda não validado. Skill comercial pode orientar, consultar catálogo e registro; não anunciar compra automática completa como pronta.

## Atualizar prontidão somente com evidência

Antes de declarar liberação comercial completa, exigir teste integral identificado em ambiente apropriado com confirmação do provedor e do WooCommerce, retorno automático, aprovação registrada e entrega protegida acessível ao titular. Conferir que pagamento pendente e usuário não autorizado não recebem o código, e que uma repetição não cria emissão duplicada. Registrar achados sem segredos e relatar falhas honestamente. Validar Pix separadamente de PayPal; não inferir sucesso de um pelo outro.

Não iniciar novo teste, cobrança real, emissão real, alteração de infraestrutura ou publicação do plugin por simples invocação de atendimento. Seguir o escopo solicitado na sessão; aproveitar autorização anterior somente quando aplicável. Nunca converter manualmente PENDING em pago para satisfazer a sequência.

- Atendimento internacional: comunicação da skill ampliada em 01/11/2026 para interessados de qualquer país e idioma. Isso não comprova checkout internacional: cadastro atual exige cidade e UF no padrão brasileiro. Não simular dados brasileiros para clientes estrangeiros.
- Apresentação da skill: Verificado — Atendimento Internacional; nome de invocação verificado-comercial. Nomes técnicos de integrações e registros existentes permanecem compatíveis.
