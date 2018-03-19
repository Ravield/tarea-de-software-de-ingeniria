import math 
def centrada(M,N,H):
	U1 = ((M/(h**2))+(N/2*h))
	U2 = (-2*M/(h**2))
	U3 = ((M/(h**2))-(N/2*h))
	return U1,U2,U3

def progresiva(M,N,H):
        U1 = (M/(h**2))
	U2 = (((-2*M)/(h**2))-(1/h))
	U3 = ((M/(h**2))+(N/h))
	return U1,U2,U3

def regresiva(M,N,H):
	U1 = (M/(h**2)-(N/h))
	U2 = (((-2*M)/(h**2))+(N/h))
        U3 = (M/(h**2))
	return U1,U2,U3


intervalos=int(input("Ingrese cantidad de nodos internos: "))
h = float(1/intervalos) 

#Creo lista A de largo (intervalos-1)
A = [0] * (intervalos-1)
#Cada elemento de la lista A será de largo (intervalos-1) [Matriz cuadrada]
for i in range(intervalos-1):
    A[i] = [0] * (intervalos-1)

#Creo lista B [Matriz de una columna]
B = [0] * (intervalos-1)

x_ini=int(input("Ingrese valor de x(0): "))
x_fin=int(input("Ingrese valor de x(1): "))
M=int(input("Ingrese M"))
N=int(input("Ingrese N"))
C=int(input("Ingrese C"))
F=input("ingrese la funcion F(x): ")
print("Aproximaciones")
print("Centrada=1")
print("Progresiva=2")
print("Regresiva=3")
num_apx=int(input("Ingrese el tipo de aproximacion que va a usar: "))
if num_apx ==1 :
	print(centrada(M,N,h))
elif num_apx ==2:
	print(progresiva(M,N,h))
elif num_apx ==3:
	print(regresiva(M,N,h))





