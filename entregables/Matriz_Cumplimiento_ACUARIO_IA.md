# ACUARIO-IA — Matriz de cumplimiento de la actividad

## Alcance del proyecto
ACUARIO-IA es un prototipo académico de un sistema IoT simulado para explorar estados de temperatura en un acuario marino. No está conectado a sensores, calentadores ni enfriadores reales. El intervalo de 24–26 °C es una meta ilustrativa del modelo y no una recomendación universal para especies marinas.

## 1. Escenario
El sistema recibe una temperatura inicial simulada y busca una secuencia de ajustes de ±1 °C para alcanzar el intervalo objetivo. La visualización usa un acuario marino de agua salada con corales, roca viva y peces marinos.

## 2. Formulación formal
- **Estado:** una temperatura entera T en °C dentro del espacio modelado de 18 a 32 °C.
- **Estado inicial S₀:** el valor seleccionado por el usuario.
- **Acciones/transiciones:** pasar de T a T−1 o T+1, siempre que el estado siguiente esté dentro de 18–32 °C.
- **Prueba de meta:** 24 ≤ T ≤ 26.
- **Costo de transición:** 1 unidad por cada cambio de 1 °C.
- **Costo acumulado g(n):** suma de los costos de las transiciones recorridas; equivale al número de pasos en este modelo.
- **Heurística h(n):**
  - Si T < 24, h(T) = 24 − T.
  - Si T > 26, h(T) = T − 26.
  - Si 24 ≤ T ≤ 26, h(T) = 0.
  
La heurística es admisible para este modelo: estima el mínimo de pasos necesarios para alcanzar el intervalo y no sobreestima el costo real.

## 3. Algoritmos
- **BFS:** explora por niveles. Con costo uniforme por transición, encuentra una ruta con el menor número de pasos. En un grafo explícito, su tiempo y memoria son O(V + E).
- **UCS:** expande el estado con menor costo acumulado g(n). Con costos positivos, encuentra una ruta de costo mínimo. Con cola de prioridad, el costo típico es O((V + E) log V) para esta representación.
- **A\*:** prioriza f(n) = g(n) + h(n). Con la heurística definida, conserva optimalidad para el modelo. En el peor caso puede consumir mucha memoria; su rendimiento depende de la heurística y del espacio de estados.

En este modelo cada transición cuesta 1, así que BFS y UCS deben coincidir en costo óptimo; A* también debe encontrar el costo mínimo. No se afirma que A* sea siempre más rápido. Se comparan estados expandidos y tamaño máximo de frontera. Estas métricas son indicadores de trabajo de búsqueda, no una medición exacta de RAM.

## 4. Caso demostrativo
Con estado inicial de 29 °C, una ruta óptima es 29 → 28 → 27 → 26. Son tres transiciones y el costo acumulado final es 3. La meta se alcanza en 26 °C, dentro del intervalo ilustrativo.

## 5. Matriz frente a la rúbrica
| Criterio | Evidencia preparada | Pendiente antes de declarar terminado |
|---|---|---|
| Escenario (20 %) | Escenario IoT simulado y delimitación explícita | Confirmar que el docente acepta el caso IoT de acuario dentro de la guía; la tabla de ejemplo se centra en redes |
| Formulación formal (30 %) | Estado, acciones, meta, costo y heurística definidos | Ejecutar la celda nueva y confirmar que la interfaz funciona en Colab |
| Selección y justificación (30 %) | BFS, UCS y A* implementados en el notebook; explicación de optimalidad y complejidad | Ejecutar pruebas en Colab y usar los valores reales que imprima la interfaz en la presentación |
| Exposición (20 %) | Prompt de presentación de 7 diapositivas y guion de aproximadamente 2 minutos | Crear/ajustar las diapositivas en Canva, ensayar el tiempo y distribuir participación |

## 6. Pruebas manuales recomendadas
Ejecutar la sección nueva en Google Colab y probar:
- 18 °C: temperatura baja; debe alcanzar 24 °C con costo 6.
- 22 °C: debe alcanzar 24 °C con costo 2.
- 25 °C: ya está en la meta; costo 0.
- 29 °C: debe alcanzar 26 °C con costo 3.
- 32 °C: debe alcanzar 26 °C con costo 6.

Para todos los casos, BFS, UCS y A* deben devolver un costo óptimo igual. Los estados expandidos pueden diferir. Registrar en la presentación solo los resultados realmente observados al ejecutar el notebook.

## 7. Límites que deben declararse
- Es una simulación, no control físico.
- No es un modelo de aprendizaje automático; es búsqueda en un espacio de estados.
- La temperatura objetivo es ilustrativa y no sustituye asesoría específica para especies marinas.
- La comparación se realiza en un espacio lineal pequeño; no demuestra una ventaja universal de A* en tiempo o memoria.
