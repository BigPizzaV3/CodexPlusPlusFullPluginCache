# Fontes consultadas e critérios de interpretação

Síntese inicial preparada em 17/09/2026 e ampliada em 20/09/2026. As páginas abaixo correspondem às páginas do PDF, contando a primeira como 1. Foram consultados os textos extraídos dos PDFs; conteúdo exclusivamente visual não integra esta síntese. Não foram copiadas listas de contatos nem dados de participantes.

## Documentos do CapelanIA

Pasta: `F:\Cola IA\CapelanIA`.

| Arquivo | Uso nesta skill |
|---|---|
| `ESPECIFICACAO-E-PROMPT-MESTRE.md` | Identidade, duas camadas espirituais, diagnóstico, 4 Qs, estrutura da minuta e limites éticos |
| `AMPLIACAO-SOCIOEMOCIONAL-RELACIONAL-E-MISSIONARIA.md` | Cinco domínios socioemocionais, matriz, amizade genuína, infância, trilhas missionária e híbrida |
| `PACOTE-DE-PUBLICACAO.md` | Nome público, iniciadores e cenários de revisão; orientações de publicação de GPT/site não são ações desta skill |

O prompt local recomenda confirmações a cada etapa. Aqui isso foi adaptado para confirmar decisões substantivas e aproveitar autorização já dada; pedidos explícitos de minuta completa podem ser atendidos com hipóteses e pendências. Mantém-se revisão humana antes da execução institucional.

## Materiais do Curso Básico/Auxiliar

Pasta de origem:

`F:\Cola IA\Minha Inteligencia IA Cola\Segundo Cerebro\2. Áreas\Trabalho Missionário MPC\Capaz\Curso Basico de Capelania Escolar`

| Arquivo | Localização | Conteúdo aproveitado |
|---|---|---|
| `CURSO AUXILIAR 2023.pptx.pdf` | 125 páginas; pp. 70–71 | Integração à escola, respeito à consciência, limites de sigilo e encaminhamentos |
| Mesmo arquivo | pp. 85–94 | Proteção, escuta de relato espontâneo, não pedir detalhes, visibilidade com privacidade e órgãos de proteção |
| Mesmo arquivo | pp. 99–106 | Projeto, 4 Qs na p. 101, mobilização de recursos e roteiro operacional |
| `APOSTILA Curso básico de Capelania Escolar MPC BRASIL .pdf` | 7 páginas; pp. 2–4 | Cuidado integral, comunidade escolar, respeito institucional, limites de atuação e oração com consentimento |
| Mesma apostila | pp. 5–7 | Recursos, objetivos, atividades, avaliação, roteiro e construção de confiança na escola |
| `Código de Ética e Conduta da Capelania Escolar da MPC Brasil.pdf` | 1 página; itens 1–7, 10–15 | Vida devocional, formação, cuidado da equipe, respeito, competência, autorização de uso do nome MPC e comunicação de ausências |

As sínteses são paráfrases operacionais, não transcrições nem uma declaração de aprovação institucional desta skill. Para citar literalmente, reabra o arquivo e confira o trecho.

## Tensões e limites das fontes

- A apostila contém linguagem evangelística e propostas confessionais. Interprete-as junto do consentimento, da liberdade religiosa e das duas camadas do CapelanIA; não trate sugestões de culto como autorização universal para escolas.
- O item 8 do Código trata de críticas/denúncias entre capelães e menciona elementos comprobatórios e testemunhas. Não o aplique para bloquear comunicação de suspeita de violência contra menores. Proteção e obrigações legais não aguardam investigação própria.
- O curso orienta comunicação à direção em casos especiais. Isso não significa que só a direção possa acionar proteção externa, nem que comunicação interna satisfaça todo dever legal.
- A apostila menciona identificar alunos cristãos. Esta skill não transforma isso em coleta de religião, lista de alvos ou reaproveitamento de contatos escolares.
- A prudência interpessoal da apostila é ampliada aqui para todas as relações, independentemente de gênero, com supervisão e limites de papel.
- A referência de proteção complementa o curso com critérios de minimização de dados, risco familiar e comunicação legal; esses acréscimos não devem ser atribuídos literalmente ao material de 2023.
- As referências à BNCC e ao CASEL vêm da ampliação local. Confira documentos primários antes de citar redação oficial ou afirmar alinhamento normativo formal. Não invente códigos de habilidades da BNCC.
- Não foi identificada entre os três PDFs usados uma política completa comprovadamente vigente de proteção nem um modelo institucional com aprovação atual. Registre-os como pendências para execução quando pertinentes.

## Verificação complementar

As fontes oficiais consultadas para esclarecer proteção e distinguir capelania de Ensino Religioso estão vinculadas em [proteção e liberdade](protecao-e-liberdade.md). Leis municipais, dados territoriais, contatos e políticas institucionais precisam de verificação no contexto de cada projeto. A antiguidade de um curso não comprova vigência normativa.

Em divergências, explicite o ponto e preserve direitos, proteção e normas aplicáveis. Mantenha a contribuição institucional identificada sem elevar o curso a autoridade jurídica ou atribuir a autores ideias não verificadas.

$ErrorActionPreference = 'Stop'
$root = 'F:\Cola IA\CapelanIA\publicacao-v1.1\capelania-projetos'
$utf8 = New-Object System.Text.UTF8Encoding($false)

