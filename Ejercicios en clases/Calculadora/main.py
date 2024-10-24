#import sys

#sys.path.append(r"c:/Users/josea/OneDrive/Documentos/1er Semestre CFT/Programación/JoseAlberto13-Git/JoseAlberto13/Ejercicios en clases/Calculadora/functions")
import functions as fns

print("""**Calculadora Básica**
Escribe la operación que deseas realizar:
Suma, Resta, Multiplicacíon o Division.
Puede usar los operadores de cada operación""")


while True:
    numero1 = int(input("Ingresa el primer número: "))
    operation = input("Indica la operación que deseas realizar (Suma |Resta |Multiplicacion |Division) o (Salir) para terminar con el programa: ")
    if operation.lower() == "salir":
        break
    numero2 = int(input("Ingresa el segundo número: "))
    if operation.lower() == "suma" or operation == "+":
        resultado = fns.sumar(numero1,numero2)
        print(f"resultado = {resultado}")
    elif operation.lower() == "resta" or operation == "-":
        resultado = fns.restar(numero1,numero2)
        print(f"resultado = {resultado}")
    elif operation.lower() == "multiplicacion" or operation == "*":
        resultado = fns.multiplicar(numero1, numero2)
        print(f"resultado = {resultado}")
    elif operation.lower() == "division" or operation == "/":
        if numero2 != 0:
            resultado = fns.dividir(numero1, numero2)
            print(f"resultado = {resultado}")
        else:
            print("Error! No se puede dividir entre cero")
    else:
        print("Hay un error en la operación")
    numero1 = resultado
