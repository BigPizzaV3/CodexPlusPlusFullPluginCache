# Experimentos

### Los brazos de un experimento de broad de un clic no salen en la API
- **Tipo**: gotcha de API
- **Por qué**: los experimentos `ADOPT_BROAD_MATCH_KEYWORDS` parten el tráfico dentro de la misma campaña. `experiment_arm.campaigns` devuelve la campaña base en los dos brazos, y las métricas son la suma.
- **Cómo detectarlo**: no existe ninguna campaña `experiment_type = EXPERIMENT` con gasto.
- **Qué hacer**: leer el resultado por brazo en la UI. Por API solo se estima la potencia: conversiones totales entre dos por brazo.
- **Evidencia**: Visto en 1 cuenta, sep 2026, v24.

### Un brazo de experimento no se puede pausar
- **Tipo**: gotcha de API
- **Por qué**: cambiar el estado de una campaña `experiment_type = EXPERIMENT` devuelve `Cannot modify dates, budget or status of a trial campaign`. El lote atómico cae entero.
- **Cómo detectarlo**: excluir brazos de cualquier lote de cambios de estado.
- **Qué hacer**: para eliminarlos, `ExperimentService` con `remove`, que es irreversible y necesita aprobación explícita.
- **Evidencia**: Visto en 1 cuenta, ago 2026, v24.
