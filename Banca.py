usuarios=[]
cuentas=[]

def agregar_usuario():
    while True:
        nombre=input("Ingresa el nombre del Usuario: ")
        if nombre in usuarios:
            print(f"El usuario {nombre} ya existe, intentelo con otro Usuario")
        else:
            usuarios.append(nombre)
            cuentas.append(0.0)
            print(f"Usuario {nombre} agregado con exito")
            break
    

def depositar():
    nombre=input("Ingrese el Usuario que va a depositar: ").strip().lower()
    if nombre in usuarios:
        indice=usuarios.index(nombre)
        saldo=float(input(f"Ingrese la cantidad a depositar, {nombre}: "))
        cuentas[indice] +=saldo
        print(f"Se han depositado {saldo} en la cuenta de {nombre}, saldo actual: {cuentas[indice]}")
    else:
        print("Usuario no registrado, por favor, registrelo primero")
        agregar_usuario()
        
def retirar():
    nombre=input("Ingrese el Usuario que va a retirar: ").strip().lower()
    if nombre in usuarios:
        indice=usuarios.index(nombre)
        saldo=float(input(f"Ingrese la cantidad a retirar, {nombre}: "))
        cuentas[indice] -=saldo
        print(f"Se han retirado {saldo} en la cuenta de {nombre}, saldo actual: {cuentas[indice]}")
    else:
        print("Usuario no registrado, por favor, registrelo primero")
        agregar_usuario()
        

def consultar_saldo():
    nombre=input("Ingrese el Usuario a consultar el saldo: ").strip().lower()
    if nombre in usuarios:
        indice=usuarios.index(nombre)
        print(f"El saldo actual de {nombre} es {cuentas[indice]}")
    else:
        print("Usuario no registrado")

def menu():
    while True:
        print("Bienvenido al sistema de banco")
        print("1. Agregar usuario")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Consultar saldos")
        print("5. Salir")
        
        opcion=input("Selecciona una opcion: ").strip()
        
        if opcion == '1':
            agregar_usuario()
        elif opcion == '2':
            depositar()
        elif opcion == '3':
            retirar()
        elif opcion == '4':
            consultar_saldo()
        elif opcion == '5':
            print("Gracias por usar el sistema")
            break
        else:
            print("Opcion incorrecta, por favor, intentalo nuevamente")
            
menu()
        
        
        
        
        
    
    