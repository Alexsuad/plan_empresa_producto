# Propuesta de Fragmentación Documental — Fase 0

Propósito: Optimizar la gestión de documentos de gran tamaño para reducir el consumo de tokens y mejorar la precisión en las ediciones.
Rol: Documento de planificación de arquitectura documental.

---

## 1. Diagnóstico de situación actual

Tras analizar el repositorio, se identifica un desequilibrio crítico en la carga de información:

| Documento | Líneas | Tamaño | Impacto en Contexto |
| :--- | :--- | :--- | :--- |
| `01_guia_humana_plan_empresa.md` | ~10,600 | 358 KB | **CRÍTICO** |
| Otros documentos (promedio) | <250 | <10 KB | BAJO |

**El 95% de la carga informativa del proyecto reside en un solo archivo.**

---

## 2. Problemas detectados por el tamaño excesivo

1. **Consumo Ineficiente de Tokens**: Cada vez que un agente necesita leer la guía completa para un ajuste menor, consume una cantidad masiva de tokens de entrada, lo que encarece y ralentiza la operación.
2. **Riesgo de Corrupción de Datos**: Al realizar `replace_file_content` en archivos de más de 10,000 líneas, aumenta la probabilidad de errores en el cálculo de offsets o de perder bloques de texto por desajustes de línea.
3. **Dificultad de Auditoría**: Seguir los cambios en un diff de 350KB es extremadamente complejo para un humano, lo que dificulta la validación de producto.
4. **Límites de Herramientas**: Muchas herramientas de edición (incluyendo las de agentes) tienen límites de lectura de 800-1000 líneas por bloque, obligando a lecturas fragmentadas que impiden ver la "foto completa" del archivo.
5. **Bloqueo de Trabajo Paralelo**: Si dos procesos (humano o agente) intentan editar el mismo archivo gigante, el riesgo de conflictos de Git es máximo.

---

## 3. Propuesta de nueva estructura

Se recomienda pasar de una estructura plana a una estructura modular basada en la jerarquía del Plan de Empresa:

### Nueva Carpeta: `docs_trabajo/01_guia_humana/`

| Archivo sugerido | Contenido |
| :--- | :--- |
| `01_equipo_promotor.md` | Bloque 1: Datos, formación, experiencia, motivación y socios. |
| `02_idea_negocio.md` | Bloque 2: Descripción, propuesta de valor y modelo. |
| `03_1_analisis_externo.md` | Bloque 3.1: Análisis externo y PESTEL. |
| `03_2_estudio_mercado.md` | Bloque 3.2: Estudio de mercado, competencia y clientes. |
| `03_3_analisis_interno.md` | Bloque 3.3: Recursos, capacidades y fortalezas. |
| `04_dafo_came.md` | Bloque 4: Matriz de diagnóstico y líneas de acción. |
| `05_objetivos_lineas_estrategicas.md` | Bloque 5: Líneas estratégicas y metas. |
| `06_1_marketing_ventas.md` | Bloque 6.1: Canales, precios y ventas. |
| `06_2_operaciones.md` | Bloque 6.2: Producción, procesos y logística. |
| `06_3_recursos_humanos.md` | Bloque 6.3: Estructura orgánica y costes laborales. |
| `06_4_juridico_fiscal.md` | Bloque 6.4: Forma legal y normativa. |
| `06_5_economico_financiero.md` | Bloque 6.5: Inversiones, costes y tablas (gran volumen de datos). |
| `07_implantacion_puesta_marcha.md` | Bloque 7: Calendario, hitos y puesta en marcha. |
| `08_viabilidad_conclusiones.md` | Bloque 8: Análisis de viabilidad y veredicto final. |

---

## 4. Documentos Índice

1. **`00_documento_maestro_organizacion_producto.md`**: Se mantiene como el punto de entrada raíz del repositorio.
2. **`01_guia_humana_plan_empresa.md`**: **NO se elimina ni se vacía**. Se transforma en el **Índice Maestro de la Guía**. Contendrá la introducción general y enlaces directos a cada uno de los nuevos fragmentos en la carpeta `01_guia_humana/`, sirviendo como mapa de navegación principal.

---

## 5. Riesgos de la fragmentación

* **Pérdida de Trazabilidad Transversal**: Al separar los documentos, un agente podría olvidar la coherencia entre el "Equipo" (Bloque 1) y las "Operaciones" (Bloque 6).
* **Gestión de Enlaces**: Requiere actualizar todos los enlaces internos de Markdown.
* **Sobrecarga de Archivos**: Pasar de 4 archivos a 15 puede abrumar si no hay una nomenclatura estrictamente numérica.

---

## 6. Recomendación de orden de ejecución (Roadmap)

1. **Paso 1 (Preparación)**: Crear la carpeta `docs_trabajo/01_guia_humana/`.
2. **Paso 2 (Extracción Secuencial)**: Mover el contenido de la Guía Humana bloque por bloque a sus nuevos archivos, verificando que no se pierda información.
3. **Paso 3 (Indización)**: Transformar el archivo `01_guia_humana_plan_empresa.md` original en un índice estructurado con enlaces a los fragmentos.
4. **Paso 4 (Verificación)**: Comprobar que todos los enlaces funcionan y que el Documento Maestro (`00`) apunta correctamente al nuevo índice.

---

**Nota Final**: Esta fragmentación no es solo técnica, es estratégica. Permite que "especialistas" (ya sean humanos o agentes de IA) trabajen exclusivamente en el Plan de Marketing o en el Plan Financiero sin cargar con el peso de los otros 11 apartados.
