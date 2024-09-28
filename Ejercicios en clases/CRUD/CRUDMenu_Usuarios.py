import os
import CRUDregistros_productos as reg
import json

adminUser = ({
    "user": "admin",
    "password": "admin123"
})

def addEProduct(file, name, quantity, price,):
    with open(file, "r") as file1:
        reg.registro = json.load(file1)
    reg.registro["productos"].append({
        "nombre": name,
        "cantidad": quantity,
        "precio": price
    })
    
    with open(file,"w") as file2:
      json.dump(reg.registro,file2, indent=4)
    print(f"Producto {name} agregado exitosamente")
    
def addProvider(file,  provider, direction, numberPhone, email):
    with open(file, "r") as file1:
        reg.registro = json.load(file1)
    reg.registro["proveedores"].append({
        "nombre": provider,
        "direccion": direction,
        "contacto": numberPhone,
        "correo": email
    })
    
    with open(file,"w") as file2:
      json.dump(reg.registro,file2, indent=4)    
    print(f"Proveedor {provider} agregado exitosamente")

def menuAdmin():
    print("Inicio de sesión como Administrador")
    inUser = input("Ingrese Usuario: ")
    inPassword = input("Ingrese Contraseña: ")
    try:
        if inUser == adminUser.get("user") and inPassword == adminUser.get("password"):
            while True:
                print("Bienvenido Admin, haga lo que le de la gana :D")
                opcion_Admin = input("1. Agregar Productos\n2. Agregar Proveedores\n3. Visualizar Lista de Clientes\n4. Visualizar Lista de Productos\n5. Visualizar Toda la Información\n6. Actualizar Producto\n7. Eliminar Producto\n0. Salir\n: ")
                
                match opcion_Admin:
                    case "1":
                        os.system("cls")
                        print("Información del Producto")
                        productName = input("Ingrese el nombre del producto: ")
                        productQuantity = int(input("Ingrese la cantidad: "))
                        productPrice = float(input("Ingrese el valor unitario: "))
                        addEProduct(reg.file_name, productName, productQuantity, productPrice)

                    case "2":
                        os.system("cls")
                        print("Información Proveedor / Distribuidora: ")
                        providerName = input("Ingrese el nombre del Proveedor / Distribuidora: ")
                        providerDirect = input("Ingrese la dirección: ")
                        providerContact = input("Ingrese el número de contacto: ")
                        providerEmail = input("Ingrese la dirección email: ")
                        addProvider(reg.file_name, providerName, providerDirect, providerContact, providerEmail)
                        
                    case "3":
                        os.system("cls")
                        print("Visualización de los Productos")
                        reg.mostrarDatos(reg.file_name)
                    case "4":
                        pass
                    case "5":
                        pass
                    case "6":
                        pass
                    case "7":
                        pass
                    case "0":
                        print("Saliste del menú de Administrador")
                        break
                    case _:
                        print("Elige una de las opciones válidas")
        else:
            print("Las Credenciales son incorrectas")
    except Exception as e:
        print(f"Hubo un ERROR inesperado! lo marco con esto para saber que es, '{e}' no me hackees pls :c")

def menuUsuario():
    print("Bienvenido al sitio de compras de no se que cosas ")
    opcion_User = input("Elige una de las opcines que desees realizar\n1. Comprar\n2. Ver Carrito\n3. Quitar Producto\n4. Finalizar Compra\n: ")
    match opcion_User:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case _:
            print("Elige una de las opciones válidas")

def menuPrincipal():
    while True:
        opcion_Menu = input("""
Bienvenido a equis
Ingresa como Usuario o Admin
1. Para Clientes
2. Para Administrador (Necesitas Credenciales)
Ingresa el número de la opción: """)
        os.system("cls")
        match opcion_Menu:
            case "1":
                menuUsuario()
            case "2":
                menuAdmin()
            case _:
                print("Ingrese una de las opciones permitidas")

menuPrincipal()


