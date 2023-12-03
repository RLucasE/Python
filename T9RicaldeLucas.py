#Herrera Gonzalo Nicolas, 


#recordatorios de utilidad
    #0- idQuem, entero: Identificador univoco del quemador.
    #1- hsTrab, entero: Cantidad de horas acumuladas de trabajo.
    #2- ubic, char: "I": Lateral izquierdo. "d": Lateral derecho. "b": Bóveda.
    #3- proxService: Horas de trabajo que debe alcanzar para el próx. mantenimiento.
    #4- tecnico, string: Nombre de la persona que realizó el último mantenimiento.
    #5- estado, entero: 0: Fuera de servicio. 1:En servicio. 2: En mantenimiento.
#Librerias
import os as os


#Declaracion de funciones
def mostrar(quem):
        print("Id: "+str(quem[0]))
        print("Horas de trabajo: "+str(quem[1]))
        print("Ubicacion: "+str(quem[2]))
        print("Proximo servicio: "+str(quem[3]))
        print("Tecnico: "+str(quem[4]))
        print("Estado: "+str(quem[5]))
        
def verficar_apertura(nombre_Archivo):
    try:
        archivo = open(nombre_Archivo,"r")
    except:
        print("Error")
        return False
    archivo.close()
    return True

def cantidad_de_lineas(nombre_Archivo):
    if verficar_apertura(nombre_Archivo):
        cant=0
        archivo = open(nombre_Archivo,"r")
        for linea in archivo:
            cant += 1
        archivo.close()
        return cant
    else:
        return -1

def mostrar_elemento(nombre_Archivo,ID):
    if (verficar_apertura(nombre_Archivo)):
        archivo = open(nombre_Archivo,"r")
        for linea in archivo:
            linea=linea.split(";")
            if linea[0]==str(ID):
                mostrar(linea)
        archivo.close()
              
def prom_horas(nombre_Archivo,ubicacion):
    if (verficar_apertura(nombre_Archivo)):
        archivo = open(nombre_Archivo,"r")
        horas=0
        quemadores=0
        for linea in archivo:
            linea=linea.split(";")
            if linea[2]==str(ubicacion):
                quemadores+=1
                horas+=int(linea[1])
        archivo.close()
        return (horas/quemadores)
    else:
        return -1

def mostrar_quem_serv_tec(nombre_Archivo,tecnico):
    if (verficar_apertura(nombre_Archivo)):
        archivo = open(nombre_Archivo,"r")
        for linea in archivo:
            linea=linea.split(";")
            if linea[4]==str(tecnico) and linea[5]=="1":
                mostrar(linea)
        archivo.close()


def eliminarFueraServ(nombre_Archivo):
    try:
        archivo = open(nombre_Archivo,"r")
    except:
        print("Error al intentar abrir archivo en eliminarFueraServ en modo r.")

    try:
        archivoAux = open("eliminarFueraServCompleted.txt","w")
    except:
        print("Error al intentar abrir archivo en eliminarFueraServ en modo w.")

    for linea in archivo:
        linea=linea.split(";")
        if(linea[5] != '0'):
            linea = ';'.join(linea)
            archivoAux.write(linea)

    archivoAux.close()
    archivo.close()

    try:
        os.remove(nombre_Archivo)
    except FileNotFoundError:
        print(f"El archivo original '{nombre_Archivo}' no existe.")

    try:
        os.rename("eliminarFueraServCompleted.txt", nombre_Archivo)
    except FileNotFoundError:
        print(f"El archivo auxiliar eliminarFueraServCompleted.txt no existe.")
    except FileExistsError:
        print(f"El archivo eliminarFueraServCompleted.txt ya existe. No se puede renombrar.")

    
    
#Inicio del programa principal
a="Quemadores.txt"
#1
print("cant de quemadores: " + str(cantidad_de_lineas(a)))

#2
mostrar_elemento(a,1523)

#3
print("Promedio de horas: " +str(prom_horas(a,"I")))

#4
mostrar_quem_serv_tec(a,"Nestor")

#5
eliminarFueraServ(a)
