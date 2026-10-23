# Exposición: Acuario-IA

## Problema
La supervisión manual de temperatura, salinidad y pH puede dejar pasar alteraciones en acuarios marinos. Se simulan lecturas, alertas y búsqueda de acciones abstractas.

## Formulación
- Estado físico inicial: 28 °C, 38 ppt, pH 7.8.
- Meta física simulada: 26 °C, 35 ppt, pH 8.2.
- Estado discreto inicial S0=(0,0,0), meta=(2,3,2).
- Acciones: cambios discretos en uno de los tres parámetros; consultar código para costos.
- Costo g(n): suma de los costos de acciones.
- Heurística h(t,s,p)=2(2-t)+(3-s)+3(2-p), cota inferior admisible.
- Algoritmos: BFS minimiza cantidad de acciones; UCS minimiza costo; A* prioriza f(n)=g(n)+h(n).

## Resultado esperado
BFS: 3 acciones y costo 20; UCS y A*: 7 acciones y costo 13. El número de estados expandidos depende del orden de desempate; A* no tiene por qué utilizar menos memoria en este ejemplo.

## Guion (2 minutos)
1. Presentar problemática y alcance de datos simulados.
2. Explicar estado inicial, meta y acciones.
3. Explicar g(n), h(n) y elección de A*.
4. Mostrar resultados de Colab y conclusión. 

## Aclaración
No hay sensores ni aprendizaje automático entrenado. Las alertas usan umbrales, mientras BFS, UCS y A* son algoritmos clásicos de búsqueda de IA. Los valores y acciones son ejemplos educativos, no indicaciones químicas reales.
