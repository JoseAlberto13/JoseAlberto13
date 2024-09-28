import os
import pandas as pd

# Funciones

# Agregar los datos al registro
def registrar_producto(nombre, cantidad, valor, qstock, fecha, idProduct):
    codigo = nombre.upper()[0:3] + "-" + fecha[2] + "-" + str(idProduct)
    productos["id"].append(idProduct)
    productos["nombre"].append(nombre)
    productos["cantidad"].append(cantidad)
    productos["valor_unitario"].append(valor)
    productos["limite_quiebre_stock"].append(qstock)
    productos["fecha_ingreso_bodega"].append(fecha)
    productos["codigo_producto"].append(codigo)
    print("Producto Ingresado Exitosamemte")

# Mostrar todos los datos dentro del registro
def visualizar_productos():
    if len(productos["id"]) == 0:
        print("No se encuentran datos registrados")
    else:
        mostrar = pd.DataFrame(productos)
        print(mostrar)

def actualizar_producto():
    pass

def eliminar_producto():
    pass

def buscar_prodcuto():
    pass

def suma_totales():
    pass

# Main

# Definimos la estructura del regisro
productos = {}
productos["id"] = []
productos["nombre"] = []
productos["cantidad"] = []
productos["valor_unitario"] = []
productos["limite_quiebre_stock"] = []
productos["fecha_ingreso_bodega"] = []
productos["codigo_producto"] = []

# ID inicial xd para que no se repitan, cuando aprenda a hacer un ID bien ahí después me critican 
idProduct = 201

while True:
    print("GESTIÓN DE BODEGA")
    opcion = input("""Elige una de las siguientes opciones
1. Listar Productos
2. Registrar Producto
3. Actualizar Producto
4. Eliminar Producto
5. Buscar Producto
6. Calcular Totales
7. Salir
""")


    match opcion:
        case "1":
            os.system("cls")
            print("LISTADO DE PRODUCTOS")
            visualizar_productos()
        case "2":
            os.system("cls")
            print("REGISTRAR PRODUCTOS")
            try:
                nombreProduct = input("Ingrese el nombre del producto: ").capitalize()
                cantidadProduct = int(input(f"Ingrese la cantidad recepcionada de {nombreProduct}: "))
                valorUnitProduct = float(input("Ingrese el valor unitario del prodcuto: "))
                quiebreStock = "???"
                fechaIngresoProduct = input("Ingrese fecha (formato DD/MM/YYYY): ")
                registrar_producto(nombreProduct, cantidadProduct, valorUnitProduct, quiebreStock, fechaIngresoProduct, idProduct)
                idProduct += 1
            except Exception as e:
                print(f"No me hackee D: ERROR {e}")
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            print("Saliste del programa\nGracias por confiar en nosotros :D if")
            break