---
name: google-ads-setup
description: "Guía para montar desde cero un agente que trabaje con Google Ads de forma segura. Usar cuando alguien quiere empezar a usar un agente (Claude Code, Codex, Cursor u otro) con su cuenta de Google Ads, no sabe cómo conectarlo, o pregunta cómo instalar estas reglas o comprobar que la conexión funciona."
---

# Montar un agente para Google Ads

Esta guía sirve para quien nunca ha trabajado con un agente sobre Google Ads. Al terminar, el agente lee la cuenta, no puede cambiar nada sin permiso y conoce estas reglas. Información comprobada en noviembre de 2026: las opciones de acceso cambian a menudo, así que revisa los enlaces oficiales antes de empezar.

## Qué necesitas

Necesitas dos cosas: un harness de agente y una forma de que lea Google Ads.

El harness principal es Claude Code. Codex, Cursor y otros agentes que leen ficheros `SKILL.md` también sirven con estas reglas.

Para que el agente lea la cuenta hay tres opciones oficiales:

- **Exportaciones de la interfaz.** Descargas una tabla de Google Ads en CSV o Google Sheets, o programas el informe para que llegue por correo, y se la das al agente. No hace falta configurar nada. Guías de Google: [descargar y programar informes](https://support.google.com/google-ads/answer/2404176) y [gestionar informes](https://support.google.com/google-ads/answer/6201327).
- **Servidor MCP oficial de Google Ads.** Google publica un servidor MCP de código abierto ([guía](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server), [repositorio](https://github.com/googleads/google-ads-mcp)). El agente lanza consultas a la cuenta en directo. Necesita un proyecto de Google Cloud con la Google Ads API activada, un cliente OAuth, `gcloud`, Python 3.10+ y `pipx`. Desde la versión 0.0.6 puede crear assets y gestionar etiquetas, así que hay que configurarlo en solo lectura (más abajo).
- **Google Ads API directa**, con la [librería cliente](https://developers.google.com/google-ads/api/docs/client-libs). Es la opción más completa y la que más código pide. Google retiró los developer tokens el 9 de septiembre de 2026: el nivel de acceso va ahora en el proyecto de Google Cloud ([niveles de acceso](https://developers.google.com/google-ads/api/docs/api-policy/access-levels)). Una cuenta real necesita nivel Explorer o superior; con el nivel Test solo se leen cuentas de prueba.

En el momento de escribir esto, Google no ofrece un conector alojado para Google Ads: el servidor MCP lo ejecutas tú.

Si no programas, empieza con exportaciones. Cuando quieras que el agente lea la cuenta en directo, el servidor MCP oficial es la vía más sencilla. Es posible que necesites ayuda técnica una vez, para el proyecto de Google Cloud y el cliente OAuth.

## Empieza en solo lectura

Hasta que el equipo confíe en el montaje, el agente no muta nada. Un agente que lee mal una cifra produce un informe equivocado, pero uno que escribe mal cambia la cuenta.

- Con el servidor MCP, crea un `tools_config.yaml` que solo active lectura y apúntalo con `GOOGLE_ADS_MCP_TOOLS_CONFIG`:
  ```yaml
  namespaces:
    customers: true
    search: true
    metadata: true
    labels: false
    assets: false
  ```
- Para conectarlo a Claude Code (`GOOGLE_ADS_LOGIN_CUSTOMER_ID` solo hace falta si entras desde una cuenta de administrador):
  ```
  claude mcp add google-ads -e GOOGLE_CLOUD_PROJECT=<proyecto> -e GOOGLE_ADS_MCP_TOOLS_CONFIG=<ruta>/tools_config.yaml -e GOOGLE_ADS_LOGIN_CUSTOMER_ID=<id_administrador> -- pipx run --spec google-ads-mcp==0.0.6 google-ads-mcp
  ```
- Con el servidor MCP o con la API directa, autoriza la conexión con un usuario de Google Ads que tenga acceso de solo lectura. Así, un error de configuración tampoco permite cambios.
- Cuando más adelante quieras dar escritura, cada cambio pasa antes por `validate_only` y espera un OK explícito de una persona que haya visto el diff. Está en las reglas de [seguridad de mutaciones](../google-ads-api-gotchas/references/seguridad-de-mutaciones.md): "Dry-run por defecto y apply solo tras revisar el diff" y "El dry-run tiene que validar contra el servidor".

## Instalar estas reglas

En Claude Code:

```
/plugin marketplace add fieradigital/fiera-google-ads-rules
/plugin install fiera-google-ads-rules@fiera-google-ads-rules
```

En otro agente que lea `SKILL.md`, copia la carpeta `skills/` en su directorio de skills.

## Comprobar que funciona

Pide al agente que liste las campañas activas con su gasto de los últimos 30 días. Por debajo debe lanzar una consulta como esta:

```sql
SELECT campaign.id, campaign.name, campaign.advertising_channel_type, metrics.cost_micros
FROM campaign
WHERE campaign.status = 'ENABLED' AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

El gasto viene en micros: divide entre 1.000.000. Compara el total con la interfaz de Google Ads para la misma ventana. Si cuadra, la conexión funciona. Si trabajas con exportaciones, haz la misma comprobación con un CSV de campañas.

## Privacidad

- El fichero de contexto de la cuenta (`account-context.md`, lo crea la skill `google-ads-account-context`) se queda en tu máquina.
- Si usas git, añade `account-context.md`, las exportaciones y las credenciales al `.gitignore`.
- No pegues Customer IDs, nombres de campaña ni datos de clientes en sitios públicos: issues, foros o chats abiertos.
