#PROBLEMATICA 1

# Filtro de edad
print("¡Bienvenido! Este local no permite el ingreso de menores de edad sin compañía de un adulto.")
while True:
    edad = int(input("Ingresa tu edad aquí: "))
    
# Si es mayor de edad
    if edad >= 18:
        print("Su edad es "+str(edad)+" años. Puede pasar.")
        break
        
# Restriccion numeros negativos    
    elif edad < 0:
        print("Por favor, ingrese una edad válida.")
        
# Ingreso menores solo acompañados        
    elif edad < 18:
            print("¿Está usted acompañado por un mayor de edad?")
            opcion = int(input(" (1) SÍ | (2) NO "))
            if opcion == 1:
                print("Su edad es "+str(edad)+" años, es menor de edad, pero está en compañía de un adulto. Puede ingresar.")
                break
            elif opcion == 2:
                print("Su edad es "+str(edad)+" años, no está con un adulto. No puede ingresar.")
                break
            else:
                print("Por favor, ingrese una opción válida.")