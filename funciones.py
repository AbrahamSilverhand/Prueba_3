def saludo():
    print("Bienvenido al control de gestion de clientes TODOAHORRO")

bd = [

]

def menu():

    opciones = [
        "Registrar Cliente",
        "Listar Clientes Registrados",
        "Registrar Compra",
        "Listar Compras de un Cliente",
        "Salir del Programa",
    ]

    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")

def registrar_cliente(bd):
    nombre = input("Ingrese primer nombre del cliente: ").upper()
    apellido = input("Ingrese primer apellido del cliente: ").upper()
    correo = input("Ingrese el correo electronico del cliente: ").upper()
    
    id_cliente = len(bd) + 1

    bd.append(
        {
            "nombre": nombre,
            "apellido": apellido,
            "correo": correo,
            "ID": id_cliente,
            "compras": []
        }
    )

    print("\nCliente agregado sastifactoriamente\n")

def listar_clientes(bd):
    print("\nLos clientes registrados son:\n")
    print("ID\t\t\tNombre\t\t\tCorreo")
    for cliente in bd:
        print(f'{cliente["ID"]}\t\t\t{cliente["nombre"]} {cliente["apellido"]}\t\t\t{cliente["correo"]}')

    print("\nListado creado con éxito!\n")  

def registrar_compra(bd):
    id = int(input("Ingrese el ID del cliente que asiste: "))

    for cliente in bd:
        if cliente["ID"] == id:
            fecha = input("Ingrese fecha de compra (AAAA-MM-DD): ")
            compra = int(input("Ingrese el total de la compra: "))
            puntos_acumulados = int(compra * 0.01)
            cliente["compras"].append({
                "fecha": fecha,
                "compra": compra,
                "puntos": puntos_acumulados
            })
            print(f'\nSe ha agregado una compra a {cliente["nombre"]} {cliente["apellido"]}.')
            print(f'Se han acumulado {puntos_acumulados} puntos por esta compra.')
            break
    else:
        print(f"El cliente de ID = {id} no existe.")   

def listar_compras(bd):
    id = int(input("Ingrese el ID del cliente que necesita: "))

    for cliente in bd:
        if cliente["ID"] == id:
            texto = f"ID Cliente: {id}\n"
            texto += f'NOMBRE CLIENTE: {cliente["nombre"]} {cliente["apellido"]}\n'
            texto += f"Fecha de Compra\t\tMonto total de Compra\t\tTotal de Puntos"

            compra_total = 0
            for compra in cliente["compras"]:
                texto += f'{compra["fecha"]}\t\t{compra["compra"]}\t\t{compra["puntos"]}\n'
                compra_total += compra["compra"]

            texto += f'Monto total de la compra: {compra_total} pesos\n'

            with open(f"RESUMEN_CLIENTE_ID_{id}.txt", "w", encoding='utf-8') as archivo:
	            archivo.write(texto)
                
            print(f'\nSe ha creado el archivo RESUMEN_CLIENTE_ID_{id}.txt')
            break