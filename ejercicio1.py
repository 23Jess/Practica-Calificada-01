#Implemente un algoritmo, usando una función recursiva, que resuelva la siguiente sumatoria: K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p 
# ● El programa debe pedir al usuario que ingrese un número n, y un número P, 
# ● Luego debe calcular el valor de K(n, p) usando una función recursiva, 
#● Debe imprimir el resultado de K(n, p)

def SumatoriaRecursiva(n,p,exp=1): #creamos una funcion recursiva
    if  n == 0: #Se condiciona para cuando el dato ingresado
        k = p - p #
    else:
        k = (p * exp) +  SumatoriaRecursiva(n-1,p,exp + 1) #
    return k
p=int(input('Ingrese un factor:  '))
n=int(input('Ingrese número:  '))
 
print(SumatoriaRecursiva(p,n))

