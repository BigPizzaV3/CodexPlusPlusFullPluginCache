# Negativas: semántica de match

### Las negativas no tienen close variants; las positivas sí
- **Tipo**: gotcha de plataforma
- **Por qué**: una negativa EXACT bloquea solo la cadena literal. La positiva del mismo texto sigue sirviendo plurales, tildes, erratas y reordenaciones.
- **Cómo detectarlo**: el 73% de las parejas negativa EXACT sobre positiva EXACT del mismo texto seguía con impresiones a 90 días.
- **Qué hacer**: clasificar la gravedad de un bloqueo así. La pérdida se mide en search terms que convertían, no en recuento de keywords.

  | Negativa | Positiva | Gravedad |
  |---|---|---|
  | PHRASE / BROAD | EXACT o PHRASE | Total |
  | EXACT | cualquiera | Literal |
  | PHRASE / BROAD | BROAD | Parcial |

- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026.

### La negativa no pliega acentos ni símbolos
- **Tipo**: gotcha de plataforma
- **Por qué**: Google trata el acento como variante cercana, y las negativas no casan variantes. Una negativa con tilde no bloquea la query sin tilde, ni al revés.
- **Cómo detectarlo**: una keyword siguió sirviendo con una lista aplicada que solo coincidía al quitar acentos.
- **Qué hacer**: subir cada raíz con tilde y sin tilde. En herramientas propias, normalizar acentos para buscar candidatas, pero decidir el bloqueo sobre el texto original.
- **Evidencia**: Visto en 2-3 cuentas, ago-nov 2026.

### Una negativa PHRASE bloquea palabras completas, no subcadenas
- **Tipo**: gotcha de plataforma
- **Por qué**: las marcas se escriben pegadas ("marcashop", "mimarca") o en forma corta. Una negativa sobre la forma canónica no toca esos tokens.
- **Cómo detectarlo**: agrupar los search terms por regex de marca, no por igualdad con la negativa existente. En un caso con las negativas de marca solo en forma canónica, casi la mitad del gasto entró por marca.
- **Qué hacer**: negativizar el token raíz y las variantes pegadas que aparezcan en el informe. Antes, verificar colisiones con positivas del ámbito.
- **Evidencia**: Visto en 1 cuenta, ago 2026.
