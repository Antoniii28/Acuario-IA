"""FASE 3 - Panel interactivo educativo en Colab (ipywidgets)."""
import ipywidgets as widgets
import matplotlib.pyplot as plt
from IPython.display import display, HTML, clear_output
from acuario_ia import RANGOS, INICIAL, buscar, valores_reales
from graph import visualizar_grafo

ESCENARIOS = {
    "Caso base de búsqueda (28 °C / 38 ppt / 7.8)": (28.,38.,7.8),
    "Acuario dentro de rango (25 °C / 35 ppt / 8.2)": (25.,35.,8.2),
    "Solo salinidad alterada (25 °C / 37 ppt / 8.1)": (25.,37.,8.1),
}
CASO_BASE = (28.,38.,7.8)
estilo = {"description_width":"105px"}
temperatura = widgets.FloatSlider(value=28,min=20,max=32,step=.5,description="Temperatura",style=estilo,continuous_update=False,layout=widgets.Layout(width="340px"))
salinidad = widgets.FloatSlider(value=38,min=30,max=42,step=.5,description="Salinidad",style=estilo,continuous_update=False,layout=widgets.Layout(width="340px"))
ph_control = widgets.FloatSlider(value=7.8,min=7,max=9,step=.1,description="pH",style=estilo,continuous_update=False,layout=widgets.Layout(width="340px"))
escenario = widgets.Dropdown(options=list(ESCENARIOS),description="Escenario",style=estilo,layout=widgets.Layout(width="440px"))
algoritmo_ui = widgets.Dropdown(options=["BFS","UCS","A*"],value="A*",description="Algoritmo",style=estilo)
btn_evaluar = widgets.Button(description="Evaluar mediciones",button_style="info",icon="check")
btn_comparar = widgets.Button(description="Comparar búsquedas",button_style="success",icon="bar-chart")
btn_grafo = widgets.Button(description="Visualizar grafo",icon="sitemap")
salida_monitor = widgets.Output()
salida_busqueda = widgets.Output()
aviso = widgets.HTML(value="<i>Los controles modifican únicamente lecturas simuladas. La búsqueda utiliza solo el caso base validado.</i>")

def aplicar_escenario(change):
    t,s,p = ESCENARIOS[change["new"]]
    temperatura.value=t; salinidad.value=s; ph_control.value=p

def valores_actuales():
    return round(temperatura.value,2),round(salinidad.value,2),round(ph_control.value,2)

def alertas_sin_imprimir(v):
    alertas=[]
    for (nombre,(bajo,alto)),valor in zip(RANGOS.items(),v):
        if not bajo <= valor <= alto:
            alertas.append(f"{nombre}: {valor} fuera de {bajo}–{alto}")
    return alertas

def evaluar(_=None):
    valores=valores_actuales()
    alertas=alertas_sin_imprimir(valores)
    with salida_monitor:
        clear_output(wait=True)
        color="#A11F1F" if alertas else "#176F49"
        status="ALERTA · parámetros fuera de rango" if alertas else "NORMAL · parámetros en rango"
        display(HTML(f"<h3 style='color:{color}'>ACUARIO-IA · {status}</h3>"))
        fig,ax=plt.subplots(1,3,figsize=(12,2.8))
        for e,(titulo,limites),valor,unidad in zip(ax,RANGOS.items(),valores,["°C","ppt",""]):
            low,high=limites
            e.axvspan(low,high,color="#c9f3dc",alpha=.7,label="Rango ilustrativo")
            e.axvline(valor,color="#D64545" if not low<=valor<=high else "#147D77",linewidth=3)
            e.set_xlim(min(valor,low)-2,max(valor,high)+2)
            e.set_yticks([])
            e.set_title(f"{titulo}: {valor} {unidad}",fontsize=10)
            e.legend(fontsize=7,loc="upper right")
        fig.tight_layout();plt.show()
        if alertas:
            for a in alertas: print("⚠",a)
        else: print("✓ Las tres lecturas están dentro de los rangos educativos.")
        if valores!=CASO_BASE:
            print("ℹ Estos valores se monitorizan, pero no se convierten en una nueva ruta de búsqueda.")
        else:
            print("✓ Este escenario coincide con el estado inicial del grafo de 36 nodos.")

def resumen_busquedas(_=None):
    with salida_busqueda:
        clear_output(wait=True)
        nombres=["BFS","UCS","A*"]
        datos=[buscar(nombre) for nombre in nombres]
        fig,axs=plt.subplots(1,3,figsize=(12,3.3))
        for ax,j,titulo in zip(axs,[1,0,2],["Costo total","Número de acciones","Estados expandidos"]):
            valores=[d[1] if j==1 else len(d[0]) if j==0 else d[2] for d in datos]
            bars=ax.bar(nombres,valores,color=["#ee9b28","#1685ac","#33aa91"])
            ax.bar_label(bars,padding=2)
            ax.set_title(titulo); ax.set_ylim(0,max(valores)*1.2)
        fig.suptitle("Comparación real de algoritmos · modelo académico fijo")
        fig.tight_layout();plt.show()
        nombre=algoritmo_ui.value
        ruta,costo,expandidos,frontera=buscar(nombre)
        print(f"Ruta {nombre}: {len(ruta)} pasos · costo {costo} · {expandidos} expandidos · frontera máxima {frontera}")
        anterior=INICIAL
        for i,(accion,c,estado) in enumerate(ruta,1):
            print(f"{i}. {accion} · costo {c} · {valores_reales(anterior)} → {valores_reales(estado)}")
            anterior=estado
        print("Nota: la frontera máxima no equivale a memoria RAM medida.")

def mostrar_grafo(_=None):
    with salida_busqueda:
        clear_output(wait=True)
        print("Grafo fijo del caso base (28 °C, 38 ppt, pH 7.8); no depende de los sliders.")
        visualizar_grafo(algoritmo_ui.value)

escenario.observe(aplicar_escenario,names="value")
btn_evaluar.on_click(evaluar)
btn_comparar.on_click(resumen_busquedas)
btn_grafo.on_click(mostrar_grafo)
display(HTML("<h2>🌊 ACUARIO-IA · Panel interactivo de simulación</h2><p>Fase 3 · Lecturas educativas, algoritmos de búsqueda y resultados visuales</p>"))
display(widgets.VBox([escenario,widgets.HBox([temperatura,salinidad,ph_control]),
                      widgets.HBox([btn_evaluar,btn_comparar,btn_grafo]),algoritmo_ui,aviso]))
display(salida_monitor,salida_busqueda)
evaluar()
