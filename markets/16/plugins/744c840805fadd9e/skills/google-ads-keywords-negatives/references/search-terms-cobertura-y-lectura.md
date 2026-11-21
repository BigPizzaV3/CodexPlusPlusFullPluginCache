# Search terms: cobertura y lectura

### Microsoft Ads no oculta search terms por umbral
- **Tipo**: gotcha de API
- **Por qué**: el detalle de términos suma el 100% del total, a diferencia de Google.
- **Cómo detectarlo**: sumar el informe de términos contra el total de campaña.
- **Qué hacer**: usar Bing como contraste de composición de intención cuando Google revela poco. Al importar campañas de Google, revisar pujas antes de encender: arrastran los CPC de Google (8 veces los nativos en un caso).
- **Evidencia**: Visto en 1 cuenta, ago 2026.

### Un match literal en español falla por flexión, orden y erratas
- **Tipo**: error de método
- **Por qué**: "zapatilla de running" en la lista no casa "zapatillas de running". "Barata" no casa "barato". La marca con orden de palabras invertido o con errata cae fuera de marca.
- **Cómo detectarlo**: términos marcados irrelevantes que contienen una entrada de la lista en otra forma. Una keyword non-brand con CPA muy por debajo de su bloque suele ser fuga de marca.
- **Qué hacer**: generar plural y género de cada entrada (cambio de género solo desde 4 letras). Añadir regex de erratas y orden invertido de la marca. Cruzar además contra las keywords que sirven en la campaña de marca.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026.
