# Acuario-IA 🌊

Prototipo académico en Python para monitoreo simulado de calidad del agua marina y **algoritmos de búsqueda BFS, UCS y A***. Datos ilustrativos; no conectar a equipos reales.

## Demo visual
- Sitio web: https://antoniii28.github.io/Acuario-IA/
- La web presenta un ejemplo didáctico de temperatura (estado inicial variable, meta 26 °C, costo unitario). Ejecuta BFS, UCS y A* sobre ese grafo sencillo.
- El enlace de Colab para la exposición abre la versión visual con acuario animado y peces; solo simula la temperatura y la corrección dentro del rango ilustrativo de 24–26 °C. No incluye salinidad ni pH.

## Ejecutar
- Para la exposición, abrir el [notebook visual de temperatura con acuario animado](https://colab.research.google.com/github/Antoniii28/Acuario-IA/blob/fase6-flujo-profesional/notebooks/Acuario_IA_Fase6_Flujo_Profesional.ipynb) y ejecutar las celdas desde el inicio. El notebook `notebooks/Acuario_IA_Colab.ipynb` es una versión ampliada diferente.
- En terminal: `python src/acuario_ia.py`
- Pruebas: `python -m unittest discover -s tests -v`.
- No requiere dependencias externas.

## Ejemplo
Estado inicial: 28 °C, 38 ppt y pH 7.8. Meta: 26 °C, 35 ppt y pH 8.2.
Los pasos simulan ajustes con costos abstractos. BFS prioriza cantidad de acciones; UCS costo acumulado g(n); A* usa f(n)=g(n)+h(n). En la demo de temperatura, h(T)=|T−26|; en el modelo ampliado, la heurística depende de los tres parámetros.
Resultados esperados: BFS 3 acciones/costo 20, UCS y A* 7 acciones/costo 13.

## Contenido
- `src/acuario_ia.py`: alertas y búsqueda.
- `notebooks/Acuario_IA_Colab.ipynb`: demo autónoma en Colab.
- `tests/test_acuario.py`: pruebas de regresión.
- `docs/guia_exposicion.md`: estructura de presentación.

## Limitaciones
No utiliza ML entrenado ni sensores. Rangos ilustrativos: temperatura 24-26 °C, salinidad 34-36 ppt, pH 8.0-8.4. Estos rangos no son universales y las acciones NO deben aplicarse a acuarios reales.

## Referencias
- [NOAA: Ocean acidification](https://www.noaa.gov/ocean-acidification)
- [Stanford CS221: búsquedas por estados](https://stanford.edu/~shervine/teaching/cs-221/cheatsheet-states-models/)
- [Python: heapq](https://docs.python.org/3/library/heapq.html)

## Fase 3 — Dashboard interactivo en Colab

El cuaderno ahora incluye un panel con:
- Selector de escenario: base, dentro de rango y salinidad alterada.
- Controles de temperatura, salinidad y pH.
- Validación de rangos y alertas con gráficos de medición.
- Comparación visual de pasos, costos y estados expandidos de BFS, UCS y A*.
- Selección de algoritmo y visualización del grafo correspondiente.

**Alcance deliberado:** las entradas manuales son solo para el monitoreo de umbrales; los algoritmos y el grafo están definidos exclusivamente para el escenario base (28 °C, 38 ppt, 7.8 pH), sin recalcular una nueva meta a partir de los controles. Así se evita presentar rutas falsas para entradas no discretizadas.

Abre el cuaderno desde GitHub en Colab y elige **Entorno de ejecución → Ejecutar todas**. La última sección contiene el panel interactivo. Si se necesita solo una gráfica, utiliza el botón correspondiente.
