# Duckhunt para Codex y ChatGPT

Plugin para consultar el inbox, organizar tareas, retomar trabajo con sus work
notes y revisar tiempo, flujo y actividad con Insights. Reutiliza el servidor MCP
de Duckhunt por HTTP y OAuth: la identidad y el espacio los decide la autorización
del usuario. No necesita arrancar este repo, acceder a SQLite ni instalar las
dependencias de la aplicación.

Las skills son el catálogo estándar de workflows del servidor, el mismo que sirve
como prompts MCP (`/mcp__duckhunt__<nombre>` en Claude Code):

- `brief`: qué necesita atención hoy, sin cambiar nada.
- `triage`: tría del inbox (reclamar, adjuntar, posponer, marcar visto).
- `work`: empezar o retomar una tarea (`t#N`) o el trabajo de un entry (`e#N`).
- `review`: revisar un pull request ingerido (`e#N`).
- `close`: cerrar una tarea con su handoff, sus huecos del atlas y su estado final.
- `capture`: capturar trabajo como tarea sin duplicar.
- `record`: registrar como tarea el trabajo ya hecho en la conversación (entries, rama, handoff y estado).
- `daily`: previsualizar y escribir la daily note.
- `time`: revisar el tiempo registrado y su sincronización con Tempo.
- `handoff`: pasar esta conversación a un agente de duckhunt en la máquina del usuario (nueva o el siguiente turno de `r#N`).
- `takeover`: traerse una conversación de un agente de duckhunt (`r#N`) para seguirla aquí.

**No se editan a mano**: se generan desde `packages/api/src/services/mcp-workflows.ts`
y un test de deriva las fija. Tras cambiar el catálogo, regenera desde la raíz del
repo con `UPDATE_PLUGIN_SKILLS=1 pnpm --filter @duckhunt/api exec tsx --test
src/services/mcp-workflow-skills.test.ts` (borra también las carpetas que sobran).

El código de las tools y sus permisos sigue en `packages/api/src/mcp/server.ts`;
el plugin añade instrucciones de uso, no otra implementación de la API.

## Insights

`duckhunt-insights` consulta las mismas vistas que `/insights`, sin modificar
datos. Su argumento obligatorio `view` elige el contenido:

| `view` | Contenido |
| --- | --- |
| `summary` | Trabajo terminado y creado, tiempo, coste de agentes e inbox, con series y comparación con el periodo anterior. |
| `findings` | Hallazgos que necesitan atención, sin los descartados por el usuario. |
| `time` | Tiempo por día, tarea y repo, código sin atribuir, reuniones y Tempo. |
| `flow` | Tiempo de ciclo, antigüedad del trabajo abierto, esperas por estado y tareas reabiertas. |
| `agents` | Runs, coste, modelos, utilidad de reglas, preguntas, esperas de permisos y ocupación de máquinas. |
| `sources` | Volumen y tría por fuente, items repetidos y posibles reglas de silencio contrastadas con los últimos 30 días. |

Los argumentos opcionales son `period` (`day`, `week`, `month` o `quarter`;
por defecto `week`), `anchor` (un día `YYYY-MM-DD` dentro del periodo; hoy para
`day`, ayer para el resto) y `scope` (`workspace`, el espacio conectado, por
defecto; `all`, todos los espacios propios). El tiempo siempre pertenece a la
persona que consulta; el alcance del tablero sigue `scope`. La comparación de
un periodo en curso usa el tramo equivalente del anterior.

Ejemplo de lectura: `duckhunt-insights {"view":"summary","period":"week","anchor":"2026-10-19","scope":"workspace"}`.
Para investigar el detalle horario, `view=time` admite `blocks=true`; por defecto
no incluye los bloques y un trimestre nunca los devuelve. Los totales ya
descuentan solapamientos: no sumes señales crudas para reconstruirlos.

Insights es una tool del servidor disponible con el plugin; las once skills
anteriores siguen siendo el catálogo de workflows generado.

## Otras tools del servidor

Las automatizaciones publican una tool de creación y otra de edición por acción:
`duckhunt-automation-create-<acción>` y `duckhunt-automation-update-<acción>`, con
los sufijos `attach-entry`, `create-task`, `update-tasks`, `archive-tasks`,
`suppress-event`, `notify`, `investigate` y `run-prompt`. Cada una publica su schema
completo y sus annotations en `tools/list`; `action` contiene solo los campos de
esa acción, sin un selector `type` ni una lista arbitraria de operaciones.

