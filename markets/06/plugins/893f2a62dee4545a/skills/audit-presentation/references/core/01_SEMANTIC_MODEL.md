# Modelo semántico

## Entidades

| Entidad | Definición |
|---|---|
| Brief | Contrato vigente de intención, alcance y restricciones |
| Modo de investigación | Elección confirmada entre contexto/archivos sin web o investigación web complementaria |
| Confirmación | Aceptación o ajuste explícito del brief por el usuario antes de crear slides |
| Deck | Presentación completa, incluidos anexos contratados |
| Slide | Unidad visual con función y mensaje dominantes |
| Storyboard | Contrato de función, mensaje, evidencia y representación por slide |
| Claim | Proposición susceptible de evidencia o condición |
| Evidencia | Registro verificable que sustenta un claim |
| Supuesto | Condición adoptada explícitamente para avanzar |
| Hallazgo | Diferencia demostrable entre criterio y estado observado |
| Artefacto | Archivo o salida producida, versionada y verificable |
| Assurance | Estado interno de calidad; no equivale a aprobación externa |

## Estados de información

`EXPLICITA`, `DELEGADA`, `INFERIDA`, `AUSENTE_MATERIAL`, `NO_APLICA`.

En tareas que no crean slides, confirmar solo una inferencia material. Antes de crear slides, presentar siempre el brief consolidado y confirmar el conjunto completo, aunque las inferencias parezcan delegables. Resolver las decisiones delegadas y registrar el supuesto. No completar una ausencia material con invención.

El modo de investigación forma parte obligatoria del brief de creación:

- `FILES_AND_CONTEXT_ONLY`: trabajar únicamente con el conocimiento/contexto disponible y los archivos adjuntos; no buscar en la web.
- `WEB_COMPLEMENTARY`: complementar con búsqueda web verificable, únicamente después de confirmar el brief.

Una modificación material posterior invalida la confirmación y devuelve el brief a `PENDING_USER_CONFIRMATION`.

## Trazabilidad mínima

`Objetivo → Audiencia → Resultado → Mensaje → Claim → Evidencia → Slide → Acción/decisión`

Conservar únicamente los eslabones aplicables al producto. Corregir, condicionar o bloquear una ausencia que pueda cambiar el uso legítimo.

## Reglas transversales

- El conteo solicitado incluye portada y anexos, salvo indicación distinta.
- Una entrega de una sola slide no recibe portada adicional.
- No eliminar contenido obligatorio para resolver layout; sintetizar, redistribuir o trasladar con trazabilidad.
- `No disponible`, `Pendiente de validación`, `No determinable` y `Confianza limitada` son estados válidos.
