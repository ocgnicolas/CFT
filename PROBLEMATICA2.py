# PROBLEMATICA 2

# Ingreso datos y notas estudiante
nombre = input("Ingrese nombre completo del estudiante: ")
curso = input("Ingrese curso del estudiante: ")

# 1era nota
while True:
    nota1 = float(input("Ingrese la 1era nota: "))
    if nota1 < 1:
        print("Por favor, ingrese una nota válida.")
    elif nota1 > 7:
        print("Por favor, ingrese una nota válida.")
    else:
        break

# 2da nota        
while True:
    nota2 = float(input("Ingrese la 2da nota: "))
    if nota2 < 1:
        print("Por favor, ingrese una nota válida.")
    elif nota2 > 7:
        print("Por favor, ingrese una nota válida.")
    else:
        break

# 3era nota       
while True:
    nota3 = float(input("Ingrese la 3era nota: "))
    if nota3 < 1:
        print("Por favor, ingrese una nota válida.")
    elif nota3 > 7:
        print("Por favor, ingrese una nota válida.")
    else:
        break

# 4ta nota      
while True:
    nota4 = float(input("Ingrese la 4ta nota: "))
    if nota4 < 1:
        print("Por favor, ingrese una nota válida.")
    elif nota4 > 7:
        print("Por favor, ingrese una nota válida.")
    else:
        break

# Cálculo promedio de notas
promedio = (nota1 + nota2 + nota3 + nota4)/4
float_promedio = float(promedio)

# Mensaje final
if float_promedio < 4:
    print("El(la) alumno(a) "+str(nombre)+", del "+str(curso)+", REPROBÓ el curso con la siguiente nota: "+str(float_promedio)+".")
else:
    print("El(la) alumno(a) "+str(nombre)+", del "+str(curso)+", APROBÓ el curso con la siguiente nota: "+str(float_promedio)+".")