Estas tools sustituyen a `duckhunt-automation-create` y `duckhunt-automation-update`.
Las reglas existentes se conservan; las que combinan varias acciones se editan en
la web. `duckhunt-automation-list` solo lee reglas; el historial se consulta con
`duckhunt-automation-runs {id}` en lugar de `includeRuns`. Las reglas que lanzan
agentes se siguen guardando desactivadas y se habilitan desde Duckhunt.

`duckhunt-tempo-log-worklog` publica el mínimo real de 60 segundos enteros y sus
formatos de fecha/hora. Cada llamada crea un worklog nuevo en Tempo: un resultado
incierto se comprueba con el listado antes de reintentar. Estos cambios del MCP
requieren desplegar el servidor y refrescar su catálogo en el cliente; regenerar
el ZIP del plugin no despliega el servidor ni resuelve su revisión externa.

`plugin.json` y `mcp.json` son los manifiestos portables. `.codex-plugin/plugin.json`
y `.mcp.json` conservan la compatibilidad local; identidad, versión y presentación
comunes se mantienen sincronizadas. El soporte y la información de revisión van
en `extensions.com.openai` del manifiesto portable porque el formato local anterior
no admite esos campos.

## Conexión

La configuración portable de [`mcp.json`](mcp.json) usa `streamable-http` y la
compatible de [`.mcp.json`](.mcp.json) usa `http`; ambas apuntan a
`https://duckhunt.info/mcp`. Al conectar, completa el consentimiento OAuth de
Duckhunt con tu cuenta y el espacio deseado. El servidor anuncia registro dinámico
de clientes públicos (DCR), PKCE S256 y los scopes `mcp:read` y `mcp:write` en sus
metadatos OAuth. Puedes elegir «solo lectura» en el consentimiento o gestionar
la conexión en `/settings/agents/connections`: las tools de escritura dejan de
listarse y sus llamadas se rechazan. `duckhunt-entry-get` sigue disponible para
leer o importar el item pedido; no modifica la fuente.

Las skills locales siguen incluidas en el paquete; su presencia no concede
permisos. Cada workflow solo puede usar las tools que ofrece la conexión.
El plugin no incluye credenciales. Para una instancia propia, cambia la URL en
ambos ficheros por su endpoint `/mcp` antes de instalar.
El transporte HTTP conserva el usuario del token; el stdio local del repo opera
como admin y no se usa en este paquete.

## Instalación personal

La creación del paquete no lo instala. Estos comandos, ejecutados desde la raíz
del repo en una terminal con acceso a tu directorio personal, usan el scaffold de
`plugin-creator` para registrar una **instalación nueva**, copian este paquete y
lo validan antes de instalarlo. Requieren Python con PyYAML, Codex y las skills de
sistema `plugin-creator` y `skill-creator`.

```bash
(
  set -eu
  duckhunt_repo="$(git rev-parse --show-toplevel)"
  plugin_creator="${CODEX_HOME:-$HOME/.codex}/skills/.system/plugin-creator"
  if [ -f "$HOME/.agents/plugins/marketplace.json" ]; then
    python3 "$plugin_creator/scripts/read_marketplace_name.py"
  fi
  python3 "$plugin_creator/scripts/create_basic_plugin.py" duckhunt \
    --with-skills --with-assets --with-mcp --with-marketplace
  cp -R "$duckhunt_repo/plugins/duckhunt/." "$HOME/plugins/duckhunt/"
  python3 "$plugin_creator/scripts/validate_plugin.py" "$HOME/plugins/duckhunt"
  duckhunt_marketplace="$(python3 "$plugin_creator/scripts/read_marketplace_name.py")"
  codex plugin add "duckhunt@$duckhunt_marketplace"
)
```

El scaffold se detiene si ya existe el plugin o su entrada: no uses `--force`
para reemplazar una instalación sin revisar su origen. El marketplace personal
`~/.agents/plugins/marketplace.json` se descubre automáticamente. Abre un hilo
nuevo después de instalar y conectar el plugin para que cargue las skills y tools.

Para actualizar una instalación existente, sigue
`plugin-creator/references/installing-and-updating.md`: valida los identificadores,
confirma que la entrada apunta a la copia instalada, copia los cambios del repo,
ejecuta `scripts/update_plugin_cachebuster.py` sobre esa copia y vuelve a ejecutar
`codex plugin add` con el nombre validado del marketplace. No edites el marketplace
a mano.

## Comprobación del paquete

