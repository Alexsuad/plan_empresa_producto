# Reporte de Auditoría de Encabezados para Fragmentación

Propósito: Identificar discrepancias entre el mapa de fragmentación propuesto y la realidad del archivo fuente.
Estado: REVISIÓN REQUERIDA

## 1. Discrepancias Críticas (Texto no coincide)

| Bloque Mapeado | Texto Real en el Archivo | Línea |
| :--- | :--- | :--- |
| `# 4. Análisis DAFO y CAME` | `# 4. Análisis DAFO` | 3681 |
| `# 5. Objetivos y líneas estratégicas` | `# 5. Objetivos y Líneas Estratégicas` | 4363 |
| `# 6.1 Plan de marketing y ventas` | `# 6.1 Plan de Marketing y Ventas` | 5034 |
| `# 6.2 Plan de operaciones` | `# 6.2 Plan de Operaciones` | 5821 |
| `# 6.3 Plan de recursos humanos` | `# 6.3 Plan de Recursos Humanos` | 6591 |
| `# 6.4 Plan jurídico y fiscal` | `# 6.4 Plan Jurídico y Fiscal` | 7322 |
| `# 6.5 Plan económico-financiero` | `# 6.5 Plan Económico-Financiero` | 8175 |
| `# 7. Implantación y puesta en marcha` | `# 7. Implantación y Puesta en Marcha` | 9295 |
| `# 8. Viabilidad y conclusiones` | `# 8. Viabilidad y Conclusiones` | 9932 |

## 2. Detección de Encabezados Duplicados

Se han detectado bloques que repiten el encabezado principal a pocas líneas de distancia (probablemente por una edición previa de unificación):

- **6.2 Plan de Operaciones**: Líneas 5821 y 5846.
- **6.3 Plan de Recursos Humanos**: Líneas 6591 y 6607.
- **6.4 Plan Jurídico y Fiscal**: Líneas 7322 y 7331.
- **6.5 Plan Económico-Financiero**: Líneas 8175 y 8189.
- **7. Implantación y Puesta en Marcha**: Líneas 9295 y 9305.
- **8. Viabilidad y Conclusiones**: Líneas 9932 y 9942.

## 3. Recomendación Técnica para el Script

Para que el script `fragmentar_guia_humana.py` funcione sin errores, se propone:
1. Usar una búsqueda de encabezados **insensible a mayúsculas**.
2. Definir los límites del bloque usando el **primer encuentro** de un encabezado y el **primer encuentro** del siguiente encabezado de nivel superior (#).
3. Normalizar los títulos en el script para que coincidan con la realidad del archivo.

---
*Reporte generado por Antigravity el 2026-05-04.*
