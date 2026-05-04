---
trigger: always_on
---

---
trigger: always_on
---

# File: .agents/rules/03_trazabilidad_y_evidencia.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Exigir evidencia mínima antes de cerrar tareas.
# Rol: Regla de trazabilidad y cierre.
# ──────────────────────────────────────────────────────────────────────

# Regla — Trazabilidad y evidencia

Todo trabajo debe cerrar con:

1. Archivos creados o modificados.
2. Resumen de cambios.
3. Verificación realizada.
4. Estado final.
5. Próximos pasos.

Estados válidos:

- `estructura_creada`
- `documento_actualizado`
- `pendiente_validacion`
- `bloqueado_por_falta_de_datos`
- `flujo_parcial_validado`

No declarar “listo para producción” en esta fase.

No avanzar de fase sin entregable verificable.

## Traza acumulativa

Cuando una tarea modifique o cree documentación importante, debe registrar qué información fue:

- `Conservado`: contenido que se mantuvo igual porque sigue siendo válido.
- `Cambiado`: contenido ajustado, indicando el motivo.
- `Agregado`: contenido nuevo, indicando la fuente.

Fuentes válidas para contenido agregado:

- usuario;
- documento fuente;
- auditoría;
- regla de gobierno;
- decisión de arquitectura funcional.

Si no hay traza suficiente para explicar un cambio relevante, el estado final debe ser:

`pendiente_validacion`