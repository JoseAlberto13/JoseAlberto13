print("""**Calculadora Básica**
Escribe la operación que deseas realizar:
Suma, Resta, Multiplicacíon o Division.
Puede usar los operadores de cada operación""")


numero1 = int(input("Ingresa el primer número: "))
resultado = 0

while True:

    op = input("Indica la operación que deseas realizar (Suma |Resta |Multiplicacion |Division) o (Salir) para terminar con el programa: ")
    if op.lower() == "salir":
        break
    numero2 = int(input("Ingresa el segundo número: "))
    if op.lower() == "suma" or op == "+":
        resultado = numero1 + numero2
        print(resultado)
    elif op.lower() == "resta" or op == "-":
        resultado = numero1 - numero2
        print(resultado)
    elif op.lower() == "multiplicacion" or op == "*":
        resultado = numero1 * numero2
        print(resultado)
    elif op.lower() == "division" or op == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
            print(resultado)
        else:
            print("Error! No se puede dividir entre cero")
    else:
        print("Hay un error en la operación")
    numero1 = resultado
        
    
"""que lo que """
    