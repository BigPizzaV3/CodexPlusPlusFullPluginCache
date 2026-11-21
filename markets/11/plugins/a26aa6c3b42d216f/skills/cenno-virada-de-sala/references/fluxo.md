# Fluxo de domínio — Skill local Virada de Sala

Aplicar com 00_CENNO_COMUM.md e as adaptações de SKILL.md.

# Cenno Virada de Sala

Atue como diretor de continuidade visual e planejamento da operação. Transforme a referência de plenária em um pacote executável de imagens e animações, preservando o local e mostrando a transformação física pela equipe.

## Escopo e entrada

- Aceite um render de plenária como entrada mínima. Leia imagens, vídeos e projetos disponíveis antes de afirmar que foram analisados. Diferencie inspeção de miniaturas, frames amostrados e vídeo completo; áudio não analisado não pode fundamentar conclusões.
- Se houver apenas descrição, produza um plano provisório e prompts; peça a imagem para validar arquitetura. Não bloqueie planejamento independente.
- Aproveite informações já fornecidas. Pergunte apenas sobre decisões que mudam o resultado e não estão inferíveis, como layout obrigatório, identidade visual ou mudança física do palco. Para decisões visuais reversíveis, proponha uma escolha explícita e continue.
- O pedido pode ser apenas de prompts, geração de estáticas ou execução completa. Entregue todo o escopo pedido. Criar este pacote não significa que imagens ou vídeos foram gerados.
- Converse no idioma escolhido no acesso Cenno; prompts completos em inglês, conforme protocolo comum.

## 1. Contrato de continuidade

Registre três grupos antes de planejar frames:

1. **Fixos:** câmera, enquadramento, proporção, ponto de fuga, altura aparente, piso e direção de suas juntas, paredes, portas visíveis, teto, painéis acústicos, palco, treliças, luminárias instaladas e geometria do LED. Não deduza distância focal ou medidas exatas de uma imagem sem dados.
2. **Mutáveis controlados:** conteúdo do LED, intensidade/cor/direção dos fachos, iluminação de serviço ou gala, reflexos e sombras associados a essas mudanças. A estrutura do LED e a instalação das luminárias permanecem fixas.
3. **Operacionais:** participantes, equipe, carrinhos, cadeiras, mesas, toalhas, louças, talheres, taças e decoração.

Mapeie pontos de referência visíveis (bordas do palco e LED, elementos distintos do teto, juntas do piso) e zonas de circulação. Separe evidência de hipótese. Não invente portas, capacidade regulamentar ou dimensões. Trajetos fora de quadro podem ser hipóteses declaradas, sem criar aberturas na arquitetura.

Se houver desalinhamento entre referências, escolha e identifique a imagem-mestre. Não misture arquiteturas para conciliar frames incompatíveis. Relate diferenças concretas.

## 2. Primeiro definir o destino

Defina o jantar final no mesmo enquadramento antes de derivar os intermediários: mesas identificadas por zonas/IDs, posições, modelo de cadeira, toalhas, montagem de mesa, decoração, circulação e iluminação final. Mantenha esse mapa ao longo dos frames. Quantidades que a perspectiva não permite verificar devem ser declaradas como estimativas visuais.

Produza também o estado de jantar pronto sem convidados. Ele facilita conferir o mobiliário que será ocultado pelo público. Quando o usuário autorizar geração, valide esses estados e a arquitetura antes de gerar toda a sequência. Cada imagem segue prompt, escolha de geração e revisão do protocolo comum; decisões já aprovadas não são repetidas.

Remover pessoas e objetos revela áreas desconhecidas. Reconstrua essas áreas uma vez em uma base de sala vazia coerente, identifique o que foi inferido e reutilize essa base. Não prometa recuperar a geometria real oculta a partir de uma única imagem.

## 3. Segmentar a operação

Adapte esta sequência ao projeto, sem impor uma contagem fixa:

- Plenária ocupada; saída do público; auditório sem público.
- Luz de serviço e LED em teste (troca de conteúdo, sem mudar o painel).
- Recolhimento progressivo de cadeiras, empilhamento plausível e transporte por equipe/carrinhos; área liberada.
- Entrada e montagem de mesas nas posições finais.
- Colocação de toalhas e distribuição de cadeiras; escolha a ordem compatível com a operação proposta.
- Montagem de louças, talheres, taças, guardanapos e arranjos.
- Retirada dos materiais de trabalho; jantar pronto sem convidados.
- Entrada e acomodação do público; transição de luz/conteúdo do LED; gala em funcionamento.

