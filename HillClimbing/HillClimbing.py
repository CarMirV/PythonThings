import numpy as np

def hillClimb(valact,norte,sur,este,oeste,dron,universo,lim):
    for x in range(10):
        if(dron[0]!=0):
            norte = universo[dron[0]-1][dron[1]]
        else:
            norte = 0
        if(dron[0]!=lim-1):
            sur = universo[dron[0]+1][dron[1]]
        else:
            sur = 0
        if(dron[1]!=lim-1):
            este = universo[dron[0]][dron[1]+1]
        else:
            este = 0
        if(dron[1]!=0):
            oeste = universo[dron[0]][dron[1]-1]
        else:
            oeste = 0
        if(valact <= norte):
            valact = norte
            dron[0]+=-1
            print(f"El dron se encuentra en la posicion{dron}")
            print(f"El valor actual es {valact}")
        elif(valact <= este):
            valact = este
            dron[1]+=1
            print(f"El dron se encuentra en la posicion{dron}")
            print(f"El valor actual es {valact}")
        elif(valact <= sur):
            valact = sur
            dron[0]+=1
            print(f"El dron se encuentra en la posicion{dron}")
            print(f"El valor actual es {valact}")
        elif(valact <= oeste):
            valact = oeste
            dron[1]+=-1
            print(f"El dron se encuentra en la posicion{dron}")
            print(f"El valor actual es {valact}")
    print(f"El valor final maximo encontrado se encuentra en la posicion: {dron} con un valor de: {valact}")
    print(f"Los valores a su alrededor son N:{norte},E:{este},S:{sur},O:{oeste}")


limite = 20
universo = np.random.randint(25,size=(limite,limite))
print(universo)
dron = np.random.randint(limite,size=(2))
print(dron)
valact = universo[dron[0]][dron[1]]
print(valact)
norte = 0
sur = 0
este = 0
oeste = 0
hillClimb(valact,norte,sur,este,oeste,dron,universo,limite)
