# Logs, encerramento e recebimento

Os diagnósticos são do segundo turno de 2026, Brasil sem exterior.

- `arvor_eleicoes_timeline`: `offset` e `limite` (1–3). Para a série inteira,
  siga `proximo_offset` até null, incluindo o dia seguinte. Há intervalos
  irregulares: não presuma que linhas vizinhas distam uma hora.
- `arvor_eleicoes_indicadores`: `tema` = `relogios` ou `transmissao`,
  `offset`, `limite` (1–20). Retorna metodologia, cobertura e sinais.
  A lista de transmissão é um ranking de destaques, não todos os locais.
- `arvor_eleicoes_local`: `tema`, `uf` (sem ZZ), `municipio` TSE,
  `zona`, `local`, `offset`, `limite`. Consulte pela chave completa.
  Ausência na lista de sinais não demonstra ausência de problemas no local.

Separe três processos: eventos de voto nos logs; encerramento registrado no BU;
recebimento pelo TSE. Recebimento não é o início da transmissão. O intervalo
encerramento→recebimento inclui etapas operacionais, preparação/transporte e
comunicação; não mede apenas latência da rede nem identifica sua causa.

A timeline está normalizada para Brasília (`America/Sao_Paulo`, UTC−3).
Campos terminados em `_local` nos dados brutos conservam o horário local:
não os compare diretamente sem verificar fuso e data. Não aplique conversão
dupla a uma série já normalizada. Leia limites de intervalo e cobertura do
payload antes de rotular um ponto como exato ou como faixa.

Não some valores acumulados. Para incrementos, use os campos do intervalo
ou a diferença entre acumulados consecutivos do mesmo universo. Para ritmo,
considere a duração irregular das faixas. Na apresentação, distinga número
de votos, número de seções, incrementos e acumulados.

Leia a cobertura dos logs e os critérios de exclusão dos relógios antes de
comparar eventos com comparecimento. Diferença entre esses totais não equivale
a votos perdidos ou alterados. Evento de voto não informa o candidato escolhido.
Sinais de relógio não significam automaticamente todos os logs sem relógio
confiável: use a definição e as categorias retornadas, incluindo sem vínculo
e sem log. Comparações por modelo de urna exigem denominadores por modelo;
uma concentração de contagens, sozinha, não mede maior risco.
