"""GUIA DE EJERCICOS BÁSICOS EN PYTHON POR EL PROFESOR JUAN DIAZ 2024"""

# 1 "Operaciones Matemáticas Simples: Escribre un programa que sume, reste, multiplique y divida dos números" 
num1 = 13 #podemos hacer la petición con float(input("")) para ahorrarme las entradas las definire directamente
num2 = 4
print(f"Suma = {num1 + num2}")
print(f"Resta = {num1 - num2}")
print(f"Multiplicación = {num1 * num2}")
print(f"División = {num1 / num2}")

# 2 "Conversion de Grados: Convierte grados Celsius a Fahrenheit"
grados_C = 26
grados_F = grados_C * 9/5 + 32
print(f"{grados_C} C° equivalen a {grados_F} F°")

# 3 "Números Pares e Impares: Dado un número, determina si es par o impar"
num1 = 1998
if num1 % 2 == 0:
    print(f"{num1} es Par")
else:
    print(f"{num1} no es Par")
    
# 4 "Mayor de Tres Números: Escribe un programa que encuentre el mayor de tres números dados"
num1 = 13 # podemos hacer la petición con float(input())
num2 = 4
num3 = 98
if num1 > num2 and num1 > num3:
    print(f"{num1} Es el mayor de los tres números")
elif num2 > num1 and num2 > num3:
    print(f"{num1} Es el mayor de los tres números")
else:
    print(f"{num3} Es el mayor de los tres números")
    
# 5 "Suma de Números en un Rango: Calcula la suma de todos los números del 1 al 100"
suma = 0
for i in range(1,101):
    suma += i  #El ejercicios se puede resolver con la fórmula de sucesión de Gauss
print(suma)

# 6 "Factorial de Número: Calcula el factorial de un número dado"
num1 = 6
factorial = num1
for i in range(1,num1):
    factorial *= i 
print(f"El factorial de {num1} = {factorial}")

# 7 "Número Primo: Verifica si un número es primo"
num1 = 73
count = 0
for i in range(1,num1+1):
    if num1 % i == 0:
        count+=1
if count == 2:
    print(f"{num1} Es un número primo")
else:
    print(f"{num1} No es un número primo")
    
# 8 "Tabla de Multiplicar: Genera la tabla de multiplicar de un número dado"
num1 = 5 # int(input("Ingresa tu número: ")) #Lo comento para que no moleste xd
for i in range(1,11):
    resultado = num1 * i
    print(f"{num1} x {i} = {resultado}")

# 9 "Adivina el Número: Escribe un programa donde el usuario debe adivinar un número entre 1 y 10"
print('Deberás adivinar el número secreto "entre 1 hasta el 10"')
num_secret = 7
while True:
    num1 = 7 # int(input("Ingresa tu número: ")) #Lo comento para que no moleste xd
    if num1 != num_secret:
        print("Pfff Intentalo de nuevo")
    else:
        print("Wow lo conseguiste! Bien hecho")
        break

# 10 "Verifica si una palabra es palíndromo"
palabra = "Reconocer"
palabra = palabra.lower()
palabra_reverse = palabra[::-1]
if palabra == palabra_reverse:
    print("Es palindromo")
else:
    print("No es palindromo")
    
# 11 "Contador de Vocales: Cuenta el número de vocales en una cadena de texto"
palabra = "Paraledepipedo" # (7 vocales)
vocales = ["a", "e", "i", "o", "u"]
count_v = 0
for i in palabra:
    if i in vocales:
        count_v +=1
print(f"La palabra tiene {count_v} vocales")

# 12 "Contador de Palabras: Cuenta cuantas palabras tiene una oración dada"
oracion = "" # (7 palabras)
count_w = 0
for i in oracion:
    if i == " ":
        count_w +=1
print(count_w+1)    #Ok, esta es la solución más simple y básica que conozco, bastante mejorable la verdad

