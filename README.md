# Evaluacion2 - Sistema de Geolocalización y Rutas (Biblioteca Nacional)

**Autora:** María Ignacia Navarro  
**Asignatura:** Telepresencia y Entornos Innovadores de Colaboración Humana (CUY6142)

## Descripción del Proyecto
Script interactivo en Python que consume la API REST de **GraphHopper Directions** para calcular rutas optimizadas hacia la Biblioteca Nacional en español, mostrando distancias y tiempos con un máximo de dos decimales (`{:.2f}`), narrativa paso a paso en español (`locale=es`) y opción de salida ingresando `"s"` o `"salir"`.

## Instrucciones de Ejecución
1. Asegurarse de contar con Python 3 y la librería `requests` instalada.
2. Ejecutar el script desde la terminal:
   ```bash
   python3 graphhopper_evaluacion2.py
Ingresar la ubicación de inicio y la ubicación de destino cuando el programa lo solicite, o escribir "s" / "salir" para finalizar la ejecución.