import numpy as np

def dosCambio(universo):
    optimo = 1000
    for base in range(4):
           tot = 0
           visitare = [0,1,2,3]
           visitare.remove(base)
           visAux = visitare.copy()
           iteracion = 1
           for i in visitare:
                print("ITER " + str(base) + "." + str(iteracion))
                print(visitare)
                print("Estoy en la ciudad " + str(base))
                tot += universo[base][i]
                visitare.remove(i)
                print("viaje a la ciudad " + str(i) + " con un costo " + str(universo[base][i]))
                print(visitare)
                if universo[i][visitare[0]] < universo[i][visitare[1]]:
                    print("viaje a la ciudad " + str(visitare[0]) + " con un costo " + str(universo[i][visitare[0]]))
                    tot += universo[i][visitare[0]]
                    print("viaje a la ciudad " + str(visitare[1]) + " con un costo " + str(universo[visitare[0]][visitare[1]]))
                    tot += universo[visitare[0]][visitare[1]]
                else:
                    print("viaje a la ciudad " + str(visitare[1]) + " con un costo " + str(universo[i][visitare[1]]))
                    tot += universo[i][visitare[1]]
                    print("viaje a la ciudad " + str(visitare[0]) + " con un costo " + str(universo[visitare[1]][visitare[0]]))
                    tot += universo[visitare[1]][visitare[0]]
                if tot < optimo:
                    optimo = tot
                print("Este viaje tuvo un costo de " + str(tot))
                visitare = visAux.copy()
                iteracion += 1
           print("\n")
    print("El viaje mas optimo tiene un costo de " + str(optimo))


A = np.random.randint(10,size=(4,4))
print(A)
dosCambio(A)

