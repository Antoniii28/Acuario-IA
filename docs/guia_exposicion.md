# ACUARIO-IA — guía final de exposición

## Qué presenta el proyecto
Prototipo académico que ilustra algoritmos de búsqueda para encontrar ajustes de parámetros en un acuario simulado. No usa sensores, no controla equipos reales y no entrena un modelo de aprendizaje automático.

## Cómo cubrir la rúbrica

### 1. Escenario — 20 %
- Problema: determinar una secuencia de ajustes hasta alcanzar una meta.
- Contexto: acuario marino; mediciones y acciones simuladas.
- La web compara BFS, UCS y A* en un modelo sencillo de temperatura. El notebook enlazado para exponer es la versión visual con acuario animado y peces; solo revisa la temperatura simulada.

### 2. Formulación formal — 30 %
**Ejemplo visual de temperatura (web):**
- Estado inicial: S₀ = 29 °C (se puede cambiar en el control).
- Meta: T = 26 °C.
- Prueba de meta: el estado actual es exactamente 26 °C.
- Acciones: subir o bajar 1 °C; costo unitario 1.
- Costo acumulado: g(n) = suma de los costos de los pasos.
- Heurística: h(T) = |T − 26|.
- Evaluación de A*: f(n) = g(n) + h(n).
- Ejemplo: h(29) = |29 − 26| = 3; al inicio g(n) = 0, así que f(n) = 0 + 3 = 3.

**Notebook visual de Colab (el que se abre desde la página):**
- Simula únicamente la temperatura.
- Rango ilustrativo: 24–26 °C.
- Incluye acuario animado, flujo de decisión y ruta simulada de corrección.
- No incluye salinidad ni pH en esta versión visual y no controla equipos reales.

### 3. Selección y justificación del algoritmo — 30 %
- BFS: prioriza la menor cantidad de acciones; no considera los costos diferentes al decidir.
- UCS: expande el estado con menor costo acumulado g(n); conviene cuando los costos son distintos.
- A*: usa f(n)=g(n)+h(n) para equilibrar costo real y estimación restante.
- En el ejemplo de temperatura, cada acción cuesta 1: BFS, UCS y A* encuentran costo 3 desde 29 °C a 26 °C.
- En el modelo ampliado de Colab, los resultados esperados del código son BFS: 3 acciones/costo 20; UCS: 7 acciones/costo 13; A*: 7 acciones/costo 13.
- Optimalidad: BFS es óptimo en número de acciones cuando todos los pasos cuestan lo mismo; UCS es óptimo con costos de paso no negativos; A* es óptimo con una heurística admisible bajo las condiciones estándar del algoritmo.
- Complejidad general: BFS O(V+E); UCS/A* con cola de prioridad, típicamente O((V+E) log V) en el grafo explícito. Memoria O(V+E). V = estados y E = conexiones. Son cotas de estructura, no mediciones directas de RAM.

### 4. Trabajo en equipo y presentación — 20 %
- Repartir la explicación entre integrantes si el equipo lo requiere.
- Mostrar la web, mover el control de temperatura y leer el cálculo de h y f.
- Abrir Colab para mostrar el acuario animado, cambiar la temperatura simulada y observar la ruta de corrección.
- Cerrar con la diferencia entre minimizar pasos y minimizar costo.

## Guion hablado de aproximadamente 2 minutos
“ACUARIO-IA es un prototipo educativo de búsqueda; trabaja con datos simulados y no controla un acuario real. En la página web simplificamos el problema a una sola variable: la temperatura. El estado inicial del ejemplo es 29 grados y la meta es 26 grados. Las acciones son subir o bajar un grado, con costo uno por acción.

La formulación define el estado inicial S₀, la prueba de meta T igual a 26, las acciones permitidas y el costo acumulado g(n). Para A* usamos la heurística h(T)=|T−26|, que estima los ajustes que faltan. Por ejemplo, h(29)=|29−26|=3. Como al inicio el costo recorrido es cero, f(n)=g(n)+h(n)=0+3=3.

BFS explora por niveles y busca la menor cantidad de acciones. UCS prioriza el costo acumulado. A* combina el costo recorrido y la heurística. En este ejemplo los tres encuentran costo tres porque todos los movimientos cuestan uno. En el notebook visual de Colab aparece el acuario animado y se simula una corrección de temperatura dentro del rango ilustrativo. La página web es la que permite comparar BFS, UCS y A* sobre el grafo sencillo de temperatura. Es un modelo académico, no un sistema de control real.”

## Checklist antes de exponer
- [ ] Abrir la página publicada y mover el control de temperatura.
- [ ] Comprobar que para 29 °C se muestra h=3, f inicial=3 y costo mínimo=3.
- [ ] Abrir el notebook visual con peces en Colab y ejecutar las celdas desde el inicio.
- [ ] Mostrar resultados de BFS/UCS/A* y explicar costo frente a cantidad de acciones.
- [ ] No afirmar que hay sensores reales, control físico o ML entrenado.
