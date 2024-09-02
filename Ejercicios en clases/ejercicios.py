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
def sumaDenumerosNaN():
    sumaWhile=0
    i = 0
    while i < 101 :
        sumaWhile+=i
        i+=1
    print(f"La suma de los número del 1 al 100 con while es = {sumaWhile}")
# sumaDenumerosNaN()

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
def dowhileSemiuleicion():
    while True:
        n = int(input("Ingresa un número positivio: "))
        if n > 0:
            break
    print("Fin del 'do while' xd")
# dowhileSemiuleicion()

# Ejercicio 15: Escribe un programa que pida al usuario un número del 1 al 7 e imprima el día de la semana correspondiente (por ejemplo, 1 para lunes) usando if, elif y else.
def diasSemana():
    dias = ["Salir","Lunes","Martes","Miércorles","Jueves","Viernes","Sábado","Domingo"]
    while True:
        dia = int(input("Ingresa un número del '1 al 7' para mostrar el día de la semana correspondiente (por ejemplo, 1 para lunes)\nPara salir del programa ingresa 0:\nIngresa un número: "))
        if dia == 0:
            print("Saliste del programa")
            break
        elif dia < 0 or dia > 7:
            print("Ingresa un número válido")
        else:
            print(f"{dia} = {dias[dia]}")
# diasSemana()

# Ejercicio 16: Escribe un programa que cuente la cantidad de números pares e impares del 1 al 100 usando un bucle for.
def contando_Pares_Impares():
    pares = 0
    impares = 0
    for i in range(1,101):
        if i % 2 == 0:
            pares +=1
        else:
            impares += 1
    print(f"Cantidad de números pares = {pares}\nCantidad de número impares = {impares}")
# contando_Pares_Impares()

# Ejercicio 17: Crea un programa que pida al usuario una lista de números y luego imprima el número mayor de la lista.
def mayordelaLista():
    listaN = []
    print("Ingresa una serie de números mayores y menores a '0'\nCnuando creas finalizar, para mostrar el mayor números ingresa '0'")
    while True:
        n = float(input("Ingresa un número: "))
        if n == 0:
            break
        listaN.append(n)
    print(listaN)
    print(f"El número mayor de la lista es: {max(listaN)}")
# mayordelaLista()

# Ejercicio 18: Escribe un programa que determine si un número proporcionado por el usuario es un número primo usando un bucle for.
def numeroPrimo():
    n = int(input("Ingresa un número natural (entero y positivo) para determinar si este es primo: "))
    esPrimo = 0
    for i in range(1, n+1):
        if n % i == 0:
            esPrimo += 1
    if esPrimo == 2:
        print(f"El número {n} es Primo")
    else:
        print(f"El número {n} no es Primo")
# numeroPrimo()

# Ejercicio 19: Modifica el programa anterior para que también imprima todos los números primos entre 1 y 100.
def numeroPrimo_100():
    print("Números primos del 1 al 100")
    for i in range(1, 101):
        esPrimo = 0
        for x in range(1,i+1):
            if i % x == 0:
                esPrimo += 1
        if esPrimo == 2:
            print(f"El número {i} es Primo")
# numeroPrimo_100()

# Ejercicio 20: Crea un programa que utilice un bucle while para imprimir todos los números entre 1 y 50 que sean múltiplos de 3.
def numeros_x3_While():
    i = 0
    while i < 50:
        i+=1
        if i % 3 == 0:
            print(i)
# numeros_x3_While()

# Ejercicio 21: Escribe un programa que pida al usuario una palabra y determine si es un palíndromo (se lee igual de izquierda a derecha y de derecha a izquierda).
def palindromo():
    palabra = input("Ingresa una palabra para determinar si es palindromo: ").lower()
    palabraRv = palabra[::-1]
    if palabraRv != palabra:
        print(f"La palabra '{palabra.capitalize()}' no es palindroma")
    else:
        print(f"La palabra '{palabra.capitalize()}' es palindroma")
