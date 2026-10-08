# onboarding-wins

Plugin local para convertir una investigación de onboarding de Zendesk en un JSON listo para importar en Onboarding Wins.

## Flujo para cada coworker

1. Trabajar en ChatGPT Work con acceso `Local`.
2. Tener Gmail conectado y Chrome abierto con la sesión corporativa de Gong, Salesforce y View 360.
3. Invocar `onboarding-wins` con la cuenta, el CSM y el rango mensual.
4. Copiar únicamente el JSON final.
5. Abrir la app Onboarding Wins, elegir `Importar caso`, validar y después importar.

El plugin conserva las limitaciones de acceso, normaliza ARR, permite `null` para datos no verificables y no marca una CSQL sin evidencia comercial explícita.

## Validación local opcional

```bash
node scripts/validate_payload.js payload.json
```

La app sigue siendo la fuente compartida de datos. El plugin no escribe directamente en la hoja: genera el objeto que la app valida y guarda con el usuario autenticado.
