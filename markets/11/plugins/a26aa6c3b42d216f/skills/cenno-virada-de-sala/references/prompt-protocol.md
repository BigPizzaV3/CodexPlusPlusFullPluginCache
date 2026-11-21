# Protocolo de prompts

## Registro por projeto

Escolha nomes como F00_plenaria, F01_saida, F02_auditorio_vazio e A00_F00-F01. Defina a ordem pelo conteúdo, não pela ordem de envio dos anexos. Registre arquivo-mestre, base vazia, jantar pronto e layout. Não associe arquivos que não foram inspecionados.

Tabela de planejamento: ID; estado visível; objetos/pessoas presentes; mudança em relação ao anterior; fonte visual; alvo seguinte; status. Tabela de animação: ID; frames de origem/destino; ação dominante; trajetos; duração pretendida; modo disponível; status. Duração pretendida é proposta editorial até verificar limites da ferramenta.

## Construção do prompt estático

Preencha estes componentes em um único texto pronto para colar:

1. Tarefa: editar a referência para mostrar o estado específico, sem redesenhar o local.
2. Papéis das referências: imagem-mestre governa arquitetura/câmera; jantar final governa posições do mobiliário; frame anterior governa progresso da operação. Em conflito, arquitetura da mestre prevalece.
3. Descrição explícita dos fixos observados: características do teto, palco, LED, piso e enquadramento reais do projeto.
4. Estado: quais pessoas, cadeiras, mesas e objetos estão presentes, onde e em qual quantidade verificável.
5. Alteração limitada: o que adicionar, retirar ou reposicionar nesta etapa; o que permanece idêntico.
6. Luz e LED: estado de serviço, teste ou gala; preservar suporte, bordas e curvatura. Para mapa de teste, preferir o mesmo arquivo gráfico fornecido; não exigir uma nova grade numerada diferente em cada frame. Logos e textos exigem revisão, não promessa de reprodução exata.
7. Acabamento: preservar proporção, resolução alvo quando suportada, materialidade, escala e realismo da referência.
8. Restrições específicas: câmera imóvel, arquitetura inalterada, nenhuma mesa extra, nenhum objeto incompatível com a etapa. Inclua restrições no texto quando a ferramenta não tiver campo negativo.

Exemplo de trecho operacional, a adaptar ao espaço e à fase:

“Show the approved round tables in their exact final positions, with bare tabletops. Keep the central circulation route clear. No tablecloths, tableware, flowers or guests are present yet. Crew members carry the final table into the remaining planned position. Do not add another table or move any installed table.”

Não envie esse trecho sozinho: inclua a descrição concreta da cena e os invariantes. Frame estático mostra um instante, não várias fases sobrepostas nem uma colagem.

## Construção do prompt de animação

Preencha estes componentes por transição:

1. “Locked-off tripod shot, continuous time-lapse”: mesmo enquadramento, sem pan, tilt, dolly, zoom, reenquadramento, corte ou transição por dissolução.
2. Estado inicial coerente com o frame anexado.
3. Atores e ação dominante: quem transporta o quê e por onde; sequência física plausível; intensidade de atividade proporcional ao trecho.
4. Progressão: começo, meio e fim. Não peça múltiplas montagens completas num trecho curto.
5. Resultado: estado visual desejado, posições finais e retirada da equipe quando pertinente.
6. Continuidade arquitetônica concreta e objetos estacionários que não podem mudar.
7. Ritmo acelerado com movimento legível e borrão moderado apenas nas pessoas/objetos em movimento. Ambiente fixo nítido. Time-lapse não significa câmera acelerada nem movimento frenético de toda a sala.
8. Evitar teleportes, fusão de móveis, objetos atravessando pessoas/mesas, morphing arquitetônico e troca de layout. Não adicionar áudio, fala, títulos ou música sem solicitação; não prometer controle de áudio se a ferramenta não permitir.

Exemplo de ação para toalhas:

“Crew members enter along the designated aisle carrying folded linens. They approach the existing tables, unfold one tablecloth per table and spread it naturally over the tabletop. Previously dressed tables stay in place and remain dressed. The cloth settles under gravity. End with every planned table covered, no tableware or floral decorations yet, and the crew carrying unused supplies out of frame.”

O prompt completo deve repetir os detalhes fixos pertinentes e especificar as rotas observáveis ou hipóteses declaradas. Não descreva o frame final como garantido quando somente Start Frame estiver disponível.

## Verificação antes da entrega

- Cada mudança entre estáticas tem uma transição correspondente; nenhuma fase exige objetos ausentes na origem sem mostrar sua entrada.
- Quantidade e posição das mesas coincidem entre montagem, toalhas, decoração e jantar.
- O modelo da cadeira não muda arbitrariamente; reaproveitamento e substituição são escolhas explícitas.
- Público sai antes da movimentação pesada; retorna após retirada dos carrinhos e materiais de trabalho.
- Luz pode mudar, material do piso não; conteúdo do LED pode mudar, sua geometria não.
- Cada prompt contém detalhes suficientes para uso independente e anexos identificáveis.
- O plano respeita o modo solicitado e distingue alvo desejado de resultado efetivamente validado.
