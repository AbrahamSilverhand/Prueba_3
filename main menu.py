from funciones import *
bd = [
    
]

saludo()
menu()

while True:
    opcion = input("Elige la opcion de elegir: ")
    if opcion == "1":
        registrar_cliente(bd)
    elif opcion == "2":
        listar_clientes(bd)
    elif opcion == "3":
        registrar_compra(bd)
    elif opcion == "4":
        listar_compras(bd)
    elif opcion == "5":
        print("HASTA LA PROXIMA")
        break
    else:
        print("La opcion elegida no es valida.")
        print("Hagalo otra vez.")