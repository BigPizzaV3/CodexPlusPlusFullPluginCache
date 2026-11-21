---
name: google-ads-account-context
description: "Crea o actualiza account-context.md, el fichero de contexto de una cuenta de Google Ads (negocio, objetivos, buckets de campañas, contrato de medición, marca y reglas de copy). Usar al empezar a trabajar con una cuenta nueva, cuando no existe account-context.md, o cuando el usuario pide revisar el contexto tras un cambio grande."
---

# Contexto de una cuenta

Esta skill crea `account-context.md` para una cuenta de Google Ads. Con ese fichero, las demás skills del paquete trabajan sabiendo qué vende el negocio, qué cuenta como éxito y qué no se puede tocar. Sigue los pasos en orden.

## 1. Leer la cuenta primero

Si tienes acceso a la cuenta (servidor MCP, API o exportaciones), léela antes de preguntar nada. Todo en solo lectura:

- **Campañas activas** con su tipo de canal y su gasto de 30 días: `campaign.status`, `campaign.primary_status`, `campaign.advertising_channel_type`, `metrics.cost_micros`.
- **Estrategias de puja y targets**: `campaign.bidding_strategy_type`, `campaign.bidding_strategy` y los campos de target. Si la campaña usa portfolio, el target de campaña sale 0 y hay que leerlo en `accessible_bidding_strategy` (regla "Con portfolio, el target de la campaña sale 0").
- **Acciones de conversión**: `conversion_action.name`, `category`, `primary_for_goal`, `counting_type`, `status`, y el nivel de objetivo de cada campaña en `conversion_goal_campaign_config`.
- **Términos de marca**: los que aparecen en nombres de campaña y en keywords de campañas de marca.
- **Mercados e idiomas**: criterios `LOCATION` y `LANGUAGE` de las campañas activas, y `customer.currency_code`.

Resume lo encontrado en pocas líneas y pide al usuario que lo confirme o lo corrija. Lo que el usuario corrija manda sobre lo leído.

Si no hay acceso, dilo y pasa al paso 2 con todas las preguntas.

## 2. Preguntar solo lo que falta

Haz las preguntas en bloques de 3 o 4 y espera la respuesta antes del siguiente bloque. Salta las que ya respondió la lectura. Un bloque se puede dejar a medias: lo que quede sin respuesta va a preguntas abiertas.

- **Negocio**: qué vende la empresa, web, modelo de negocio y moneda de la cuenta.
- **Objetivos**: presupuesto mensual, KPI de negocio principal y dónde se mide, CPA o ROAS objetivo, y cómo es un buen mes.
- **Reglas**: términos de marca, competidores por los que se puede o no se puede pujar, claims que no se pueden hacer en anuncios, tono de voz, y qué no se cambia nunca sin preguntar.
- **Medición**: qué acción de conversión es el KPI real, si la puja usa otra distinta, y cuánto tardan en llegar las conversiones.

## 3. Escribir el fichero

Copia `templates/account-context.md` y rellénalo. Reglas:

- Escribe `account-context.md` en la carpeta de trabajo del usuario, salvo que pida otra ruta. Si gestiona varias cuentas, una carpeta por cuenta con su propio fichero.
- Los buckets (Brand, NonBrand, PMax, Demand Gen, App) se definen por ID de campaña y tipo de canal, no por nombre.
- Separa lo que viene de la cuenta de lo que dijo el usuario. Lo que nadie confirmó va a preguntas abiertas, no se rellena con suposiciones.
- Pon la fecha de la última revisión.

## 4. Cerrar

Dile al usuario:

- dónde está el fichero;
- que las demás skills lo leen antes de trabajar con la cuenta;
- que conviene revisarlo cada mes y después de cualquier cambio grande (objetivo, presupuesto, conversión de puja, estructura);
- que el fichero se queda en su máquina y, si usa git, debe ir en el `.gitignore`.
