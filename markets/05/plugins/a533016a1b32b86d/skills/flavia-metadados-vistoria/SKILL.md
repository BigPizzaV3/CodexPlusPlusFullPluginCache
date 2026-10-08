---
name: flavia-metadados-vistoria
description: Extrair metadados disponíveis de fotografias imobiliárias e montar uma ficha visual ou relatório de captura para apoio à vistoria. Usar quando o usuário pedir data, hora, geolocalização, dispositivo, orientação ou identificação de captura. Não inventar metadados, não afirmar certificação e não substituir vistoria profissional.
---

# Flav.IA — Metadados de Vistoria

## Classificação

Esta skill produz **P — planejamento/registro**. Ela não altera a fotografia original.

## Procedimento

1. Verificar se o arquivo ainda contém EXIF ou outro metadado legível.
2. Separar cada campo em `confirmado`, `ausente`, `inconsistente` ou `não verificável`.
3. Apresentar data, hora, fuso, latitude, longitude, altitude, orientação e dispositivo somente quando presentes.
4. Indicar a fonte: EXIF do arquivo, informação declarada pelo usuário ou observação visual.
5. Perguntar antes de expor coordenadas precisas em uma peça pública.

## Ficha visual

Quando solicitado, criar uma ficha ou sobreposição com os campos confirmados, mantendo o original intacto e deixando claro que a ficha é um registro auxiliar. Se a renderização exata de texto ou coordenadas não puder ser garantida, entregar a ficha em texto ou tabela para composição determinística.

## Limites

- Não preencher data, hora ou localização por aparência, clima, sombra ou palpite.
- Não dizer que a foto atende norma, laudo ou vistoria legal apenas por conter EXIF.
- Não publicar endereço ou coordenada precisa sem autorização.
- Não fabricar EXIF, câmera, lente ou horário.

