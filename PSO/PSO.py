import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Particula:
    
    def __init__(self):
        self.posicion = np.array([np.random.randint(limI[0],limS[0]),np.random.randint(limI[1],limS[1])])
        self.mejorPos = self.posicion
        self.mejorValor = float('inf')
        self.velocidad = np.array([0,0])

    def movimiento(self):
        self.posicion = self.posicion + self.velocidad

    def __str__(self):
        return str("Posicion:" + str(self.posicion) + " ,Mejor Valor:" + str(self.mejorValor))

class Universo:

    def __init__(self):
        self.particulas = []
        self.mejorValG = float('inf')
        self.mejorPosG = np.array([np.random.randint(limI[0],limS[0]),np.random.randint(limI[1],limS[1])])
        self.x = []
        self.y = []
        self.z = []
        self.evolucion = []

    def obtParticulas(self):
        for particula in self.particulas:
            print(particula)

    def evalParticula(self,func):
        for particula in self.particulas:
            valActual = func(particula.posicion[0],particula.posicion[1])
            self.x.append(particula.posicion[0])
            self.y.append(particula.posicion[1])
            self.z.append(valActual)
            if(particula.mejorValor > valActual):
                particula.mejorValor = valActual
                particula.mejorPos = particula.posicion

    def evalGlobal(self,func):
        for particula in self.particulas:
            valActualG = func(particula.posicion[0],particula.posicion[1])
            if(self.mejorValG > valActualG):
                self.mejorValG = valActualG
                self.mejorPosG = particula.mejorPos
                self.evolucion.append(self.mejorValG)

    def sumaTiempo(self):
        for particula in self.particulas:
            global W
            nuevaVelocidad = (W*particula.velocidad)+(c1*np.random.random())*(particula.mejorPos-particula.posicion)+(c2*np.random.random())*(self.mejorPosG-particula.posicion)
            particula.velocidad = nuevaVelocidad
            particula.movimiento()
            





#Funcion a evaluar para el funcionamiento del PSO
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
    #return (np.sin(10*(x ** 2 + y ** 2)))/10
    #return x ** 2 + y ** 2
####################################################
#Se pueden modificar los limites de busqueda
limI = np.array([-10,-10])
limS = np.array([10,10])
####################################################


W = float(input("Ingrese el valor de omega: "))
c1 = float(input("Ingrese el valor de el coeficiente cognitivo: "))
c2 = float(input("Ingrese el valor de el coeficiente social: "))
numParticulas = int(input("Ingrese el numero de particulas en el enjambre: "))
numIter = int(input("Ingrese el numero de iteraciones a realizar: "))



particulasini = [Particula() for _ in range(numParticulas)]
espacio = Universo()
espacio.particulas = particulasini
#espacio.obtParticulas()
for i in range(numIter):
    espacio.evalParticula(f)
    espacio.evalGlobal(f)
    espacio.sumaTiempo()

print("El mejor valor obtenido despues de " + str(numIter) + " es: " + str(espacio.mejorValG) + ", en la posicion: " + str(espacio.mejorPosG))

ax = plt.axes(projection='3d')
ax.scatter(espacio.x, espacio.y, espacio.z, c=espacio.z, cmap='viridis', linewidth=0.5);
plt.show()

xE = []
for i in range(len(espacio.evolucion)):
    xE.append(i)

plt.plot(xE,espacio.evolucion)
plt.show()