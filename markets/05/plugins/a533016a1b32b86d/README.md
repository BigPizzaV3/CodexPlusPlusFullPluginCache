# Flav.IA — Fotos de Imóveis 0.3.1

Versão ampliada do plugin para preparação fotográfica, proteção de dados e criação de conteúdo imobiliário. Esta versão aplica a logo oficial aprovada da Flav.IA com a assinatura IAtiza.ai.

## Skills publicadas anteriormente

| Skill | Função |
|---|---|
| `flavia-fotos-imoveis` | normalização RNS-01 e APROVAR PADRÃO |
| `flavia-auditar-fidelidade` | comparação entre original e tratada |
| `flavia-privacidade-imobiliaria` | detecção e ocultação de dados pessoais |
| `flavia-curadoria-fotos` | seleção, capa, sequência e pendências |
| `flavia-copy-imobiliaria` | copy baseada em evidências |
| `flavia-coach-fotografico` | orientação para captura e refotografia |

## Skills novas desta versão

| Skill | Função e limite principal |
|---|---|
| `flavia-metadados-vistoria` | extrai EXIF disponível e monta ficha visual; não inventa data, hora ou localização e não certifica vistoria |
| `flavia-organizacao-seguranca` | revisa privacidade e preparação da cena; não remove móveis, bagunça ou defeitos para embelezar |
| `flavia-luz-natural` | planeja melhor horário e direção de captura com evidências; não relitiga a foto para falsificar o horário |
| `flavia-amplitude-enquadramento` | sugere distância, altura, lente e recorte; não cria paredes, janelas ou bordas inexistentes |
| `flavia-destaques-imovel` | identifica características visíveis e planeja closes; não afirma atributos não confirmados |
| `flavia-criativos-sociais` | cria posts, stories e carrosséis a partir de fotos aprovadas |
| `flavia-criativos-experiencia` | cria conceitos com pessoas ou elementos gerados, sempre rotulados como conceituais |
| `flavia-marca-identidade` | aplica logo e marca-d’água fornecidas depois da aprovação; não redesenha marcas |
| `flavia-otimizacao-anuncio` | analisa texto, fotos e link acessível; sinaliza quando o anúncio não pode ser lido |

## Regra de separação

Cada resposta deve declarar se é **F — factual**, **C — criativa conceitual** ou **P — planejamento**. Imagens factuais preservam a realidade do imóvel. Criativos conceituais não podem ser usados como registro, vistoria, anúncio de característica existente ou prova de condição.

## Estado da entrega

- Versão do pacote: `0.3.1`.
- Ícone e logo: substituídos pela logo oficial aprovada fornecida pelo proprietário do plugin.
- Validação estrutural: executar `scripts/validar.sh`.
- Avaliação das skills: obrigatória antes de publicar.
- Publicação: depende da submissão e aprovação da OpenAI.

