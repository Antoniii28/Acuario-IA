"""Simulación educativa de acuario marino; no controla equipos reales."""
from collections import deque
from heapq import heappush, heappop
from itertools import count

RANGOS = {"Temperatura (°C)": (24, 26), "Salinidad (ppt)": (34, 36), "pH": (8.0, 8.4)}
MEDICIONES = [("Normal",25,35,8.2),("Alterada",28,38,7.8),("Parcial",25,37,8.1)]
INICIAL, META = (0,0,0), (2,3,2)
PASOS = [
    (0,1,2,"Reducir temperatura 1 °C"),
    (0,2,7,"Reducir temperatura 2 °C"),
    (1,1,1,"Reducir salinidad 1 ppt"),
    (1,3,6,"Reducir salinidad 3 ppt"),
    (2,1,3,"Aumentar pH 0.2"),
    (2,2,7,"Aumentar pH 0.4"),
]

def monitorear(nombre, temperatura, salinidad, ph):
    """Alertas de umbral; no es aprendizaje automático."""
    alertas = []
    for (parametro,(minimo,maximo)), valor in zip(RANGOS.items(),(temperatura,salinidad,ph)):
        if not minimo <= valor <= maximo:
            alertas.append(f"{parametro}: {valor} fuera de [{minimo}, {maximo}]")
    print(f"{nombre}: " + (" | ".join(alertas) if alertas else "Todo en rango"))
    return alertas

def valores_reales(e):
    return (28-e[0], 38-e[1], round(7.8+0.2*e[2],1))

def sucesores(e):
    for eje,paso,costo,nombre in PASOS:
        nuevo=list(e); nuevo[eje]+=paso
        if nuevo[eje] <= META[eje]:
            yield tuple(nuevo),costo,nombre

def heuristica(e):
    return 2*(2-e[0]) + (3-e[1]) + 3*(2-e[2])

def ruta_de(padres, meta):
    ruta=[]; actual=meta
    while padres[actual] is not None:
        previo,accion,costo=padres[actual]
        ruta.append((accion,costo,actual)); actual=previo
    return list(reversed(ruta))

def buscar(algoritmo):
    if algoritmo not in ("BFS","UCS","A*"):
        raise ValueError("Algoritmo no reconocido")
    padres={INICIAL:None}; expandidos=0; max_frontera=1
    if algoritmo=="BFS":
        q=deque([INICIAL]); vistos={INICIAL}
        while q:
            e=q.popleft(); expandidos+=1
            if e==META:
                ruta=ruta_de(padres,e)
                return ruta,sum(a[1] for a in ruta),expandidos,max_frontera
            for n,c,a in sucesores(e):
                if n not in vistos:
                    vistos.add(n); padres[n]=(e,a,c); q.append(n)
            max_frontera=max(max_frontera,len(q))
    else:
        seq=count(); heap=[(heuristica(INICIAL) if algoritmo=="A*" else 0,next(seq),0,INICIAL)]
        mejor={INICIAL:0}
        while heap:
            _,_,g,e=heappop(heap)
            if g!=mejor[e]:
                continue
            expandidos+=1
            if e==META:
                return ruta_de(padres,e),g,expandidos,max_frontera
            for n,c,a in sucesores(e):
                ng=g+c
                if ng < mejor.get(n,float("inf")):
                    mejor[n]=ng; padres[n]=(e,a,c)
                    f=ng+(heuristica(n) if algoritmo=="A*" else 0)
                    heappush(heap,(f,next(seq),ng,n))
            max_frontera=max(max_frontera,len(heap))
    raise RuntimeError("Meta inalcanzable")

def main():
    print("ACUARIO-IA | datos y costos simulados, no aplicar físicamente")
    for datos in MEDICIONES:
        monitorear(*datos)
    print("Inicio:",valores_reales(INICIAL),"Meta:",valores_reales(META),"h(S0):",heuristica(INICIAL))
    for nombre in ("BFS","UCS","A*"):
        ruta,costo,expandidos,frontera=buscar(nombre)
        print(f"\n{nombre}: pasos={len(ruta)}, costo={costo}, expandidos={expandidos}, frontera máxima={frontera}")
        for i,(accion,c,estado) in enumerate(ruta,1):
            print(f"  {i}. {accion} (simulado), costo {c}, estado {valores_reales(estado)}")

if __name__=="__main__":
    main()