# palindromo()

# Ejercicio 22: Crea un programa que utilice un bucle for para imprimir la serie de Fibonacci hasta el décimo término.
def fibonacci(n):
    a,b = 0, 1
    for i in range(1,n+1):
        c = a+b
        print(f"Termino #{i} = {a}")
        a = b
        b = c
# fibonacci(10)

# Ejercicio 23: Modifica el programa anterior para que el usuario pueda decidir cuántos términos de la serie de Fibonacci imprimir.
"""Como se me encendió el foco, no volvere a escribir el código, ya que estoy haciendo funciones, simplemente las llamare con un input xd"""
# fibonacci(int(input("Ingresa cuántos términos de la serie de Fibonacci desea imprimir: ")))

# Ejercicio 24: Escribe un programa que cuente cuántas vocales tiene una frase introducida por el usuario.
def cuentaVocales():
    vocales = "aeiouáéíóú"
    count = 0
    palabra = input("Ingresa una palabra o frase, contaremos la cantidad de vocales que tiene: ")
    palabraAux = palabra.lower()
    for i in palabraAux:
        if i in vocales:
            count += 1
    print(f"'{palabra}' tiene una cantidad de {count} vocales")
# cuentaVocales()

# Ejercicio 25: Crea un programa que utilice un bucle while para imprimir el alfabeto de la a a la z.
import string
def alfabetoWhile():
    alfabeto = list(string.ascii_lowercase) #Metodo de la biblioteca string, transformamos en una lista para efecto practico del ejercicio del buen profesor xd unico detalle es que no tiene agregada la "ñ"
    i = 0
    while i < len(alfabeto):
        print(alfabeto[i])
        i += 1
# alfabetoWhile()

# Ejercicio 26: Escribe un programa que pida al usuario una lista de números y calcule la media de esos números.
def promedio_media():
    listaN = []
    while True:
        n = float(input("Ingresa un número: "))
        listaN.append(n)
        media = sum(listaN) / len(listaN)
        print(f"Lista: {listaN}\nMedia = {media}")
# promedio_media()

# Ejercicio 27: Crea un programa que imprima una pirámide de asteriscos con un número de niveles introducido por el usuario.
def piramide():
    n = int(input("Ingresa el nivel de pisos para la piramide: "))
    for i in range(1,n+1):
        print(" " * (n-i) + "*" * (i*2-1))
# piramide()

# Ejercicio 28: Escribe un programa que simule un juego de adivinanza de números. El programa debe generar un número aleatorio del 1 al 100 y permitir al usuario intentar adivinarlo hasta que acierte.
import random
def adivinarNumero():
    print("Intenta adivinar el número!\nAdivina el número secreto entre el '1 y 100'")
    nSecreto = random.randint(1,100)
    print(nSecreto)
    intentos = 0
    while True:
        nUser = int(input("Ingresa tu número: "))
        intentos += 1
        if nUser == nSecreto:
            print(f"Bien hecho! haz adivinado en {intentos} intentos")
            break
        elif nUser > nSecreto:
            print("Buen intento, el número secreto es menor")
        elif nUser < nSecreto:
            print("Buen intento, el número secreto es mayor")
# adivinarNumero()

# Ejercicio 29: Crea un programa que utilice un bucle for para calcular la suma de todos los números impares entre 1 y 100.
def sumaForImpares():
    suma = 0
    for i in range(1,101,2):
        suma += i
    print(f"El resultado de la suma de todos los números impares es = {suma}")
# sumaForImpares()

# Ejercicio 30: Escribe un programa que pida al usuario una lista de palabras y las ordene alfabéticamente.
def ordenarPalabras():
    listaOrd = []
    while True:
        palabras = input("Añade una palabra a la lista: ")
        listaOrd.append(palabras)
        listaOrd.sort()
        print(listaOrd)
