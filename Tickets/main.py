import sys, os, random, pickle

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def generar_numero_ticket():
    return random.randint(1000, 9999)

def guardar_ticket(ticket, nombre_archivo):
    with open(nombre_archivo, 'wb') as archivo:
        pickle.dump(ticket, archivo)

def cargar_ticket(nombre_archivo):
    with open(nombre_archivo, 'rb') as archivo:
        return pickle.load(archivo)

def existe_ticket(nombre_archivo):
    return os.path.isfile(nombre_archivo)

def agregar_ticket():

    limpiar_pantalla()
    print("ingresa los datos para generar un nuevo ticket")
    nombre = input("ingresa tu nombre: ")
    sector = input("ingrese tu sector: ")
    asunto = input("ingrese el asunto: ")
    mensaje = input("Iingrese el mensaje: ")

    numero_ticket = generar_numero_ticket()
    ticket = {
        'nombre': nombre,
        'sector': sector,
        'asunto': asunto,
        'mensaje': mensaje,
        'numero_ticket': numero_ticket
    }
    
    nombre_archivo = f'ticket_{numero_ticket}.txt'
    guardar_ticket(ticket, nombre_archivo)
    
    print("\nse genero el siguiente ticket")
    print("="*50)
    print(f"Su nombre: {nombre}")
    print(f"Sector: {sector}")
    print(f"Asunto: {asunto}")
    print(f"Mensaje: {mensaje}")
    print(f"N° Ticket: {numero_ticket}")
    print("="*50)
    print("\nrekorda tu numero de ticket")
    
    otro_ticket = input("¿queres generar un nuevo ticket? (s/n): ").lower()
    if otro_ticket == 's':
        agregar_ticket()
    else:
        menu_principal()

def leer_ticket():
    limpiar_pantalla()
    numero_ticket = input("ingresa el número del ticket que desea leer: ")
    nombre_archivo = f'ticket_{numero_ticket}.txt'
    
    if existe_ticket(nombre_archivo):
        ticket = cargar_ticket(nombre_archivo)
        print("\nse recuperó el siguiente ticket")
        print("="*50)
        print(f"su nombre: {ticket['nombre']}")
        print(f"sector: {ticket['sector']}")
        print(f"asunto: {ticket['asunto']}")
        print(f"mensaje: {ticket['mensaje']}")
        print(f"N° ticket: {ticket['numero_ticket']}")
        print("="*50)
    else:
        print("\n el ticket ingresado no existe.")

    otro_ticket = input("¿qeures leer otro ticket? (s/n): ").lower()
    if otro_ticket == 's':
        leer_ticket()
    else:
        menu_principal()

def menu_principal():
    while True:
        limpiar_pantalla()
        print("wenas papu, bienvenido al sistema de tickets")
        print("1 - generar un nuevo ticket")
        print("2 - leer un ticket")
        print("3 - salir")
        seleccion = input("selecciona: ")

        if seleccion == '1':
            agregar_ticket()
        elif seleccion == '2':
            leer_ticket()
        elif seleccion == '3':
            confirmar_salida = input("esta seguro que desea salir? (s/n): ").lower()
            if confirmar_salida == 's':
                print("saliendo del sistema")
                sys.exit()
            else:
                continue
        else:
            print("seleccion inválidam inntenta de nuevo")

if __name__ == "__main__":
    menu_principal()
#tuve que ayudarme con tutoriales de youtube pq se me iban las cosas de la cabeza y muy bien no entendi los mensajes 
# y un poco con chat gpt para que me explique cosas que no sabia como lo la linea 114 y eso de """ JAWKDJA