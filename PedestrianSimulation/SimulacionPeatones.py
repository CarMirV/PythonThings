import random
import numpy as np
import plotly.graph_objects as go
from dataclasses import dataclass
import matplotlib.pyplot as plt

def movimiento(U,P,tam,nP):
    print(U)
    for i in range(nP*2):
        print("x= "+ str(P[i].x) + " y= " + str(P[i].y))
        if P[i].dir == 1:
            for p in range(P[i].velocidad+1):
                if P[i].x < tam-1:
                    if(U[P[i].y][P[i].x+1]) == 0 and P[i].x != tam-1:
                        U[P[i].y][P[i].x] = 0
                        P[i].x += 1
                        U[P[i].y][P[i].x] = P[i].dir
                    elif P[i].y < tam-1:
                        if(U[P[i].y+1][P[i].x]) == 0 and P[i].y != tam-1:
                            U[P[i].y][P[i].x] = 0
                            P[i].y +=1
                            U[P[i].y][P[i].x] = P[i].dir
        elif P[i].dir == -1:
            for p in range(P[i].velocidad+1):
                if P[i].x > 0:
                    if(U[P[i].y][P[i].x-1]) == 0 and P[i].x != 0:
                        U[P[i].y][P[i].x] = 0
                        P[i].x -=1
                        U[P[i].y][P[i].x] = P[i].dir
                    elif P[i].y > 0:
                        if(U[P[i].y-1][P[i].x]) == 0 and P[i].y != 0:
                            U[P[i].y][P[i].x] = 0
                            P[i].y -=1
                            U[P[i].y][P[i].x] = P[i].dir
        print("x= "+ str(P[i].x) + " y= " + str(P[i].y))
    print(U)

@dataclass
class Peaton:
    dir: int
    velocidad: int
    etiqueta: str
    x: int
    y: int

@dataclass
class Obstaculo:
    x: int
    y: int

tamU = 50
numP = 200
numO = 20
universo = np.zeros((tamU,tamU))


peatones = []
obstaculos = []
for i in range(numP):
    peatones.append(Peaton(-1,np.random.randint(1,2),"PI"+str(i),np.random.randint(0,tamU-1),np.random.randint(0,tamU-1)))
    peatones.append(Peaton(1,np.random.randint(1,2),"PD"+str(i),np.random.randint(0,tamU-1),np.random.randint(0,tamU-1)))

for i in range(numO):
    obstaculos.append(Obstaculo(np.random.randint(0,tamU-1),np.random.randint(0,tamU-1)))
    universo[obstaculos[i].y][obstaculos[i].x] = 3


for i in range(numP*2):
    universo[peatones[i].y][peatones[i].x] = peatones[i].dir

print(universo)


for i in range(10):
    movimiento(universo,peatones,tamU,numP)
    plt.imshow(universo)
    plt.show()



