# Práctica 3: Árbol de Decisión

**Curso:** Análisis de Algoritmos  
**Nombre:** Miguel Anres Monroy Najera  
**Carne:** 202302407  
**Fecha:** 18 de Noviembre 2025  

## Descripción
Implementación de un árbol de decisión simple en Python sin librerías externas.

## Objetivos
**General:** Construir y ejecutar un árbol de decisión simple en Python aplicando Gitflow.
**Específicos:**
* Implementar árbol con umbral.
* Generar dataset de 1000 números.
* Aplicar flujo de trabajo Gitflow.

--- 
## Lógica del Árbol:
El sistema utiliza una variable constante denominada `UMBRAL` (valor por defecto: 50).
1.  **Entrada:** Un número entero proveniente del archivo `data/numeros_1000.txt`.
2.  **Nodo de Decisión:** ¿Es el número mayor o igual al umbral?
    * **SÍ (`>= 50`):** Se clasifica como **"Alto"**.
    * **NO (`< 50`):** Se clasifica como **"Bajo"**.
3.  **Salida:** El sistema imprime la clasificación y genera estadísticas finales.

## Metodología y Flujo de Trabajo

### Estructura del Código
El proyecto se modularizó en la carpeta `src/`:
* `data_loader.py`: Se encarga de verificar la existencia del dataset. Si no existe, genera 1,000 números aleatorios entre 1 y 100 garantizando la reproducibilidad (semilla 42).
* `decision_tree.py`: Contiene la función pura que evalúa el número contra el umbral.
* `main.py`: Maneja la ejecución, mide el tiempo de procesamiento y muestra los resultados en consola.

## Resultados
* Total Altos: 513
* Total Bajos: 487
* Tiempo de ejecución: 0.0425 segundos
* Primeros 10 ejemplos: 
- 82 -> Alto
- 15 -> Bajo
- 4 -> Bajo
- 95 -> Alto
- 36 -> Bajo
- 32 -> Bajo
- 29 -> Bajo
- 18 -> Bajo
- 95 -> Alto
- 14 -> Bajo

## Conclusiones
* La implementación de Gitflow permitió mantener un historial limpio y ordenado, facilitando la identificación de en qué momento se agregó cada funcionalidad (feature) y cuándo se aplicaron correcciones (hotfix).
* Aunque el árbol de decisión implementado es básico, muestra cómo los algoritmos de clasificación binaria toman decisiones basadas en fronteras (umbrales) numéricas.
* La separación de lógica en módulos (`data_loader`, `decision_tree`) facilita el mantenimiento y la escalabilidad del código en comparación con un solo script.

## Evidencias
Las capturas de pantalla del funcionamiento y del repositorio se encuentran en la carpeta `docs/evidencias`.