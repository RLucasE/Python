# T10. Consigna y envío de la Actividad OBLIGATORIA. (Hasta Vie. 24/11, 15:59 hs.)
# ACTIVIDAD OBLIGATORIA DEL TEMA 10

# Es su primer día de trabajo en el departamento de sistemas de una importante empresa de Bolsas de Polietileno de Salta, el jefe de sistemas le solicita desarrollar una aplicación ABMC (Alta, Baja, Modificación y Consulta) para gestionar la información de producción de las bolsas de polietileno del último semestre. La aplicación debe cumplir los siguientes requerimientos:

# 1. La estructura de datos debe ser una lista de diccionarios con la siguiente información:
#        IdBobina, int.
#        Metros (m.), int.
#        Ancho (mm.), int
#        Stock, int.

# 2. Una función menú para mostrar las opciones y retornar el valor ingresado por el usuario.
# 3. Una función parametrizada para cada opción del menú que incluya la entrada de datos necesarios para la resolución.
# 4. Desarrollar la baja, modificación y consulta de una bobina a partir del IdBobina ingresado por el usuario.
# 5. Las funciones no deben retornar la lista, deben incluir un parámetro transferido por referencia.
# 6. Todos los datos serán ingresadas desde el teclado.
# 7. En todos los casos, el programa debe mostrar un texto de error cuando el IdBobina ingresado no se encuentre registrado en la lista.

# Pautas para la presentación de la actividad

# Primero declare e implemente las funciones y procedimiento solicitados. Luego desarrolle el bloque del programa principal.
# Utilice comentarios para definir claramente las secciones del programa (func/proc, prog.principal, entradas, procesamiento y salidas).
# Todos los datos deben ser ingresados por el usuario desde el teclado.
# Solo utilice estructuras de datos solicitadas.
# No utilice la instrucción break ni continue para afectar la ejecución de los ciclos.
# Nombre del archivo que debe adjuntar:   T10 - Apellidos - nombres . py
# Vencimiento del plazo de presentación


##Funciones y procedimientos

##Funciones/Procedimientos para crear cargar datos
def newBobina():
    bobina = {}
    bobina["IdBobina"] = int(input("Id de la bobina: ")) ##Int
    bobina["Metros"] = int(input("Metros de la bobina: "))
    bobina["Ancho"] = int(input("Milimetros de ancho de la bobina: "))
    bobina["Stock"] = int(input("Stock de la bobina: "))
    return bobina
    
def ingresarLista(lista):
    for i in range(int(input("Ingrese la cantidad de bobinas: "))):
        lista.append(newBobina())

def menu():
    print("Opcion 1: ")
    return input()

def estaEn(idBobina,lista):
    for bobina in lista:
        if bobina["IdBobina"] == idBobina: return True
    return False

def keySelectBobina():
    print("1.Id Bobina")
    print("2.Metros")
    print("3.Ancho")
    print("4.Stock")
    op = int(input("Opcion: "))
    if(op == 1): return "IdBobina"
    if(op == 2): return "Metros"
    if(op == 3): return "Ancho"  
    if(op == 4): return "Stock"
    return "IdBobina"

def darBaja(bobinas,idBobina):
    if estaEn(idBobina,bobinas): 
        for i in range(len(bobinas)):
            if bobinas[i]["IdBobina"] == idBobina:
                band = True
                del bobinas[i]
    else : print("La bobina no se encuentra")
    

def modificarBobina(bobinas,idBobina):
    if estaEn(idBobina,bobinas):
        for i in range(len(bobinas)):
            if bobinas[i]["IdBobina"] == idBobina:
                seleccion = keySelectBobina()
                bobinas[i][seleccion] = input("Nuevo valor")
    else: print("La bobina no se encuentra")

def consultarBobina(bobinas,idBobina):
    if estaEn(idBobina,bobinas):
        for bobina in bobinas:
            if(bobina["IdBobina"] == idBobina):
                print(bobina)
    else: print("La bobina no se encuentra")       

##Main

listaBobi = []
ingresarLista(listaBobi)
# print(listaBobi)
# darBaja(listaBobi,int(input("Id de la bobina a remover")))
# print(listaBobi)
modificarBobina(listaBobi,int(input("Id de la bobina a modificar: ")))
print(listaBobi)
consultarBobina(listaBobi,int(input("Id de la bobina a modificar: ")))