# 13 "Invertir una Cadena: Escribe un programa que invierta el orden de los caracteres en una cadena"
palabra = "Hola Python"
palabra_reverse = palabra[::-1]
print(palabra_reverse)

# 14 "Mayor y Menor en una Lista: Encuentra el número mayor y menor en una lista de números"
lista = [4, 12, 34, 1, 2, 443, -52, 98]
max_lista = max(lista)
min_lista = min(lista)
print(f"El Mayor es {max_lista}\nEl Menor es {min_lista}")

# 15 "Promedio de una Lista: Calcula el promedio de una lista de números"
lista = [42, 12, 34, 55, 25, 43, 52, 48]
promedio_lista = sum(lista)/len(lista)
print(f"El Promedio de la lista es = {promedio_lista}")

# 16 "Elimina los duplicados: Elimina los elementos duplicados de una lista"
lista_num = [1, 1, 2, 3, 4, 6, 2, 3, 5, 3, 7, 6]
lista_str = ["Hola", "Como", "Estas", "?", "Como", "Estas", "Usando", "Python", "?"]
print(lista_num)
print(lista_str)

lista_num = set(lista_num)
lista_str = set(lista_str)
print(lista_num)
print(lista_str)

# 17 "Múltiplos de 3 y 5: Imprime todos los múltiplos de 3 y 5 entre 1 y 100"
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} Multiplo de 3 y 5")
    # elif i % 3 == 0:
    #     print(f"{i} Multiplo de 3")
    # elif i % 5 == 0:
    #     print(f"{i} Multiplo de 5")  # por si acaso lo escribí tambien xd
    
# 18 "Número Fibonacci: Genera la seria de Fibonacci hasta un número n dado"
limite_f = 39 #int(input("Ingresa un número entero para el limite de la serie de Fibonacci: ")) #comentado para que no moleste
a, b, c = 0, 1, 0
while True:
    c = a + b
    if c <= limite_f:
        print(f"{a} + {b} = {c}")
        a = b
        b = c
    else:
        break
    
# 19 "Número Capicúa: Verifica si un número es capicúa (se lee igual al derecho y al revés)"
while True:
    try:
        num1 = 3223 #int(input("Ingresa un número: ")) #comentado para que no moleste
        num_str = str(num1)
        num_capicua = num_str[::-1]
        if num_str == num_capicua:
            print("El Número es Capicua")
            break
        else:
            print("No es Capicua")
            break
    except:
        print("Ingresa un fokin numero!")
        
# 20 "Ordenar Números: Ordena una lista de números de menor a mayor"
lista = [4, 12, 34, 1, 2, 443, -52, 98]
lista.sort()
print(lista)  #Para solo mostrar los números ordenados sin modificar sus indices, podemos usar la función sorted()
print(sorted(lista))

# 21 "Calculadora Básica: Crea una calculadora simple que permita sumar, restar, multiplicar, y dividir dos números"
# print("Calculadora Básica")
# while True:
#     print("\nOperaciones ('sumar' o '+') ('restar' o '-') ('multiplicar' o '*') ('dividir' o '/')\nSi desea salir del programa ('salir' o 'x')\n")
#     num1 = float(input("Ingresa el primer número: "))
#     op = input("Indica la operación: ")
#     if op == "salir" or op == "x":
#         break
#     num2 = float(input("Ingresa el segundo número: "))
    
#     if op == "sumar" or op == "+":
#         print(f"Resultado = {num1 + num2}")
#     elif op == "restar" or op == "-":
#         print(f"Resultado = {num1 - num2}")
#     elif op == "multiplicar" or op == "*":
#         print(f"Resultado = {num1 * num2}")
#     elif op == "dividir" or op == "/":
#         if num2 != 0:
#             print(f"Resultado = {num1 / num2}")
#         else:
#             print("Error! No se puede dividir entre CERO")
#     else:
#         print("Error en la operación")

