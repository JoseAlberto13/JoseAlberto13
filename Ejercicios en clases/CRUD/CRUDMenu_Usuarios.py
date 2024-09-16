import os
import CRUDregistros_productos

adminUser = ({
    "user": "admin",
    "password": "admin123"
})

def menuAdmin():
    print("Inicio de sesión como Administrador")
    inUser = input("Ingrese Usuario: ")
    inPassword = input("Ingrese Contraseña: ")
    try:
        if inUser == adminUser.get("user") and inPassword == adminUser.get("password"):
            print("Bienvenido Admin, haga lo que le de la gana :D")
            opcion_Admin = input("1. Agregar Producto\n2. Visualizar Producto\n3. Visualizar Lista de Productos\n4. Visualizar Lista de Clientes\n5. Actualizar Producto\n6. Eliminar Producto\n0. Salir\n: ")
            match opcion_Admin:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    pass
                case "0":
                    pass
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


