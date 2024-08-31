"""GUIA #2 DE EJERCICOS BÁSICOS EN PYTHON POR EL PROFESOR JUAN DIAZ 2024"""
# Reto 2: 
# Desarrolle todos sus algoritmos solicitando al usuario ingresar la información por teclado

# numero = int(input("ingresa una numero cualquiera : "))

# Ejercicio 1: Escribe un programa que imprima los números del 1 al 10 usando un bucle for.
# Entrada: ?
# Proceso: ?
# Salida: ?
numeros = []
for i in range(1,11):
    numeros.append(i)
print(numeros)

# Ejercicio 2: Modifica el programa anterior para que imprima solo los números pares del 1 al 10.
numeros.clear()
for i in range(2,11,2):
    numeros.append(i)
print(numeros)

# Ejercicio 3: Escribe un programa que imprima los números del 10 al 1 usando un bucle while.
numeros.clear()
x = 10
while x > 0:
    numeros.append(x)
    x-=1    
print(numeros)

# Ejercicio 4: Escribe un programa que pregunte al usuario por un número y determine si es positivo, negativo o cero usando if, elif y else.
def negativo_positivo():
    n = float(input("Ingrese un número, veamos si es positivo o negativo: "))
    if n == 0:
        print(f"El {round(n)} es Cero")
    elif n > 0:
        print(f"El {n} es Positivo")
    else:
        print(f"El {n} es Negativo")
# negativo_positivo()

# Ejercicio 5: Escribe un programa que imprima la tabla de multiplicar del 5 usando un bucle for.
def tablaMultiplicar():
    for i in range(1,11):
        print(f"5 x {i} = {5*i}")
# tablaMultiplicar()

# Ejercicio 6: Modifica el programa anterior para que el usuario elija qué tabla de multiplicar desea imprimir.
def tablaMultiplicar():
    n = int(input("Ingresa un número para mostrar su tabla de multiplicar: "))
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
# tablaMultiplicar()

# Ejercicio 7: Escribe un programa que sume los números del 1 al 100 usando un bucle while.
sumaWhile=0
i = 0
while i < 101 :
    sumaWhile+=i
    i+=1
print(f"La suma de los número del 1 al 100 con while es = {sumaWhile}")

# Ejercicio 8: Crea un programa que pida al usuario una contraseña y continúe pidiéndola hasta que el usuario introduzca la contraseña correcta usando un bucle while.
def contraseñaLoca():
    contraseña = input("Crea una contraseña? : ")
    esContraseña = False
    while not esContraseña:
        verfiContraseña = input("Introduzca la contraseña nuevamente: ")
        if verfiContraseña == contraseña:
            esContraseña = True
            print("Contraseña Correcta")
        else:
            print("Contraseña ingresada es incorrecta")
# contraseñaLoca()

# Ejercicio 9: Escribe un programa que encuentre todos los números entre 1 y 100 que son divisibles por 7 usando un bucle for.
def DivisiblesDe():
    divisiblesx7 = []
    for i in range(7,100,7):
        divisiblesx7.append(i)
    print(divisiblesx7)
# DivisiblesDe()     

# Ejercicio 10: Modifica el programa anterior para que use un bucle while en lugar de for.
def DivisiblesDe():
    divisiblesx7 = []
    i = 7
    while i < 101:
        divisiblesx7.append(i)
        i += 7
    print(divisiblesx7)
# DivisiblesDe()

# Ejercicio 11: Escribe un programa que calcule el factorial de un número proporcionado por el usuario usando un bucle while.
def factorial():
    n= int(input("Ingresa un número entero: "))
    i = n-1
    while i > 0:
        n *= i
        i-=1
    print(f"El factorial del número ingresado es = {n}")
# factorial()

# Ejercicio 12: Crea un programa que utilice un bucle for para imprimir una secuencia de números del 1 al 10, pero que salte el número 5 usando continue.
def usandoContinue():    
    for i in range(1,11):
        if i == 5:
            continue
        print(i)
# usandoContinue()

