#!/usr/bin/env python3
import os
import sys
import argparse
import shutil

# File: scripts/fragmentar_guia_humana.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Fragmentar la Guía Humana en archivos modulares.
# Rol: Script de mantenimiento documental determinista.
# ──────────────────────────────────────────────────────────────────────

SOURCE_FILE = "docs_trabajo/01_guia_humana_plan_empresa.md"
TARGET_DIR = "docs_trabajo/01_guia_humana/"

# Mapa de bloques basado en encabezados reales detectados
MAPA_BLOQUES = [
    {
        "nombre": "01. Equipo promotor",
        "inicio": "# 1. Equipo promotor",
        "fin": "# 2. Idea de negocio",
        "destino": "01_equipo_promotor.md"
    },
    {
        "nombre": "02. Idea de negocio",
        "inicio": "# 2. Idea de negocio",
        "fin": "# 3. Análisis del entorno y las propias capacidades",
        "destino": "02_idea_negocio.md"
    },
    {
        "nombre": "03.1 Análisis externo",
        "inicio": "# 3.1 Análisis externo",
        "fin": "# 3.2 Estudio del mercado",
        "destino": "03_1_analisis_externo.md"
    },
    {
        "nombre": "03.2 Estudio del mercado",
        "inicio": "# 3.2 Estudio del mercado",
        "fin": "# 3.3 Análisis interno",
        "destino": "03_2_estudio_mercado.md"
    },
    {
        "nombre": "03.3 Análisis interno",
        "inicio": "# 3.3 Análisis interno",
        "fin": "# 4. Análisis DAFO",
        "destino": "03_3_analisis_interno.md"
    },
    {
        "nombre": "04. Análisis DAFO",
        "inicio": "# 4. Análisis DAFO",
        "fin": "# 5. Objetivos y Líneas Estratégicas",
        "destino": "04_dafo_came.md"
    },
    {
        "nombre": "05. Objetivos y Líneas Estratégicas",
        "inicio": "# 5. Objetivos y Líneas Estratégicas",
        "fin": "# 6. Planes de Acción",
        "destino": "05_objetivos_lineas_estrategicas.md"
    },
    {
        "nombre": "06.1 Marketing y Ventas",
        "inicio": "# 6.1 Plan de Marketing y Ventas",
        "fin": "# 6.2 Plan de Operaciones",
        "destino": "06_1_marketing_ventas.md"
    },
    {
        "nombre": "06.2 Operaciones",
        "inicio": "# 6.2 Plan de Operaciones",
        "fin": "# 6.3 Plan de Recursos Humanos",
        "destino": "06_2_operaciones.md"
    },
    {
        "nombre": "06.3 Recursos Humanos",
        "inicio": "# 6.3 Plan de Recursos Humanos",
        "fin": "# 6.4 Plan Jurídico y Fiscal",
        "destino": "06_3_recursos_humanos.md"
    },
    {
        "nombre": "06.4 Jurídico y Fiscal",
        "inicio": "# 6.4 Plan Jurídico y Fiscal",
        "fin": "# 6.5 Plan Económico-Financiero",
        "destino": "06_4_juridico_fiscal.md"
    },
    {
        "nombre": "06.5 Económico-Financiero",
        "inicio": "# 6.5 Plan Económico-Financiero",
        "fin": "# 7. Implantación y Puesta en Marcha",
        "destino": "06_5_economico_financiero.md"
    },
    {
        "nombre": "07. Implantación y Puesta en Marcha",
        "inicio": "# 7. Implantación y Puesta en Marcha",
        "fin": "# 8. Viabilidad y Conclusiones",
        "destino": "07_implantacion_puesta_marcha.md"
    },
    {
        "nombre": "08. Viabilidad y Conclusiones",
        "inicio": "# 8. Viabilidad y Conclusiones",
        "fin": None, # Hasta el final
        "destino": "08_viabilidad_conclusiones.md"
    }
]

def extraer_bloques(lineas):
    resultados = []
    
    for bloque in MAPA_BLOQUES:
        inicio_idx = -1
        fin_idx = -1
        
        # Buscar inicio
        for i, linea in enumerate(lineas):
            if linea.strip() == bloque["inicio"]:
                inicio_idx = i
                break
        
        if inicio_idx == -1:
            print(f"Error: No se encontró el encabezado de inicio '{bloque['inicio']}' para el bloque {bloque['nombre']}")
            sys.exit(1)
            
        # Buscar fin
        if bloque["fin"] is None:
            fin_idx = len(lineas)
        else:
            for i, linea in enumerate(lineas[inicio_idx + 1:], start=inicio_idx + 1):
                if linea.strip() == bloque["fin"]:
                    fin_idx = i
                    break
                    
        if fin_idx == -1:
            print(f"Error: No se encontró el encabezado de fin '{bloque['fin']}' para el bloque {bloque['nombre']}")
            sys.exit(1)
            
        contenido = "".join(lineas[inicio_idx:fin_idx])
        
        if not contenido.strip():
            print(f"Error: El bloque {bloque['nombre']} está vacío.")
            sys.exit(1)
            
        resultados.append({
            "nombre": bloque["nombre"],
            "destino": bloque["destino"],
            "contenido": contenido,
            "caracteres": len(contenido)
        })
        
    return resultados

def main():
    parser = argparse.ArgumentParser(description="Fragmentar la Guía Humana del Plan de Empresa.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true", help="Muestra qué haría sin escribir archivos.")
    group.add_argument("--write", action="store_true", help="Escribe los archivos destino.")
    parser.add_argument("--backup", action="store_true", help="Crea un backup .bak antes de sobrescribir archivos existentes (solo con --write).")
    
    args = parser.parse_args()
    
    if not os.path.exists(SOURCE_FILE):
        print(f"Error: No existe el archivo fuente {SOURCE_FILE}")
        sys.exit(1)
        
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        lineas = f.readlines()
        
    print(f"--- Iniciando fragmentación de {SOURCE_FILE} ---\n")
    
    bloques_extraidos = extraer_bloques(lineas)
    
    print(f"{'BLOQUE':<35} | {'ARCHIVO DESTINO':<35} | {'CARACTERES':<10} | {'ESTADO'}")
    print("-" * 100)
    
    for b in bloques_extraidos:
        ruta_destino = os.path.join(TARGET_DIR, b["destino"])
        
        if args.dry_run:
            print(f"{b['nombre']:<35} | {b['destino']:<35} | {b['caracteres']:<10} | [SIMULADO]")
        
        elif args.write:
            try:
                # Backup opcional si existe
                if args.backup and os.path.exists(ruta_destino):
                    shutil.copy2(ruta_destino, ruta_destino + ".bak")
                
                # Escribir contenido
                with open(ruta_destino, "w", encoding="utf-8") as f:
                    f.write(b["contenido"])
                
                print(f"{b['nombre']:<35} | {b['destino']:<35} | {b['caracteres']:<10} | OK")
            except Exception as e:
                print(f"{b['nombre']:<35} | {b['destino']:<35} | {b['caracteres']:<10} | ERROR: {e}")

    if args.dry_run:
        print("\n[INFO] Modo Dry-run finalizado. No se han realizado cambios físicos.")
    else:
        print("\n[INFO] Proceso de escritura finalizado.")

if __name__ == "__main__":
    main()
