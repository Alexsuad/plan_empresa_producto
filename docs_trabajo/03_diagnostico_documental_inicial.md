# File: docs_trabajo/03_diagnostico_documental_inicial.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Diagnóstico del estado documental de la Fase 0.
# Rol: Auditoría de producto y recomendaciones estratégicas.
# ──────────────────────────────────────────────────────────────────────

# Diagnóstico Documental Inicial - Fase 0

Este documento presenta el análisis del estado actual del repositorio documental del proyecto "Plan de Empresa / Producto".

## 1. Estado de cada documento

| Archivo | Estado | Observación |
| :--- | :--- | :--- |
| `00_documento_maestro_...` | **LISTO** | Actualizado con la arquitectura funcional permitida y rutas correctas. |
| `01_guia_humana_...` | **SOBRECARGADO** | Contiene el núcleo pedagógico, pero mezcla diseño operativo al final. |
| `02_mapa_transversal_...` | **ESQUELÉTICO** | Contiene solo la cabecera. El contenido que le corresponde está en `01`. |

## 2. Problemas de nombre, estructura o jerarquía

- **Rutas en encabezados:** Los archivos `01` y `02` mantienen en su cabecera la ruta antigua (`docs/`), lo que genera confusión sobre su ubicación real en `docs_trabajo/`.
- **Jerarquía plana en `01`:** Se utiliza el nivel H1 (`#`) para casi todas las secciones y subsecciones (ej. `# 1.`, `# 1.1`, `# 1.2`), lo que rompe la navegación semántica de Markdown y dificulta la lectura de la estructura.
- **Nomenclatura inconsistente:** Algunos títulos internos de `01` no coinciden con el nuevo nombre del archivo (se refieren a "Blueprint" o "Guía Red ARCE").

## 3. Secciones duplicadas o repetidas

- Se detectan preguntas sobre **viabilidad y riesgos** que aparecen tanto en los bloques específicos del plan de empresa como en la sección final de "Revisión transversal" de `01`.
- Hay una redundancia intencionada (pedagógica) en las preguntas para el emprendedor, pero debe vigilarse que no genere datos contradictorios en el futuro sistema.

## 4. Contenido que parece estar en el documento equivocado

- **El "final" de `01` pertenece a `02`:** Desde la línea 10650 aproximadamente ("Investigaciones profundas por punto") hasta el final del archivo `01`, el contenido es puramente operativo y de diseño de sistema (matrices de investigación, niveles de profundidad, etc.). Esto debería estar en el **Mapa Transversal**.
- **Diagnósticos operativos en `01`:** Las tablas de "Mini diagnóstico" (ej. sección 1.14 de `01`) están a medio camino entre una guía humana y un requisito de validación del sistema.

## 5. Contenido que falta para completar la fase de producto

- **Matriz de Trazabilidad Completa:** Falta mapear formalmente cada pregunta de la guía humana con su anexo correspondiente en `02`.
- **Definición de Preinformes:** Aunque se mencionan, no hay una estructura detallada de qué entrega el sistema al emprendedor tras completar cada bloque.
- **Requisitos de Skills de Producto:** Falta listar qué habilidades específicas debe simular cada rol funcional del servicio.

## 6. Riesgos de edición

- **Tamaño de `01_guia_humana_...`:** Con más de 10,000 líneas, es un archivo propenso a errores de edición, tiempos de carga lentos para herramientas de IA y dificultad de mantenimiento.
- **Mezcla de roles:** Al estar el diseño del sistema mezclado con la guía humana, existe el riesgo de que Antigravity empiece a diseñar arquitectura técnica antes de cerrar la fase de producto.

## 7. Recomendaciones de mejora

1. **Trasvase de contenido:** Mover toda la capa de "Diseño transversal" (anexos, investigaciones, validaciones) del final de `01` al archivo `02`.
2. **Normalización de Jerarquía:** Cambiar los niveles de `01` a una estructura lógica:
   - `# Título Principal`
   - `## Bloque (1. Equipo, 2. Idea...)`
   - `### Subsección (1.1, 1.2...)`
3. **Fragmentación (Opcional):** Valorar si `01` debería dividirse en archivos por bloques (ej. `01a_equipo_promotor.md`, `01b_idea.md`) para mejorar la agilidad.
4. **Corrección de metadatos:** Sincronizar las rutas de los encabezados con la realidad del sistema de archivos.

## 8. Próximo paso recomendado

1. **Limpieza y Trasvase:** Mover el bloque de diseño operativo de `01` a `02` y corregir los encabezados de ambos.
2. **Auditoría de validaciones:** Una vez que `02` tenga su contenido, revisar si las validaciones propuestas son suficientes para los "Criterios de calidad" definidos en el documento maestro.

---
> [!NOTE]
> Este diagnóstico se ha realizado sin modificar los documentos originales `01` y `02`, cumpliendo con las restricciones de la Fase 0.
