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


intervalos=int(input("Ingrese cantidad de nodos internos"))
h = float(1/intervalos) 
x_ini=int(input("Ingrese valor de x(0)"))
x_fin=int(input("Ingrese valor de x(1)"))
M=int(input("Ingrese M"))
N=int(input("Ingrese N))
C=int(input("Ingrese C"))
F=input("ingrese la funionF(x)")
num_deri=int(input("Ingrese el tipo de derivada a usar"))
print("Centrada=1")
print("Progresiva=2")
print("Regresiva=3")
if num_deri ==1 :
	print(centrada(x,h))
elif num_deri ==2:
	print(progresiva(x,h))
elif num_deri ==3:
	print(regresiva(x,h))





