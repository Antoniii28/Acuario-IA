# Grafo de estados del Acuario-IA

El grafo se genera directamente a partir de `sucesores()` del motor de búsqueda; no es un dibujo independiente de la lógica.

- **36 nodos:** todas las combinaciones (t,s,p) con t∈{0,1,2}, s∈{0,1,2,3}, p∈{0,1,2}.
- **Aristas dirigidas:** representan acciones legales; el número amarillo sobre la ruta resaltada representa el costo de la transición.
- **Naranja:** inicio; **verde:** meta; **turquesa:** ruta; **gris:** otros nodos.
- El layout usa capas por progreso t+s+p; la posición vertical es puramente visual.
- Los estados físicos se obtienen con (28-t °C, 38-s ppt, 7.8+0.2p pH).

Para ejecutar, abre el cuaderno `notebooks/Acuario_IA_Colab.ipynb` y ejecuta ambas celdas; aparecerán tres grafos (BFS, UCS y A*). La celda usa Matplotlib ya disponible normalmente en Colab.

La función `validar_ruta` comprueba que cada acción de la ruta coincide con una arista del grafo y que termina en la meta. Las rutas se calculan mediante las mismas funciones del prototipo que ya existían.

**Precaución:** es un espacio de estados discreto académico; no representa la cinética real del agua ni medidas seguras para corregir parámetros.