# Ejercicio 13: Escribe un programa que imprima los números del 1 al 10 y termine el bucle si encuentra el número 6 usando break.
def usandoBreak():    
    for i in range(1,11):
        if i == 6:
            break
        print(i)
# usandoBreak()

# Ejercicio 14: Crea un programa que simule un bucle do-while pidiendo al usuario que introduzca un número positivo y repitiendo mientras el número sea negativo.


# Ejercicio 15: Escribe un programa que pida al usuario un número del 1 al 7 e imprima el día de la semana correspondiente (por ejemplo, 1 para lunes) usando if, elif y else.

# Ejercicio 16: Escribe un programa que cuente la cantidad de números pares e impares del 1 al 100 usando un bucle for.

# Ejercicio 17: Crea un programa que pida al usuario una lista de números y luego imprima el número mayor de la lista.

# Ejercicio 18: Escribe un programa que determine si un número proporcionado por el usuario es un número primo usando un bucle for.

# Ejercicio 19: Modifica el programa anterior para que también imprima todos los números primos entre 1 y 100.

# Ejercicio 20: Crea un programa que utilice un bucle while para imprimir todos los números entre 1 y 50 que sean múltiplos de 3.

# Ejercicio 21: Escribe un programa que pida al usuario una palabra y determine si es un palíndromo (se lee igual de izquierda a derecha y de derecha a izquierda).

# Ejercicio 22: Crea un programa que utilice un bucle for para imprimir la serie de Fibonacci hasta el décimo término.

# Ejercicio 23: Modifica el programa anterior para que el usuario pueda decidir cuántos términos de la serie de Fibonacci imprimir.

# Ejercicio 24: Escribe un programa que cuente cuántas vocales tiene una frase introducida por el usuario.

# Ejercicio 25: Crea un programa que utilice un bucle while para imprimir el alfabeto de la a a la z.

# Ejercicio 26: Escribe un programa que pida al usuario una lista de números y calcule la media de esos números.

# Ejercicio 27: Crea un programa que imprima una pirámide de asteriscos con un número de niveles introducido por el usuario.

# Ejercicio 28: Escribe un programa que simule un juego de adivinanza de números. El programa debe generar un número aleatorio del 1 al 100 y permitir al usuario intentar adivinarlo hasta que acierte.

# Ejercicio 29: Crea un programa que utilice un bucle for para calcular la suma de todos los números impares entre 1 y 100.

# Ejercicio 30: Escribe un programa que pida al usuario una lista de palabras y las ordene alfabéticamente.

# Ejercicio 31: Crea un programa que imprima los números del 1 al 100, pero para múltiplos de tres imprima "Fizz" en lugar del número y para los múltiplos de cinco imprima "Buzz". Para números que son múltiplos de ambos tres y cinco imprima "FizzBuzz".

# Ejercicio 32: Escribe un programa que encuentre el segundo número más grande en una lista de números introducida por el usuario.

# Ejercicio 33: Crea un programa que utilice un bucle for para imprimir una tabla de conversión de grados Celsius a Fahrenheit para los valores de 0 a 100.

# Ejercicio 34: Escribe un programa que simule un bucle do-while que continúe ejecutándose mientras el usuario ingrese una palabra que no sea "salir".

# Ejercicio 35: Crea un programa que utilice un bucle while para invertir una cadena de texto introducida por el usuario.

# Ejercicio 36: Escribe un programa que pida al usuario una lista de números y elimine todos los números duplicados.

# Ejercicio 37: Crea un programa que utilice un bucle for para calcular el número de palabras en una frase proporcionada por el usuario.

# Ejercicio 38: Escribe un programa que pida al usuario un número y calcule su raíz cuadrada utilizando un método de aproximación (como el método de bisección).

# Ejercicio 39: Crea un programa que imprima los primeros 10 números de la secuencia de números perfectos (números cuya suma de divisores propios es igual al número mismo).

# Ejercicio 40: Escribe un programa que genere un patrón de números en forma de triángulo usando bucles anidados.
