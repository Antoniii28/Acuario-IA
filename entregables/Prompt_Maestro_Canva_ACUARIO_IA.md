# Prompt maestro para Canva IA — Presentación ACUARIO-IA

## Instrucción principal
Crea una presentación académica en español, de **7 diapositivas**, para la asignatura **Inteligencia Artificial | Unidad: Algoritmos de Búsqueda**. El proyecto se titula **ACUARIO-IA: búsqueda de una ruta para regular la temperatura de un acuario marino simulado**.

La exposición dura aproximadamente **2 minutos**. Prioriza claridad visual, exactitud técnica y poco texto por diapositiva. No inventes datos, experimentos, sensores reales ni resultados que no estén descritos aquí.

## Identidad visual obligatoria: acuario MARINO
El ambiente debe ser de acuario marino de agua salada, con agua azul océano, arrecife de coral, roca viva, anémonas, corales marinos, peces payaso, peces cirujano o peces ángel marinos. Puede incluir un sensor digital ilustrado como elemento conceptual, pero debe quedar claro que el sistema es simulado.

**No usar:** acuarios de agua dulce, peces dorados, bettas, guppys, plantas de agua dulce, grava de colores, castillos de pecera ni estética de estanque.

### Dirección de arte
- Formato panorámico 16:9, presentación limpia y profesional.
- Paleta: azul abisal #061B2B, azul océano #087EAB, turquesa #2BC4A2, blanco espuma #F4FAFC, acento coral naranja #FF8C69.
- Fondo oscuro oceánico con degradados sutiles; usar motivos de ondas o partículas discretas, sin afectar la lectura.
- Tipografía sans serif moderna; títulos grandes, cuerpo breve y legible.
- Diagramas vectoriales simples, líneas limpias, flechas claras y buen contraste.
- Mantener el mismo estilo, paleta y jerarquía en todas las diapositivas.
- Evitar párrafos extensos, adornos excesivos y fotos detrás de texto.
- Si se usa imagen de fondo, que sea un arrecife marino realista y oscuro, con área limpia para texto.

## Contenido exacto por diapositiva

### Diapositiva 1 — Portada
**Título:** ACUARIO-IA
**Subtítulo:** Búsqueda de estados para la regulación térmica de un acuario marino simulado
**Asignatura:** Inteligencia Artificial · Unidad: Algoritmos de Búsqueda
**Pie:** Prototipo académico de IoT simulado

**Diseño:** arrecife marino de agua salada con corales, roca viva y peces marinos en el lado derecho. En el lado izquierdo, título grande y subtítulo. Añade una pequeña visualización digital de temperatura, por ejemplo “29 °C”, con apariencia de interfaz, no como fotografía de equipo real.

### Diapositiva 2 — Problema y escenario
**Título:** ¿Qué problema resolvemos?
**Texto breve:**
- El sistema recibe una temperatura simulada.
- Debe encontrar una secuencia de ajustes de ±1 °C.
- La meta ilustrativa es llegar al intervalo de 24–26 °C.
- No hay sensores ni actuadores físicos conectados.

**Diseño:** ilustración central de acuario marino con tres etiquetas pequeñas: “Lectura simulada”, “Búsqueda de ruta” y “Meta térmica”. Usar flechas sencillas entre las etiquetas.

### Diapositiva 3 — Formulación formal del problema
**Título:** Del escenario a un problema de búsqueda
Presenta cinco tarjetas o una tabla compacta:
- **Estado inicial S₀:** temperatura seleccionada, por ejemplo 29 °C.
- **Estados:** temperaturas enteras de 18 a 32 °C.
- **Acciones:** subir o bajar 1 °C, sin salir del espacio modelado.
- **Prueba de meta:** 24 ≤ T ≤ 26 °C.
- **Costo g(n):** suma acumulada; cada transición cuesta 1 unidad.
- **Heurística h(n):** distancia en grados al intervalo objetivo; vale 0 dentro del rango.

**Diseño:** diagrama de estados con nodos de temperatura, destacando 29 °C como inicio y 24–26 °C como zona meta turquesa. Asegurar que las flechas representen cambios de ±1 °C. El rango es ilustrativo y no debe presentarse como recomendación universal para especies marinas.