# 22 "Convertir Horas a Segundos: Convierte una cantidad de horas a segundos"
horas = 2 #float(input("Ingrese la cantidad de horas que quiera convertir a segundos: "))
segundos_hora = int(horas * 3600)
print(f"{horas} Horas a Segundos {segundos_hora}")

# 23 "Número de Dígitos: Calcula cuántos dígitos tiene un número"
num1 = 2
print(f"el {num1} tiene {len(str(num1))} dígito(s)") #podemos usar condicionales para mostrar el mensaje exacto

# 24 "Suma de Dígitos: Suma todos los dígitos de una número"
num1 = 123
num2 = 456
suma_digit = str(num1) + str(num2)
print(suma_digit)

# 25 "Área de un Círculo: Calcula el área de un círculo dado su radio."
radio = 12
area = 3.14159265 * (radio*radio)
print(f"El área es = {area}")

# 26 "Conversión de Moneda: Convierte una cantidad de dinero de una moneda a otra (USD a EUR)"
monto_USD = 22
valor_EUR = 0.89
conv_USD_EUR = monto_USD * valor_EUR
print(f"{monto_USD} USD = {round(conv_USD_EUR,2)} EUR") #La función round(numero) redondea el valor que le indiquemos, si tiene decimales podemos indicar la cantidad que deba mostranos round(numero, cant. decimales a mostrar)

# 27 "Determinar Edad: Calcula la edad de una persona dada su fecha de nacimiento"
año_actual = 2024
año_nacimiento = 1998
print(f"Tienes {año_actual - año_nacimiento} años")

# 28 "Piedra, Papel o Tijera: Implemente el juego de piedra, papel o tijera. (Usuario vs Computadora)"
import random
mov = ["piedra", "papel", "tijera"]
print('Juega al Piedra, Papel o Tijera contra la PC :D "Escribe tu elección"\nGana el mejor de tres')
wins_USER = 0
wins_PC = 0
combats = 0
while combats < 3:
    mov_USER = input("Elige tu movimiento: ")
    mov_USER = mov_USER.lower() #para que no falle en la escritura de las opciones que elija mi agradable usuario
    mov_PC = random.choice(mov) #La función choice(colección) de la libreria de ramdon, nos permite hacer una elección aleatoria dentro de una coleccion de elementos
    if mov_USER not in mov: #si el mov del usuario no es correcto, lo mandamos a freir mono
        print("Elige entre Piedra, Papel o Tijera! Inteligente...")
    elif mov_USER == "piedra" and mov_PC == "tijera" or mov_USER == "tijera" and mov_PC == "papel" or mov_USER == "papel" and mov_PC == "piedra": #escenarios donde el usuario gana
        wins_USER += 1
        combats += 1
        print(f"Elegiste {mov_USER} vs {mov_PC}\nGanaste!")
    elif mov_PC == "piedra" and mov_USER == "tijera" or mov_PC == "tijera" and mov_USER == "papel" or mov_PC == "papel" and mov_USER == "piedra": #escenarios donde el pc gana
        wins_PC += 1 
        combats += 1
        print(f"Elegiste {mov_USER} vs {mov_PC}\nLa PC Gana")
    else:
        combats += 1
        print(f"Elegiste {mov_USER} vs {mov_PC}\nEmpate!")
        
print(f"Combates: {combats}\nJugador: {wins_USER}\nPC: {wins_PC}") #damos información del enfrentamiento entre el pc y el usuario :D
if wins_USER == wins_PC:
    print("Empate, No hay Ganadores!") 
elif wins_USER > wins_PC:
    print("¡Felicitaciones, Eres el Ganador!")
else:
    print("Buen Intento, La PC Gana :C")
    
# 29 "Conteo Regresivo: Crea un contador que cuente hacia atrás desde un número n hasta 0"
num1 = 3
for i in range(0,num1+1):
    print(num1-i)
    
# 30 "Divisores de un Número: Encuentra todos los divisores de un número dado"
num1 = 27
for i in range(1,num1+1):
    if num1 % i == 0:
        print(i)