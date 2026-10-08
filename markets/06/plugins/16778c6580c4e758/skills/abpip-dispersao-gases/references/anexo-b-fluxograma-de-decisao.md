# Anexo B - fluxograma de decisão

Interpretação textual conferida visualmente do Anexo B. Localizador: [Anexo B, pp. 48-49; PDF p. 25].

## Etapa 1 - verificar gatilhos

O fluxograma começa com três ramos independentes:

```text
Há descarga para a atmosfera por vent, dispersor ou PSV?
  Sim -> desenvolver o estudo
  Não -> fim deste ramo

A avaliação semiquantitativa apresentou meta de cobertura >= 60%?
  Sim -> desenvolver o estudo
  Não -> fim deste ramo

A corrente oleosa ou gasosa contém H2S >= 100 ppm, indicado como IDLH?
  Sim -> desenvolver o estudo
  Não -> fim deste ramo
```

Qualquer resposta `Sim` converge para a Etapa 2. Os três testes correspondem aos gatilhos do capítulo 3; não some nem combine os valores.

## Etapa 2 - desenvolver o estudo

```text
Desenvolver estudo para gases inflamáveis e/ou tóxicos
conforme o objetivo da demanda
  |
  v
Obter os resultados das simulações computacionais
```

O Anexo B não detalha dados ou método nessa caixa. Para isso, use [desenvolvimento-do-estudo.md](desenvolvimento-do-estudo.md).

## Etapa 3 - interpretar os resultados e posicionar

### Ramo de área sensível

```text
A nuvem, na concentração de interesse, atinge alguma área sensível?
  Não -> fim deste ramo
  Sim -> posicionar detectores para proteção da área sensível,
         pelo monitoramento do trajeto e do receptor
```

### Ramo de área de processo ou congestionada

```text
O resultado da dispersão pode gerar a nuvem de interesse?
  Não -> fim deste ramo
  Sim -> posicionar detectores para proteção da área de processo
         e/ou congestionada, por monitoramento volumétrico
           |
           v
         Os posicionamentos atendem à meta de cobertura do Anexo A?
           Não -> revisar o posicionamento e verificar novamente
           Sim -> prosseguir para a Etapa 4
```

Os dois ramos convergem para a configuração do sistema quando aplicáveis. O fluxograma não fornece coordenadas nem quantidade universal de detectores.

## Etapa 4 - configurar o sistema

Configurar conforme a filosofia de segurança da operadora, incluindo:

- níveis de alarme e respostas operacionais;
- ações de mitigação;
- lógicas de votação;
- comissionamento e testes de aceitação do sistema.

Depois dessa etapa, o fluxograma termina.

## Limite de interpretação

`Fim` encerra somente o caminho representado. Não significa, isoladamente, que um estudo, detector ou medida de segurança seja dispensável sob outra análise de risco, norma, regulamento ou diretriz da operadora. Se os dados forem ausentes ou conflitantes, não escolha um ramo por presunção.
