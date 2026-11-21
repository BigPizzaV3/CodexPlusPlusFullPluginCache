# Copy y RSAs: medir

### Las métricas por asset de un RSA se multiplican; usa ratios dentro del anuncio
- **Tipo**: error de método
- **Por qué**: cada impresión sirve 2-3 headlines y 1-2 descriptions, y todos anotan impresión, clic y conversión. La suma da 2,4-3,4x el total del anuncio en headlines.
- **Cómo detectarlo**: sumar métricas de assets y comparar con `ad_group_ad`.
- **Qué hacer**: comparar solo ratios entre pares del mismo anuncio. Los pineados quedan fuera: el pin fuerza su cuota.
- **Evidencia**: Visto en 1 cuenta, ago 2026.

### Un asset con poco serving no es un asset a reescribir
- **Tipo**: error de método
- **Por qué**: el anuncio mediano concentra el 80% del serving en 5 de 17 headlines. Así funciona un RSA. Con 15 headlines, alguno sale con CTR bajo por azar.
- **Cómo detectarlo**: contar cuántos assets marca el test frente a los esperados por azar (2,5% con z ≤ -1,96).
- **Qué hacer**: solo entran a worklist los assets que Google sirve y pierden mientras sirven. Un asset con CPA igual o mejor que su ad group nunca entra en la worklist.
- **Evidencia**: Visto en 2-3 cuentas, ago 2026.

### Un cambio de copy no se lee antes de 2-4 semanas, y Google puede no servirlo
- **Tipo**: error de método
- **Por qué**: el asset nuevo tarda en acumular serving. En una ronda, Google apenas sirvió los textos nuevos.
- **Cómo detectarlo**: impresiones del asset nuevo frente a sus pares a 2 y 4 semanas.
- **Qué hacer**: fijar la fecha de lectura al aplicar. No leer el CTR del ad group antes.
- **Evidencia**: Visto en 2-3 cuentas, sep-oct 2026.

### Las conversiones por asset son participación, no lift aislado
- **Tipo**: error de método
- **Por qué**: todos los assets servidos en un clic convertidor reciben la conversión. El pin sesga más la lectura.
- **Cómo detectarlo**: n/a.
- **Qué hacer**: usar `metrics.conversions` y `cost_micros` de `ad_group_ad_asset_view` para ordenar dentro del anuncio, nunca para sumar ni atribuir.
- **Evidencia**: Visto en 4+ cuentas, abr 2026.