### Diapositiva 4 — Algoritmos comparados
**Título:** Tres formas de buscar una solución
Usa tres columnas visuales:
- **BFS — Búsqueda en anchura:** explora por niveles; con costos uniformes encuentra una ruta con el menor número de pasos.
- **UCS — Costo uniforme:** expande el estado con menor costo acumulado g(n).
- **A* — Búsqueda informada:** prioriza f(n) = g(n) + h(n).

**Diseño:** tres mini-grafos con nodos y flechas. BFS por niveles; UCS con etiqueta de costo acumulado; A* con la fórmula destacada. No afirmar que A* siempre es más rápido ni consume siempre menos memoria.

### Diapositiva 5 — Ejemplo de ruta
**Título:** De 29 °C a la zona objetivo
**Ruta demostrativa:** 29 → 28 → 27 → 26 °C
**Costo:** 3 transiciones × 1 unidad = 3
**Meta alcanzada:** 26 °C, dentro del intervalo ilustrativo.

**Diseño:** una ruta horizontal grande de cuatro nodos. Inicio 29 °C en coral naranja; pasos intermedios en azul; meta 26 °C en turquesa. Añade pequeñas flechas entre nodos. Mantén el fondo de arrecife muy sutil para que la ruta sea protagonista.

### Diapositiva 6 — Comparación y lectura de resultados
**Título:** ¿Qué aprendemos al comparar?
**Texto:**
- Con costo 1 por transición, BFS y UCS deben encontrar el mismo costo óptimo.
- A* también encuentra una solución óptima con la heurística admisible definida.
- Los estados expandidos y el tamaño máximo de frontera ayudan a comparar el trabajo de búsqueda.
- Estas métricas no equivalen a una medición exacta de memoria RAM.

**Diseño:** tabla compacta con columnas “Algoritmo”, “Costo”, “Estados expandidos”. No inventar cifras. Indica “valores obtenidos al ejecutar el notebook” para que se completen con los resultados reales de la corrida, o deja espacios editables si Canva no puede conocerlos. No generar números de ejemplo como si fueran resultados reales.

### Diapositiva 7 — Conclusión y límites
**Título:** Conclusión
**Texto:**
- ACUARIO-IA modela un problema de búsqueda sobre estados de temperatura.
- BFS, UCS y A* exploran el mismo espacio con estrategias distintas.
- La heurística de A* estima la distancia restante hasta la meta.
- Es un prototipo académico: no controla un acuario real y no es un modelo de aprendizaje automático.

**Cierre visual:** acuario marino con una interfaz discreta mostrando “Meta alcanzada: 26 °C”. Pie final: “Gracias”.

## Notas para exposición (aprox. 2 minutos)
- Diapositiva 1 (10 s): “Presentamos ACUARIO-IA, un prototipo académico de búsqueda aplicado a un acuario marino simulado”.
- Diapositiva 2 (15 s): “Partimos de una temperatura y buscamos una secuencia de ajustes de un grado hasta entrar en el rango objetivo ilustrativo”.
- Diapositiva 3 (20 s): “Cada temperatura es un estado, subir o bajar un grado son acciones, cada paso cuesta uno y la meta está entre 24 y 26 grados”.
- Diapositiva 4 (25 s): “BFS explora por niveles, UCS prioriza el costo acumulado y A* combina costo recorrido con una heurística”.
- Diapositiva 5 (15 s): “Desde 29 grados, una ruta es 29, 28, 27 y 26; son tres transiciones”.
- Diapositiva 6 (20 s): “Comparamos costo y estados explorados. Como los costos son uniformes, BFS y UCS coinciden en el costo mínimo; A* también es óptimo con esta heurística”.
- Diapositiva 7 (15 s): “El valor del proyecto es mostrar búsqueda y comparación de algoritmos en un sistema IoT simulado, no afirmar control físico real”.

## Reglas de calidad final
1. Mantén el español correcto y los símbolos matemáticos legibles.
2. No inventes resultados medidos, datos de sensores ni afirmaciones biológicas.
3. No llames a esto aprendizaje automático: es búsqueda en espacio de estados.
4. No representes agua dulce bajo ninguna circunstancia; debe parecer inequívocamente un arrecife marino.
5. Prioriza diagramas de búsqueda legibles por encima de ilustraciones decorativas.
