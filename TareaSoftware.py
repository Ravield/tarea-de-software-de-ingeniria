def funcion(x):
	resultado=pow(x,3)+pow(x,2)+x+3
	return resultado

def centrada(x):
	deri=(funcion(x+h)-funcion(x-h))/(2*h)
	return deri

def progresiva(x):
	deri=(funcion(x+h)+funcion(x))/h
	return deri

def regresiva(x):
	deri=(funcion(x)-funcion(x-h))/h
	return deri
def segundaDerivada (x):
	deri=(funcion(x-h)-2funcion(x)+funcion(x-h))/(h²)
	return deri

int x=0
int xfin=1
intervalos=int(input("Ingrese cantidad de nodos internos"))
float h=(1/intervalos)
num_deri=int(input("Ingrese el tipo de derivada a usar"))
print("Centrada=1")
print("Progresiva=2")
print("Regresiva=3")
if num_deri ==1 :
	print(centrada(x))
elif num_deri ==2:
	print(progresiva(x))
elif num_deri ==3:
	print(regresiva(x))





