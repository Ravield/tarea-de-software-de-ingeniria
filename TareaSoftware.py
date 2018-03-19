import math 
intervalos=int(input("Ingrese cantidad de nodos internos: "))
h = float(1/(intervalos+1)) 
print(h)
#Creo lista A de largo (intervalos-1)
A = [0] * (intervalos)
#Cada elemento de la lista A será de largo (intervalos-1) [Matriz cuadrada]
for i in range(intervalos):
    A[i] = [0] * (intervalos)

#Creo lista B [Matriz de una columna]
B = [0] * (intervalos-1)

x_ini=int(input("Ingrese valor de x(0): "))
x_fin=int(input("Ingrese valor de x(1): "))
M=int(input("Ingrese M: "))
N=int(input("Ingrese N: "))
C=int(input("Ingrese C: "))
F=math.sin(math.pi/2)
print(F)
print("Aproximaciones")
print("Centrada=1")
print("Progresiva=2")
print("Regresiva=3")
num_apx=int(input("Ingrese el tipo de aproximacion que va a usar: "))
if num_apx ==1 :
        U1 = ((M)+(h*N/2))
        U2 = (-2*M)
        U3 = ((M)-(h*N/2))
        
elif num_apx ==2:
        U1 = (M)
        U2 = ((-2*M)-(N*h))
        U3 = ((M)+(h*N))
        
elif num_apx ==3:
        U1 = (M-(N*h))
        U2 = ((-2*M)+(N*h))
        U3 = (M)
        
	
for i in range(intervalos):
        for j in range(intervalos):
                if i==j :
                        A[i][j]= U2
                elif j == i+1:
                        A[i][j]= U3
                elif j == i-1:
                        A[i][j]= U1
                else:
                        A[i][j]= 0
print("la matriz A es la siguiente:")
print('\n'.join([''.join(['{:10}'.format(item) for item in row]) 
      for row in A]))

for i in range(intervalos):
        print(i)
        if i == 0:
                B[i] = h**2*(F-C)-(x_ini)
                print(B)
        elif i == intervalos-1:
                B[i] =  h**2*(F-C)-(x_fin)
        else:
                B[i] =  h**2*(F-C)
print("la metriz B es:")
print(B)