# ordenarPalabras()

# Ejercicio 31: Crea un programa que imprima los números del 1 al 100, pero para múltiplos de tres imprima "Fizz" en lugar del número y para los múltiplos de cinco imprima "Buzz". Para números que son múltiplos de ambos tres y cinco imprima "FizzBuzz".
def FizzBuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
# FizzBuzz()

# Ejercicio 32: Escribe un programa que encuentre el segundo número más grande en una lista de números introducida por el usuario.
def segundoMayor():
    listaN = []
    print("Ingresa una serie de números, se añadiran a una lista\ncuando quieras saber cual fue el segundo número más grande de la lista ingresa un Cero '0'")
    while True:
        n = int(input("Añade un número a la lista: "))
        if n == 0:
            print(f"Tu lista: {listaN}")
            listaN.remove(max(listaN))  #Igual pude usar sort y luego imprimir el indice len-2, pero queria probar si de alguna manera el metodo max era capaz de hacerlo xd
            break
        listaN.append(n)
    print(f"El segundo número más grande ingresado fue el {max(listaN)}")
# segundoMayor()

# Ejercicio 33: Crea un programa que utilice un bucle for para imprimir una tabla de conversión de grados Celsius a Fahrenheit para los valores de 0 a 100.
def Celsius_Fahrenheit():
    for celsius in range(101):
        fahrenheit = (celsius * 9/5) + 32
        print(f"C {celsius}° = F {fahrenheit}°")
# Celsius_Fahrenheit()

# Ejercicio 34: Escribe un programa que simule un bucle do-while que continúe ejecutándose mientras el usuario ingrese una palabra que no sea "salir".
def aburrido():
    while True:
        entrada = input("Simplemente escribe... no hace nada, si quieres salir del programa, escribe 'Salir': ").lower()
        match entrada:
            case "salir":
                break
            case _:
                pass
    print("Saliste del programa :D")
# aburrido()
    
# Ejercicio 35: Crea un programa que utilice un bucle while para invertir una cadena de texto introducida por el usuario.
def invertirCaracter():
    texto = input("Escribe un texto para invertir: ")
    invTexto = ""
    i = 0
    while i < len(texto):
        i += 1
        invTexto += texto[i*-1]
    print(invTexto)
# invertirCaracter()

# Ejercicio 36: Escribe un programa que pida al usuario una lista de números y elimine todos los números duplicados.
def eliminarNDuplicados():
    listaN = []
    print("Añade números a una lista, ingresa '0' cuando estes listo para eliminar los duplicados")
    while True:
        n = int(input("Ingresa el número: "))
        if n == 0:
            listaN = list(set(listaN))
            print("Duplicados Eliminados ✓")
            print(listaN)
        else:
            listaN.append(n)
            print(listaN)
            print("Número agregado ✓")               
# eliminarNDuplicados()

# Ejercicio 37: Crea un programa que utilice un bucle for para calcular el número de palabras en una frase proporcionada por el usuario.
def cuentaPalabras():
    frase = input("Ingresa una frase: ")
    count = 1
    for palabra in frase:
        if palabra == " ":
            count +=1
    print(f"La frase tiene {count} palabras")
# cuentaPalabras()

# Ejercicio 38: Escribe un programa que pida al usuario un número y calcule su raíz cuadrada utilizando un método de aproximación (como el método de bisección).


# Ejercicio 39: Crea un programa que imprima los primeros 10 números de la secuencia de números perfectos (números cuya suma de divisores propios es igual al número mismo).


# Ejercicio 40: Escribe un programa que genere un patrón de números en forma de triángulo usando bucles anidados.
def navidad_xd(n):
    for i in range(1,n+1):
        for x in range(i):
            print(" " * ((n*2-i)-x-1) + str(i)*(((i)*2-1)+x+x)) # Debo estudiar más sobre ciclos y algoritmos de patrones... se me complicó xd