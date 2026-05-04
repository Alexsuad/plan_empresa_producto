---
description: Auditoría documental
---

# File: .agents/workflows/auditoria_documental.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir el flujo para auditar coherencia documental.
# Rol: Workflow de auditoría documental.
# ──────────────────────────────────────────────────────────────────────
# Workflow — Auditoría documental

## Objetivo

Revisar si los documentos del repositorio son coherentes entre sí y no contradicen el alcance de producto.

## Pasos

1. Leer documentos principales.
2. Comparar alcance declarado.
3. Detectar duplicados.
4. Detectar contradicciones.
5. Detectar secciones fuera de lugar.
6. Proponer acciones sin ejecutar cambios destructivos.
7. Registrar hallazgos en el documento indicado por el usuario.

## No hacer

- No borrar contenido.
- No reescribir documentos completos.
- No cambiar el sentido del proyecto.
- No convertir el proyecto en app técnica antes de tiempo.

## Evidencia esperada

- Lista de hallazgos.
- Recomendaciones.
- Archivos revisados.
- Estado final: `pendiente_validacion`.