Desde la raíz del repo:

```bash
plugin_creator="${CODEX_HOME:-$HOME/.codex}/skills/.system/plugin-creator"
skill_creator="${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator"
python3 "$plugin_creator/scripts/validate_plugin.py" plugins/duckhunt
for skill in plugins/duckhunt/skills/*/; do
  python3 "$skill_creator/scripts/quick_validate.py" "$skill"
done
```

Tras conectar, pide «¿Qué necesita mi atención en Duckhunt hoy?». Debe leer el
brief y los eventos necesarios sin marcarlos como vistos. Para probar contexto,
pide el estado de una tarea existente por su referencia `t#N`; una consulta de
estado no debe moverla ni crear work notes. Las escrituras se prueban con una tarea
de prueba y una petición explícita de la acción.

Los PNG de `assets/` son copias de `assets/logo/mark-256.png` e
`assets/logo/icon-512.png` del repo; se incluyen para que el paquete sea autónomo.

## Preparación de publicación

El subtítulo tiene 28 caracteres y el color `#C88718` tiene contraste 3,03:1 contra
blanco. El manifiesto portable incluye el soporte en `/support` y nueve casos de
revisión (seis positivos y tres negativos) con setup, tools esperadas y resultados
observables. **Los casos están redactados, no ejecutados**: necesitan una cuenta
de revisión y los datos de ejemplo que describe cada caso. Las credenciales van
solo en los campos seguros del portal, nunca en este paquete.

La versión `0.7.0` regenera las skills `work` y `close`: la tarea se mantiene al día mientras se trabaja
(descripción, campos y, si el usuario deja mover estados, el estado de sus entries en la fuente) y el cierre deja la
descripción como lo entregado. No añade tools ni cambia el endpoint.

La versión `0.6.0` añade las skills `handoff` y `takeover`: transferir conversaciones en los dos sentidos
entre el agente del cliente y los de duckhunt (`duckhunt-agent-start`, `duckhunt-agent-message` y
`duckhunt-agent-takeover`); lo que se pide en edición espera la aprobación del usuario en su dispositivo. No cambia el
endpoint.

La versión `0.5.0` regenera las skills `review` y `close` sobre las tools genéricas de
pull requests (`duckhunt-pr-review-tasks`, `duckhunt-pr-review-task-resolve` y el ci de
`duckhunt-pipeline-*` en bitbucket y github) en lugar de las de bitbucket; el servidor crea issues
en jira, linear o github con `duckhunt-entry-create`. No cambia el endpoint.

El nombre público del plugin es `duckhunt`, el editor indicado es `Juan Mier` y la
disponibilidad incluye todos los países
admitidos por el portal (`publication.countries: []`, sin restricciones de países).
La verificación de identidad se completa en el portal.

Antes de presentar el plugin faltan por confirmar:

- Si hay pagos o compras.
- Acceso OAuth de la cuenta de prueba y ejecución de los casos de revisión.
- Accesibilidad y vigencia de la [demo registrada](https://youtu.be/5iA5Tm-HaJA),
  ya incluida en `review.demo_recording_url`.

Las URLs indicadas por el editor son `https://duckhunt.info/privacy` para privacidad
y `https://duckhunt.info/policies` para términos de servicio, guardadas en ambos
manifiestos. El 2026-09-30 `/privacy`, `/policies`, `/support`, los metadatos OAuth de
`/.well-known/` y el challenge `/.well-known/openai-apps-challenge` respondían 200 en
público, y `/mcp` sin token devolvía 401 con `resource_metadata`.

Para renovar la demo, usa una cuenta de prueba en Codex con el plugin conectado:
enseña el consentimiento OAuth sin credenciales en pantalla, pide el resumen del
inbox sin cambios, crea la tarea `Plugin review creation`, añade una work note y
léela de vuelta, y termina con el ejemplo negativo de enviar correo. Muestra los
prompts y resultados reales de cada paso. Revisa el vídeo antes de alojarlo en una
URL accesible sin una cuenta privada; esa URL irá en `review.demo_recording_url`.
No se considera completa una demo por disponer solo de este guion.

El ZIP de publicación es `plugins/duckhunt.zip` (gitignorado): este directorio bajo
una carpeta raíz `duckhunt/`, ficheros ocultos incluidos. Regenéralo tras cualquier
cambio del paquete, desde la raíz del repo:

```bash
(cd plugins && rm -f duckhunt.zip && python3 -m zipfile -c duckhunt.zip duckhunt)
```
