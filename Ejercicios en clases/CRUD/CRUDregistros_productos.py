import json
import os

# Estructura del json
registro = {
    "productos" : [],
    "proveedores" : [],
    "compras" : [],
    "clientes": [],
    "ventas": []
}


# Direccion y nombre del archivo json
dir = "."
file_name = "registro.json"

# Creación del archivo json
with open(os.path.join(dir, file_name), "w") as file:
    json.dump(registro, file)


# mostrarDatos simplemente imprime el contenido del archivo json
def mostrarDatos(elarchivo):
    with open(elarchivo, "r") as file:
        datas = json.load(file)
        print(json.dumps(datas, indent=4))  # json.dumps() para imprimir bonito