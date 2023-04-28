#Sistema ingreso listas
lista = []

#agregar parametro
def agregar():
    lista.append(input("Nombre a ingresar: "))
    print(" ")
    print("La lista se ha actualizado: ", lista)

#agregar parametro lugar especifico
def agregar_esp():
    lista.insert(int(input("Posicion a ingresar: ")),input("Nombre a ingresar: "))
    print(" ")
    print("La lista se ha actualizado: ", lista)

#eliminar parametro
def eliminar():
    if len(lista) == 0:
        print("La lista está vacía. No hay parámetros para eliminar.")
        return
    lista.remove(input("Nombre a eliminar: "))
    print(" ")
    print("La lista se ha actualizado: ", lista)

#mostrar lista
def mostrar_lista():
    if len(lista) == 0:
        print("La lista está vacía.")
    else:
        print("La lista actualizada es: ", lista)

#INGRESO AL SISTEMA
print("|-----------------Bienvenido al sistema-------------------|")
while True:
    print(" ")
    # MENU DEL SISTEMA
    print("| (1) Agregar parametro                                   |")
    print("| (2) Agregar parametro (lugar especifico)                |")
    print("| (3) Eliminar parametro                                  |")
    print("| (4) Mostrar lista actualizada                           |")
    print("|---------------------------------------------------------|")
    print("| (5) Salir del sistema                                   |")
    print(" ")
    opcion = int(input("Seleccione una opción: "))
    print(" ")
    
    # Verificar opción válida
    if opcion not in [1, 2, 3, 4, 5]:
        print("Por favor, ingrese una opción válida (1, 2, 3, 4 o 5).")
        continue
    
    #opciones
    if opcion == 1:
        agregar()
    elif opcion == 2:
        agregar_esp()
    elif opcion == 3:
        eliminar()
    elif opcion == 4:
        mostrar_lista()
    elif opcion == 5:
        print("Saliendo del sistema...")
        break