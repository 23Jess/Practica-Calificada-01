#Implemente un programa para convertir un número decimal a hexadecimal 
#ejm. el número 8642 en forma hexadecimal es: 21C2

def ConversionDecimalAHexadecimal(): # Esta sera nuestra función principal
    decimal = int(input("Introduzca un numero para la conversión a hexadecimal: ")) # Pedimos los decimales al usuario
    hexadecimal = "" # Se almacenan los valores hexadecimales
    while decimal != 0: # Cambiamos los digitos por los hexadecimales
        rem = CambiarDigitos(decimal % 16) # se llena la varibale "hexadecimal" con los nuevos valores
        hexadecimal = str(rem) + hexadecimal
        decimal = int(decimal / 16)
    print("Resultado: " + hexadecimal) # Mostramos el resultado

def CambiarDigitos(digitos): # Esta funcion traduce los digitos a sus respectivos hexadecimales
    decimales =     [10 , 11 , 12 , 13 , 14 , 15 ]
    hexadecimal = ["A", "B", "C", "D", "E", "F"]
    for c in range(7):
        if digitos == decimales[c - 1]:
            digitos = hexadecimal[c - 1]
    return digitos

ConversionDecimalAHexadecimal()