function Replace-Exact([string]$path, [string]$old, [string]$new) {
    $text = [IO.File]::ReadAllText($path)
    if (-not $text.Contains($old)) { throw "Trecho nao encontrado em $path" }
    [IO.File]::WriteAllText($path, $text.Replace($old, $new), $utf8)
}

$manifest = Join-Path $root '.codex-plugin\plugin.json'
Replace-Exact $manifest '"version": "1.0.0"' '"version": "1.1.0"'

$skill = Join-Path $root 'skills\orientar-projetos\SKILL.md'
$oldStep = '4. Conecte espiritualidade, competências socioemocionais e presença relacional à necessidade. Para encontros e matriz, leia [pedagogia e relacionamentos](references/pedagogia-e-relacionamentos.md).'
$newStep = '4. Conecte espiritualidade, competências socioemocionais e presença relacional à necessidade. Para encontros e matriz, leia [pedagogia e relacionamentos](references/pedagogia-e-relacionamentos.md). Para fundamentação da missão, vocação e Reino, leia [missiologia bíblica e vocação](references/missiologia-biblica-e-vocacao.md). Para leitura cultural e postura relacional, leia [contextualização, escuta e pontes](references/contextualizacao-escuta-e-pontes.md). Para ações urbanas e cooperação, leia [desenvolvimento comunitário e parcerias](references/desenvolvimento-comunitario-e-parcerias.md).'
Replace-Exact $skill $oldStep $newStep

$oldPublic = '**Expressão pública:** explique como o valor será vivido no serviço. Não presuma fé compartilhada. Oração, leitura bíblica e anúncio cristão explícito dependem do contexto, das normas aplicáveis, das autorizações e de participação livre. A autorização da direção não substitui consentimento nem supera direitos de consciência.'
$newPublic = $oldPublic + "`r`n`r`nMateriais missionários confessionais podem orientar igrejas, equipes e atividades de adesão livre. Não transfira métodos de evangelização, discipulado, identificação de “pessoas de paz” ou formação de grupos para escolas, benefícios assistenciais ou relações de cuidado sem análise do contexto, transparência, consentimento e alternativa real. Nunca trate vulnerabilidade, infância, ajuda material ou amizade como oportunidade de pressão religiosa."
Replace-Exact $skill $oldPublic $newPublic

$sources = Join-Path $root 'skills\orientar-projetos\references\fontes.md'
$text = [IO.File]::ReadAllText($sources)
$text = $text.Replace('Síntese preparada em 17/09/2026.', 'Síntese inicial preparada em 17/09/2026 e ampliada em 20/09/2026.')
$append = @'

## Ampliação missionária de 2026

Pasta de origem: `F:\Cola IA\CapelanIA\Novas Bases`.

Foram inventariados 55 arquivos: 17 DOCX, 23 PDFs, 11 PPTX, 3 vídeos e 1 ZIP. A extração inicial recuperou texto de 44 arquivos. Seis DOCX compostos principalmente por imagens e três vídeos ficaram fora da síntese textual; o ZIP foi apenas catalogado. Arquivos temporários do Word foram ignorados.

| Conjunto | Uso nesta versão |
|---|---|
| “Deus está em missão”, “O Evangelho do Reino” e Perspectivas | Missão como iniciativa de Deus, bênção às nações, Reino e envio |
| Materiais de vocação | Discernimento de chamado, dons, limites e prestação de contas |
| “Construindo Pontes” e Lições 8 e 9 | Humildade cultural, escuta, contextualização e reciprocidade |
| Desenvolvimento Comunitário Cristão e Lição 10 | Transformação integral, leitura comunitária e serviço |
| EMU, Lição 7 e materiais de estratégia | Leitura territorial, planejamento e projetos urbanos |
| Lição 12 e materiais de parceria | Cooperação, papéis e sustentabilidade |
| Guia da Equipe Alpha | Facilitação de conversa em ambiente confessional voluntário |
| Materiais de discipulado | Uso restrito a ambientes confessionais de adesão livre |

Os guias de Perspectivas e o Guia da Equipe Alpha informam direitos autorais. Esta skill contém sínteses operacionais e referências de localização, não reproduções integrais. Confirme autorização antes de redistribuir originais ou copiar trechos extensos.

### Limites específicos

- Verifique estatísticas missionárias, religiosas e etárias em fontes primárias atuais antes de usá-las.
- Confira na obra original as ideias e citações atribuídas a autores.
- Reformule linguagem de “alvo”, “campo fértil”, “pessoa de paz” e “alcançar” em projetos públicos para preservar dignidade, agência e liberdade de consciência.
- Materiais de evangelização infantil não autorizam pressão sobre crianças. Aplique proteção, consentimento, assentimento e adequação etária.
- Discipulado e convite religioso só cabem em ambientes transparentemente confessionais e voluntários. Não condicione amizade, serviço ou benefício à participação religiosa.
- Cronogramas, propostas pessoais e orientações administrativas servem como contexto histórico, não como políticas vigentes.
'@
[IO.File]::WriteAllText($sources, $text.TrimEnd() + "`r`n" + $append.TrimStart(), $utf8)

$test = Join-Path $root 'skills\orientar-projetos\references\teste.tmp'
if (Test-Path -LiteralPath $test) { Remove-Item -LiteralPath $test }

Write-Output 'Atualizacao v1.1 aplicada.'

