import random
import numpy as np
import plotly.graph_objects as go
from dataclasses import dataclass

def avance(U, autos, nAutos, tam, reg):
    nAutos = nAutos
    for i in range(nAutos):
        posA = autos[i].pos
        for p in range(0,autos[i].v+1):
            if posA+p < tamU:
                if universo[posA+p] == "x" or universo[posA+p] == autos[i].etiqueta:
                       universo[posA+p] = autos[i].etiqueta
                       if p != 0:
                            universo[posA+(p-1)] = "x"
                            autos[i].pos = posA+p
                       if autos[i].v < autos[i].vmax:
                            autos[i].v += 1
                else:
                    autos[i].v = 1
                    break
            elif posA+p >= tam:
                universo[tam-1] = "x"
                posA = 0
        reg[i] = autos[i].pos
    print(reg)
    print(U)
    

@dataclass
class Auto:
    etiqueta: str
    v: int
    vmax: int
    prob: float
    pos: int


tamU = 200
autosN = 30
numIter = 30

lista = []
universo = ["x"]*tamU
for i in range(autosN):
    lista.append(Auto("A"+str(i),0,np.random.randint(2,5),random.random(),np.random.randint(tamU)))
    lista[i].v = np.random.randint(1,lista[i].vmax)
    universo[lista[i].pos]=lista[i].etiqueta
print(universo)

iteraciones = []
for i in range(numIter):
    posiciones = [0]*autosN
    iteraciones.append(posiciones)
for i in range(numIter):
    avance(universo,lista,autosN, tamU,iteraciones[i])

tiempos = []
for i in range(numIter):
    tmp = ["t"+str(i)]*autosN
    tiempos.append(tmp)

fig = go.Figure()
for i in range(numIter):
    fig.add_trace(go.Scatter(
    x=iteraciones[i],
    y = tiempos[i],
    marker=dict(color="crimson", size=12),
    mode="markers",
    name="tiempo"+str(i),
    ))

fig.show()

