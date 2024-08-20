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
num1 = 5
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