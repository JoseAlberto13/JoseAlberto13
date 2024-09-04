import random

palabras = ["python", "javascript", "ram", "cpu", "gpu", "programador", "analista", "informatico", "informatica", "desarrollo", "software", "hardware"]
palabraSecreta = random.choice(palabras)
palabraMostrar =""
letrasAdivinadas = []
intentos = 0

for esconder in palabraSecreta:
    esconder = "_"
    palabraMostrar += esconder
print(palabraMostrar)

while True:
    palabraMostrar =""
    letra = input("Ingresa una letra brother: ")
    letra = letra[0]
    if letra in letrasAdivinadas:
        print("Ya haz utilizado esta letra!")
    else:
        letrasAdivinadas.append(letra)
        for letra in palabraSecreta:
            if letra in letrasAdivinadas:
                palabraMostrar += letra
            else:
                palabraMostrar +="_"
        intentos +=1
        print(f"{palabraMostrar}  | {intentos}: Intentos")
        if palabraMostrar == palabraSecreta:
            print(f"Haz adivinado la palabra '{palabraSecreta.capitalize()}'! en {intentos}")
            break