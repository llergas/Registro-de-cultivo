
def registracultivo():
    # Gestión de recolección y mantenimiento de cultivos

    # Se hace un ciclo While infinito para ingresar la cantidad de cultivos que desee y sus  respectivas características.

    while True:
        nom = input("Ingrese el nombre del cultivo: ").upper()
        mtto = input("Ingrese los días y el horario de mantenimiento: ")
        regado = input("Ingrese los días y el horario del regado: ")
        abono = input("Ingrese los días y el horario del abono: ")
        etapa = input("Ingrese la etapa del cultivo: ")

    # Se crea o se abre un archivo .txt para almacenar cada característica del cultivo.
    # El nombre del archivo txt se lo da la variable nom e mayúsculas

        file = open(f"cultivos/{nom}.txt", "w")

        file.write(f"{nom}\n")
        file.write(f"{mtto}\n")
        file.write(f"{regado}\n")
        file.write(f"{abono}\n")
        file.write(f"{etapa}\n")
        file.close()
        respueta = input("¿Desea registrar mas cultivos? S/N ").upper()
        if respueta == "N":
            break
    # Se hace la pregunta si desea registrar mas cultivos. En caso que sean S comienza de nuevo el ciclo.

def pregunta():
    # Se importa os para poder almacenar en una variable los archivos que están contenidos en la carpeta cultivos.
    # Estos archivos se almacena en una tupla.

    import os
    contenido = os.listdir("cultivos")

    # Se hace un ciclo for para que recorra todos los archivos contenidos en la variable contenido y los imprima
    # precedido de un consecutivo que inicia en 1 formando un menú par que el usuario  escoja el cultivo.

    while True:
        print(f"Cultivos disponibles: \n")
        for i in range(0, len(contenido)):
            print(i + 1, contenido[i])

        print()

        cultivo = int(input("Ingrese el número del cultivo "))
        print()
        cultivo_selec = contenido[cultivo - 1]
        print(f"Usted escogió el cultivo {cultivo_selec}")
        print()

        # Despúes de que el usuario escoge el cultivo, la aplicación abre el archivo correspondiente y lee el total del contenido

        bd_cultivo = open(f"cultivos/{cultivo_selec}", "r")
        nom = bd_cultivo.readline().replace("\n", "")
        mtto = bd_cultivo.readline().replace("\n", "")
        regado = bd_cultivo.readline().replace("\n", "")
        abono = bd_cultivo.readline().replace("\n", "")
        etapa = bd_cultivo.readline().replace("\n", "")

        # Despúes de leer el contenido del archivo se despliega otro menú que pregunta si quiere saber sobre el horario de
        # gestión, la etapa del cultivo o salir de la aplicación.

        print(f"Informacion disponible: \n\n"
              f"\t1. Horario de gestion de cultivo \n"
              f"\t2. Etapas del cultivo \n"
              f"\t3. Salir \n")

        info = int(input("Ingrese el numero correspondiente a la informacion deseada: "))
        print()

        if info == 1:
            print(f"Esta es la informacion del horario de gestion:\n"
                  f"\n"
                  f"Nombre del cultivo: {nom}\n"
                  f"Dias y horario de mantenimiento: {mtto}\n"
                  f"Dias y horario de regado: {regado}\n"
                  f"Dias y horario de abono: {abono}\n")
            break
        elif info == 2:
            print(f"Esta es la informacion sobre las etapas:\n"
                  f"\n"
                  f"Nombre del cultivo: {nom}\n"
                  f"Etapa: {etapa}\n")
            break

        elif info == 3:
            print("Saldra de la aplicacion")
        else:
            print("Esat opcion no existe")

while True:
    print("\n ¿Que desea hacer? para elegir una opcion escriba el numero que corresponda. \n")
    print("1. Registrar cultivo.")
    print("2. Preguntar sobre cultivo existente.")
    print("3. Salir.")
    respuesta = input()
    print()
    if respuesta == "1":
        registracultivo()
    elif respuesta == "2":
        pregunta()
    elif respuesta == "3":
        break
    else:
        print("Ingrese una opcion valida.")