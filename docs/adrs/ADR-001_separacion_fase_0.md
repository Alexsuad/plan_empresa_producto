# ADR-001: Separación de Capas y Normalización de Fase 0

# ──────────────────────────────────────────────────────────────────────
# Propósito: Documentar la decisión de separar la guía didáctica de la capa operativa.
# Rol: Registro de decisiones de arquitectura de producto (ADR).
# ──────────────────────────────────────────────────────────────────────

## Estado
Ejecutado por Antigravity — pendiente de validación final de producto

## Contexto
Durante la Fase 0, la guía humana contenía bloques operativos y técnicos que dificultaban su uso pedagógico y generaban ruido para el diseño funcional del sistema agéntico.

## Decisión
1. **Separación de Responsabilidades**:
   - `01_guia_humana_plan_empresa.md`: Queda restringido exclusivamente al ámbito didáctico y acompañamiento del emprendedor.
   - `02_mapa_transversal_anexos_investigaciones_validaciones.md`: Se establece como el núcleo operativo que define qué debe hacer el sistema, con qué profundidad y bajo qué reglas.
2. **Normalización Terminológica**:
   - Se reemplaza "diseño técnico" por "definición funcional y traspaso técnico" para evitar el inicio prematuro de tareas de codificación.
   - Los agentes se definen como "roles funcionales" y no como componentes de software.

## Consecuencias
- **Positivas**: Mayor claridad para el usuario (emprendedor), estructura limpia para el diseño funcional, prevención de deuda técnica prematura.
- **Negativas**: Requiere mantener la sincronización manual entre la guía y el mapa operativo durante esta fase.

## Trazabilidad (Audit Trail)
- **Conservado**: El contenido íntegro de la investigación original.
- **Cambiado**: Ubicación del contenido operativo (de 01 a 02).
- **Agregado**: Este registro de decisiones.
