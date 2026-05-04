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