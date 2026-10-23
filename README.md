# Acuario-IA 🌊

Prototipo académico en Python para monitoreo simulado de calidad del agua marina y **algoritmos de búsqueda BFS, UCS y A***. Datos ilustrativos; no conectar a equipos reales.

## Ejecutar
- En Google Colab, abrir `notebooks/Acuario_IA_Colab.ipynb` y ejecutar la celda.
- En terminal: `python src/acuario_ia.py`
- Pruebas: `python -m unittest discover -s tests -v`.
- No requiere dependencias externas.

## Ejemplo
Estado inicial: 28 °C, 38 ppt y pH 7.8. Meta: 26 °C, 35 ppt y pH 8.2.
Los pasos simulan ajustes con costos abstractos. BFS prioriza cantidad de acciones; UCS costo acumulado g(n); A* usa f(n)=g(n)+h(n).
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
