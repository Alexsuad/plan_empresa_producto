---
description: Diagnóstico funcional del repositorio
---

# File: .agents/workflows/diagnostico_funcional_repositorio.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir el flujo para diagnosticar el estado funcional del repositorio.
# Rol: Workflow documental para diagnóstico inicial.
# ──────────────────────────────────────────────────────────────────────


# Workflow — Diagnóstico funcional del repositorio

## Objetivo

Crear o actualizar:

`docs_arquitectura_funcional/00_diagnostico_estado_actual_repositorio.md`

## Pasos

1. Leer documentos base del repositorio.
2. Identificar estructura actual.
3. Listar fortalezas.
4. Listar riesgos.
5. Detectar documentos faltantes.
6. Relacionar el estado actual con `Proyecto_automatizaciones`.
7. Indicar reglas del documento maestro aplicables.
8. Cerrar con próximos pasos.

## No hacer

- No crear código.
- No crear backend.
- No crear frontend.
- No crear agentes ejecutables.
- No borrar documentos.
- No modificar estructura sin aprobación.

## Evidencia esperada

- Archivo diagnóstico creado o actualizado.
- `git status`
- `git diff`
- Estado final: `pendiente_validacion`