# FIERA - reglas abiertas de Google Ads

Somos Fiera, una consultora de performance marketing de Barcelona. Gestionamos cada día cuentas de Google Ads de empresas de distintos sectores, y estas reglas salen de ese trabajo: comportamientos de la API que la documentación no cuenta, lecturas de datos que engañan y decisiones que hemos visto salir bien y mal.

Las publicamos como Agent Skills para quien ya trabaja, o quiere empezar a trabajar, con un agente conectado a Google Ads. Las personas que gestionan cuentas también pueden leerlas tal cual.

## Qué hay dentro

### Empieza aquí

Si es la primera vez que conectas un agente a Google Ads, empieza por estas dos skills:

| Skill | Para qué sirve |
|---|---|
| `google-ads-setup` | Montar el agente desde cero: cómo conectarlo a Google Ads, por qué empezar en solo lectura, cómo instalar estas reglas y cómo comprobar que funciona |
| `google-ads-account-context` | Crear `account-context.md` con el negocio, los objetivos, los buckets de campañas, el contrato de medición y las reglas de marca de una cuenta. Las demás skills lo leen antes de trabajar |

### Reglas y auditoría

Las otras cinco skills llevan las reglas. Cada una lleva un `SKILL.md` con el índice de sus reglas y una carpeta `references/` con las reglas completas, separadas por tema. El agente lee el índice y abre solo el fichero que necesita.

| Skill | Qué cubre | Reglas |
|---|---|---|
| `google-ads-api-gotchas` | GAQL, cliente Python, historial de cambios, cuotas, mutaciones seguras, creación de campañas, PMax y Demand Gen por API, Auction Insights | 103 |
| `google-ads-keywords-negatives` | Search terms, match types, AI Max, negativas, Keyword Planner y Quality Score | 29 |
| `google-ads-copy-assets-pmax` | Copy de RSA, extensiones, Performance Max, Demand Gen, App, estructura, geo y landing pages | 53 |
| `google-ads-bidding-measurement` | Smart Bidding, portfolios, budgets y pacing, objetivos de conversión, tracking, lag y atribución | 18 |
| `google-ads-account-audit` | Auditoría de una cuenta en doce pasos, en solo lectura | 1 workflow |

## Cómo instalarlo

En Claude Code, añade el marketplace e instala el plugin:

```
/plugin marketplace add fieradigital/fiera-google-ads-rules
/plugin install fiera-google-ads-rules@fiera-google-ads-rules
```

Si usas otro agente que lea ficheros `SKILL.md`, como Codex o Cursor, copia la carpeta `skills/` en el directorio de skills de tu agente. Cada skill funciona sola, aunque la auditoría cita reglas de las otras y todas leen `account-context.md` si existe.

## Cómo está escrita cada regla

Todas las reglas siguen el mismo formato:

- **Tipo**: gotcha de API, gotcha de plataforma, regla de decisión, regla de seguridad o error de método.
- **Por qué**: el mecanismo que explica el comportamiento.
- **Cómo detectarlo**: la consulta GAQL, el campo o el paso concreto para verlo en tu cuenta.
- **Qué hacer**: la acción.
- **Evidencia**: en cuántas cuentas lo hemos visto y cuándo.

"Visto en 1 cuenta" quiere decir que lo hemos observado en una sola cuenta. Lo publicamos porque el mecanismo es reproducible, pero conviene comprobarlo en tu cuenta antes de actuar. "Visto en 2-3 cuentas" y "Visto en 4+ cuentas" indican que se ha repetido. Los gotchas de API llevan la versión en la que se comprobaron, casi siempre la v24.

Ninguna regla identifica a un cliente. Hemos quitado nombres, sectores, mercados y cifras absolutas de cuenta.

## Sin soporte

Puedes usar estas reglas libremente, tal como están. Leemos los issues que se abran, pero no los contestamos uno a uno. Si una regla deja de ser cierta por un cambio de Google, nos ayuda mucho que lo cuentes en un issue.

## ¿Necesitas más?

Si quieres que un agente aplique estas reglas sobre tus cuentas cada día, con análisis, propuestas y cambios aprobados, mira nuestra [plataforma de agentes](https://fiera.digital/agent-platform?utm_source=github&utm_medium=readme&utm_campaign=rules-v1). Si prefieres que llevemos tus campañas, mira nuestro servicio de [paid media](https://fiera.digital/paid-media?utm_source=github&utm_medium=readme&utm_campaign=rules-v1). Para cualquier otra cosa, [escríbenos](https://fiera.digital/contact?utm_source=github&utm_medium=readme&utm_campaign=rules-v1).

## Licencia

El texto se publica bajo [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Puedes copiarlo, adaptarlo y usarlo en proyectos comerciales, siempre que cites a Fiera como autor y enlaces a la licencia. El texto completo está en [`LICENSE`](LICENSE).
