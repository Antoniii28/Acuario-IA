"""Visualización del grafo de estados: prototipo educativo Acuario-IA.
Funciona con Matplotlib, sin NetworkX; no realiza ajustes físicos.
"""
from acuario_ia import INICIAL, META, sucesores, buscar
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def construir_grafo():
    """Devuelve todos los nodos y aristas calculados mediante sucesores reales."""
    nodos = [(t,s,p) for t in range(META[0]+1)
                     for s in range(META[1]+1)
                     for p in range(META[2]+1)]
    aristas = [(estado, siguiente, costo, accion)
               for estado in nodos for siguiente,costo,accion in sucesores(estado)]
    return nodos, aristas

def posiciones_por_capas(nodos):
    """Orden determinista por progreso, sin confundir estados iguales."""
    capas = defaultdict(list)
    for nodo in nodos:
        capas[sum(nodo)].append(nodo)
    pos = {}
    for nivel, estados in capas.items():
        for i, estado in enumerate(sorted(estados)):
            pos[estado] = (nivel, i-(len(estados)-1)/2)
    return pos

def validar_ruta(ruta):
    estado=INICIAL
    for accion,costo,siguiente in ruta:
        if (siguiente,costo,accion) not in list(sucesores(estado)):
            raise ValueError("La ruta no corresponde al grafo de transiciones")
        estado=siguiente
    if estado!=META:
        raise ValueError("La ruta no termina en la meta")
    return True

def visualizar_grafo(algoritmo="A*", guardar=None):
    if algoritmo not in ("BFS","UCS","A*"):
        raise ValueError("Algoritmo desconocido")
    nodos,aristas=construir_grafo()
    ruta,costo,expandidos,frontera=buscar(algoritmo)
    validar_ruta(ruta)
    pos=posiciones_por_capas(nodos)
    aristas_ruta=set()
    anterior=INICIAL
    for _,_,estado in ruta:
        aristas_ruta.add((anterior,estado))
        anterior=estado
    fig,ax=plt.subplots(figsize=(15,7))
    fig.patch.set_facecolor("#071c33")
    ax.set_facecolor("#071c33")
    for origen,destino,peso,_ in aristas:
        x1,y1=pos[origen]; x2,y2=pos[destino]
        elegida=(origen,destino) in aristas_ruta
        flecha=FancyArrowPatch((x1,y1),(x2,y2),
              arrowstyle="-|>",mutation_scale=12 if elegida else 7,
              color="#3ee2a0" if elegida else "#688098",
              alpha=0.95 if elegida else 0.18,
              linewidth=2.5 if elegida else 0.65,
              shrinkA=11,shrinkB=11,zorder=1)
        ax.add_patch(flecha)
        if elegida:
            ax.text((x1+x2)/2,(y1+y2)/2+0.15,str(peso),
                    fontsize=9,color="#f9d65c",ha="center",weight="bold")
    camino={INICIAL}|{paso[2] for paso in ruta}
    for estado in nodos:
        x,y=pos[estado]
        color=("#F59E0B" if estado==INICIAL else
               "#22C55E" if estado==META else
               "#45c7cf" if estado in camino else "#466078")
        ax.scatter(x,y,s=270 if estado in camino else 100,c=color,
                   edgecolors="#e7f7fc" if estado in camino else "none",
                   linewidths=0.9,zorder=3)
        if estado in camino:
            ax.text(x,y-0.37,str(estado),fontsize=8,color="#ffffff",ha="center",zorder=4)
    ax.set_title(f"ACUARIO-IA · Grafo de estados · {algoritmo}\n"
                 f"{len(nodos)} nodos · {len(aristas)} transiciones · "
                 f"{len(ruta)} acciones · costo {costo} · {expandidos} expandidos",
                 color="white",fontsize=15,pad=22)
    ax.set_xlim(-0.6,7.6)
    ys=[p[1] for p in pos.values()]
    ax.set_ylim(min(ys)-0.85,max(ys)+0.85)
    ax.set_xticks(range(8))
    ax.set_xlabel("Avance discreto hacia la meta (t+s+p)",color="#d9edf4")
    ax.set_yticks([])
    ax.tick_params(colors="#d9edf4")
    for spine in ax.spines.values(): spine.set_visible(False)
    fig.tight_layout()
    if guardar:
        fig.savefig(guardar,dpi=170,bbox_inches="tight",facecolor=fig.get_facecolor())
    plt.show()
    return {"nodos":len(nodos),"aristas":len(aristas),"acciones":len(ruta),
            "costo":costo,"expandidos":expandidos,"frontera_maxima":frontera}

def comparar_grafos():
    for nombre in ("BFS","UCS","A*"):
        visualizar_grafo(nombre)
