import os
import pandas as pd

# Funciones

# Agregar los datos al registro
def registrar_producto(nombre, cantidad, valor, qstock, fecha, idProduct):
    codigo = nombre.upper()[0:3] + "-" + fecha[3:5] + "-" + str(idProduct)
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
        print("No se encuentran artículos registrados")
    else:
        mostrar = pd.DataFrame(productos)
        print(mostrar)

# Actualiza los elementos si es que se ingresa algún dato, bastante feo esta el código, pero funciona xd 
def actualizar_producto(nID,nombre, cantidad, valorUnit, qStock, fecha, codigo):
    if len(nombre) > 0:
        productos["nombre"][nID] = nombre
    if len(cantidad) > 0:
        productos["cantidad"][nID] = int(cantidad)
    if len(valorUnit) > 0:
        productos["valor_unitario"][nID] = float(valorUnit)
    if len(qStock) > 0:
        productos["limite_quiebre_stock"][nID] = float(qStock)
    if len(fecha) > 0:
        productos["fecha_ingreso_bodega"][nID] = fecha
    if len(codigo) > 0:
        productos["codigo_producto"][nID] = codigo
    print("Producto Actualizado Exitosamente")

# Eliminar producto por indice
def eliminar_producto(nID):
    productos["id"].pop(nID)
    productos["nombre"].pop(nID)
    productos["cantidad"].pop(nID)
    productos["valor_unitario"].pop(nID)
    productos["limite_quiebre_stock"].pop(nID)
    productos["fecha_ingreso_bodega"].pop(nID)
    productos["codigo_producto"].pop(nID)
    print("Producto Eliminado!")

# Buscar producto por su indice, para mostrarlo en forma de tabla lo hice con chatgpt, asi que hay que estudiar un poquito mas
def buscar_prodcuto(nID):
    df = pd.DataFrame(productos)
    
    # Filtrar el DataFrame por el ID del producto
    producto = df[df["id"] == nID]
    # Imprimir el producto en formato de tabla sin mostrar el índice
    print(producto.to_string(index=False))    
        
# Suma el total del valor del o los articulos, habra que estudiar más sobre como mostrar los datos de una manera más sencilla y bonita.
def suma_totales(nID):
    if nID == 1:
        suma = 0
        for i in range(0,len(productos["id"])):
            print(f"{productos["cantidad"][i]} {productos["nombre"][i]} = {productos["cantidad"][i]*productos["valor_unitario"][i]}")
            aux = productos["valor_unitario"][i]*productos["cantidad"][i]
            suma += aux
        return suma
    elif nID not in productos["id"]:
        print("Ingresa un ID válido")
    else:
        i = productos["id"].index(nID)
        return f"Producto:{productos["nombre"][i]} Cant:{productos["cantidad"][i]} Valor Unit:{productos["valor_unitario"][i]} = {productos["cantidad"][i]*productos["valor_unitario"][i]}"

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
    print("\nGESTIÓN DE BODEGA")
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
                nombreProduct = input("Ingrese el nombre del producto: ").title()
                cantidadProduct = int(input(f"Ingrese la cantidad recepcionada de {nombreProduct}: "))
                valorUnitProduct = float(input("Ingrese el valor unitario del prodcuto: "))
                quiebreStock = float(input("Ingrese el quiebre de stock del producto: "))
                fechaIngresoProduct = input("Ingrese fecha (formato DD/MM/YYYY): ")
                registrar_producto(nombreProduct, cantidadProduct, valorUnitProduct, quiebreStock, fechaIngresoProduct, idProduct)
                idProduct += 1
            except Exception as e:
                print(f"No me hackee D: ERROR '{e}'")

        case "3":
            os.system("cls")
            print("ACTUALIZA INFORMACIÓN DE PRODUCTO")
            try:
                idActual = int(input("Ingrese el 'ID' del producto que desea actualizar u modificar información: "))
                if idBuscar not in productos["id"]:
                    print("El 'ID' ingresado no existe")
                    continue
                print("Si no quiere cambiar la información, ignore el ingreso de datos y presione enter")
                nombreProduct = input("Actualizar nombre del producto: ").title()
                cantidadProduct = (input(f"Actualizar cantidad recepcionada: "))
                valorUnitProduct = (input("Actualizar valor unitario del prodcuto: "))
                quiebreStock = (input(f"Actualizar quiebre del stock: "))
                fechaIngresoProduct = input("Actualizar fecha (formato DD/MM/YYYY): ")
                codProduct = (input("Actualizar código del prodcuto: "))
                actualizar_producto(productos["id"].index(idActual), nombreProduct, cantidadProduct, valorUnitProduct, quiebreStock, fechaIngresoProduct, codProduct) 
            except Exception as e:
                print(f"Ocurrio un error inesperado en la Actualización  de datos {e}")
    
        case "4":
            while True:
                os.system("cls")
                print("ELIMINAR PRODUCTO")
                try:
                    idRemove = int(input("Ingrese el 'ID' del producto que desea eliminar del registro: "))
                    if idRemove not in productos["id"]:
                        print(f"El 'ID' ingresado no existe, ingrese un 'ID' válido")
                        continue
                    eliminar_producto(productos["id"].index(idRemove))
                except Exception as e:
                    print(f"Ocurrio un error inesperado en la Eliminación del producto {e}")
                aux = input("Desea eliminar otro artículo? Pulsa Enter, de lo contrario ingresa 'No' para volver al menú principal): ").lower()
                if aux == "no":
                    break
                
        case "5":
            os.system("cls")
            print("BUSCAR INFORMACIÓN DE PRODUCTO")
            try:
                idBuscar = int(input("Ingrese el 'ID' del producto que desea visualizar en el registro: "))
                if idBuscar not in productos["id"]:
                    print("El 'ID' ingresado no existe")
                    continue
                buscar_prodcuto(idBuscar)
            except Exception as e:
                print(f"Ocurrio un ERROR inesperado  en la búsqueda de datos {e}")

        case "6":
            os.system("cls")
            print("CALCULA EL VALOR DEL INVENTARIO")
            try:
                idCalcul = int(input("Ingrese el 'ID' del producto que desee calcular o ingrese '1' para calcular el total del inventario: "))
                print(f"{suma_totales(idCalcul)}")
            except:
                print("Ingrese un valor válido, invalido")

        case "7":
            os.system("cls")
            print("Saliste del programa\nGracias por confiar en nosotros :D if")
            break