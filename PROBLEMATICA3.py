# PROBLEMÁTICA 3

print("Bienvenido al sistema.")
print(" ")

while True:
    print(" ")
    # MENU DEL SISTEMA
    print("| (1) Formulario para ingreso de personas |")
    print("| (2) Ingreso de productos                |")
    print("| (3) Cálculadora de IVA                  |")
    print(" ")
    opcion = input("Seleccione una opción: ")
    print(" ")
    
    # (1) INGRESO PERSONAS
    while opcion == "1":
        print("| Formulario para ingreso de personas |")
        nombre = input("Ingrese nombre completo: ")
        print(" ")
        correo = input("Ingrese correo electrónico: ")
        print(" ")
        print("Ingrese cargo: ")
        print("| (1) GERENTE    |")
        print("| (2) SECRETARIA |")
        print("| (3) BODEGA     |")
        print("| (4) AUXILIAR   |")
        cargo = int(input())
        print(" ")
        if cargo == 1:
            print("Cargo: Gerente")
        elif cargo == 2:
            print("Cargo: Secretaria(o)")
        elif cargo == 3:
            print("Cargo: Bodega")
        elif cargo == 4:
            print("Cargo: Auxiliar")
        else:
            print("Ingrese una opción válida.")
            print(" ")
            break
        print(" ")
        print("Ingrese tipo de contrato: ")
        print("| (1) A PLAZO    |")
        print("| (2) INDEFINIDO |")
        contrato = int(input())
        print(" ")
        if contrato == 1:
            print("Contrato: A plazo")
        elif contrato == 2:
            print("Contrato: Indefinido")
        else:
            print("Ingrese una opción válida.")
            print(" ")
            break
            
        # DATOS TRABAJADOR
        print(" ")
        print("| Datos del Trabajador |")
        print(" ")
        print("| Nombre: " + str(nombre) + " |")
        print(" ")
        print("| Correo: " + str(correo) + " |")
        print(" ")
        if cargo == 1:
            print("| Cargo: Gerente |")
        elif cargo == 2:
            print("| Cargo: Secretaria(o) |")
        elif cargo == 3:
            print("| Cargo: Bodega |")
        elif cargo == 4:
            print("| Cargo: Auxiliar |")
        print(" ")
        if contrato == 1:
            print("| Contrato: A plazo |")
        elif contrato == 2:
            print("| Contrato: Indefinido |")
            
        # MENU DE CONTINUACION 1
        print(" ")
        print("¿Desea hacer otro ingreso?")
        print("| (1) Continuar                |")
        print("| (2) Salir                    |")
        print(" ")
        cont = int(input("Ingrese una opción aquí: "))
        print(" ")
        if cont != 1:
            break
        
    # (2) INGRESO PRODUCTO        
    while opcion == "2":
        print("| Formulario para ingreso de producto |")
        print(" ")
        nombre_prod = input("Ingrese nombre: ")
        print(" ")
        marca = input("Ingrese marca: ")
        print(" ")
        precio = int(input("Ingrese valor x unidad: "))
        print(" ")
        if precio <= 0:
            print("Ingrese un precio válido.")
            print(" ")
            break     
        cantidad = int(input("Ingrese cantidad: "))
        print(" ")
        if cantidad <= 0:
            print("Ingrese una cantidad válida.")
            print(" ")
            break
        elif cantidad > 10:
            print("No puede ingresar más de 10.")
            print(" ")
            break
            
        # DATOS PRODUCTO INGRESADO
        else:
            print("| Informe de producto ingresado |")
            print(" ")
            print("| Nombre: " + str(nombre_prod) +" |")
            print(" ")
            print("| Marca: " + str(marca) +" |")
            print(" ")
            print("| Precio x unidad: " + "$" + str(precio) +" |")
            print(" ")
            print("| Cantidad ingresada: " + str(cantidad) +" un. |")
            
        # MENU DE CONTINUACION 2
        print(" ")
        print("¿Desea hacer otro ingreso?")
        print("| (1) Continuar                |")
        print("| (2) Salir                    |")
        print(" ")
        cont2 = int(input("Ingrese una opción aquí: "))
        print(" ")
        if cont2 != 1:
            break
    
    # (3) CALCULADORA IVA
    while opcion == "3":
        print(" ")
        print("| Calculadora de IVA producto |")
        print(" ")
        nombre_prod2 = input("Ingrese nombre: ")
        print(" ")
        marca2 = input("Ingrese marca: ")
        print(" ")
        bruto = int(input("Ingrese valor bruto: "))
        if bruto <= 0:
            print(" ")
            print("Ingrese un precio válido.")
            print(" ")
            break    
        iva = int(bruto * 0.19)
        total = bruto + iva
        
        # CALCULO DE IVA Y TOTAL
        print(" ")
        print("| Calculo de IVA del producto |")
        print(" ")
        print("| Nombre: " + str(nombre_prod2) +" |")
        print(" ")
        print("| Marca: " + str(marca2) +" |")
        print(" ")
        print("| Valor bruto: " + str(bruto) +" |")
        print(" ")
        print("| Valor IVA: " + str(iva) +" |")
        print(" ")
        print("| Valor total: " + str(total) +" |")
        print(" ")
        
        # MENU DE CONTINUACION 3
        print(" ")
        print("¿Desea hacer otro ingreso?")
        print("| (1) Continuar                |")
        print("| (2) Salir                    |")
        print(" ")
        cont3 = int(input("Ingrese una opción aquí: "))
        print(" ")
        if cont3 != 1:
            break
    break