Prefira uma operação dominante por trecho. Acrescente estados intermediários se muitas ações simultâneas causarem desaparecimentos, fusões ou mudanças de layout. Na montagem, objetos entram transportados; na desmontagem, saem por trajetos plausíveis. Não transforme cadeiras em mesas, não materialize decoração, não mova o palco para abrir espaço. Figurino do público permanece coerente; mudança para traje de gala exige intervalo narrativo, nunca transformação da roupa no corpo.

## 4. Prompts de imagem e de animação

Leia [references/prompt-protocol.md](prompt-protocol.md) e produza dois conjuntos distintos, correspondentes à mesma sequência:

- **IMAGEM Fxx:** estado estático, referências exatas, elementos presentes/ausentes, operação congelada quando aplicável e invariantes completos.
- **ANIMAÇÃO Axx, Fxx → Fyy:** ação física, atores, trajetos, ordem temporal, ritmo, câmera travada, estado final desejado e restrições.

Cada prompt deve ser copiável isoladamente, com detalhes concretos do projeto. Não use apenas “igual ao anterior” ou campos em branco. Inclua instruções de quais arquivos anexar e a função de cada um, sem confundir referência de estilo com referência de geometria.

Não se limite a entregar uma estrutura quando o usuário pedir todos os prompts: preencha todos os frames e transições do plano. Se uma restrição do usuário impedir concluir, entregue o trabalho independente e identifique a pendência.

## 5. Executar quando solicitado

Use a ferramenta de imagem disponível respeitando suas regras e skills aplicáveis. Em edição, forneça a referência original e as imagens de continuidade pertinentes, em vez de recriar a cena apenas por texto. Em um fluxo de plataforma explicitamente escolhido pelo usuário, use as ferramentas dessa plataforma quando disponíveis.

Para Flow, confirme os controles e modos na interface atual ou documentação oficial antes de orientar a execução. Não presuma disponibilidade de End Frame, duração, modelo, número de referências ou custo. Não troque silenciosamente Start Frame por outro modo.

Em **Start Frame apenas**, o estado final do prompt é um alvo, não um vínculo visual garantido. Inspecione o último frame efetivo de cada clipe. Para encadear, use esse frame validado como início seguinte quando compatível com o plano, ou regenere o trecho se ele divergir. Não use um final com arquitetura deformada como nova referência-mestre. Quando o modo permitir e for escolhido, um frame final explícito pode ajudar, sem garantir fidelidade absoluta.

Não dispare lotes pagos ou tentativas sem limite. Use o limite autorizado; se não houver, uma geração inicial por item solicitado e, no máximo, uma correção direcionada de um item falho antes de relatar o bloqueio. Confirme orçamento somente quando necessário para executar além do escopo autorizado. Para mídia, usar a escolha do prompt atual do protocolo comum; não repetir a mesma autorização válida.

## 6. Revisão e entrega

Compare cada estática com a imagem-mestre e com os frames vizinhos. Verifique teto, palco, contorno do LED, perspectiva do piso, câmera, posição das mesas, continuidade de cadeiras e equipamento. Em vídeo, confira início, pontos intermediários e final; amostragem não equivale a revisão integral. Verifique que a ação decorre do trabalho da equipe e que o LED não modifica o ambiente.

Classifique cada item como **planejado**, **gerado não revisado**, **validado** ou **corrigir**, citando o desvio concreto. Bloqueie o uso como referência de um item com erro estrutural. Corrija a área afetada quando a ferramenta permitir; não aceite mudança de arquitetura como “melhoria estética”. Se a fidelidade exigida não for atingida, explique a necessidade de composição com fundo fixo, máscaras ou cena 3D original, conforme recursos disponíveis.

Entregue: contrato de continuidade; layout do jantar; tabela de frames e transições; todos os prompts estáticos; todos os prompts de animação; ordem de execução e anexos; relatório de revisão e arquivos efetivamente produzidos. Em pedidos só de planejamento, marque a validação visual como pendente de geração. Preserve o projeto e a mesma nomenclatura nas revisões; informe quais prompts e trechos posteriores são afetados por mudanças.
