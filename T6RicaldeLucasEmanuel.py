def definirMatrizMxN(M,N):
    matriz = []
    for i in range(M):
        matriz.append([])
        for j in range(N):
            matriz[i].append(0)
    
    return matriz

def CargarMat(mat,M,N): #Carga matriz fila x fila
    for i in range(M):
        for j in range(N):
            mat[i][j] = int(input(f"Ingrese la cantidad de litros del equipo {i+1} en el mes {j+1}"))


def MostrarMat(mat,M,N): 
    for i in range(M):
        print(f"Equipo {i+1}: ")
        for j in range(N):
            print(f"Mes {j+1}: ",mat[i][j])


def ProdMes(mat,M,N,Mes):  #Retorna producción de un MES específico.
    produccionTotal = 0 

    if(Mes <= N): 
        for i in range(M):
            produccionTotal += mat[i][Mes-1]
    
    else: print("Mes fuera de rango")
    return produccionTotal

def ProdEquipo(mat,M,N,equipo):  #Retorna producción de un MES específico.
    produccionTotal = 0  

    if(equipo <= M):
        for j in range(N):
            produccionTotal += mat[equipo-1][j]
            
    else: print("Equipo fuera de rango")

    return produccionTotal 


def AgregarCol(mat,M,N):
    for i in range(M):
        (mat[i]).append(input(f"Produccion del equipo {i+1}: "))


def EliminarEquipo(mat,M,N,Eq): #Elimina um equipo específico. }
    if(Eq <= M):
        del mat[Eq-1]
    else: print("Equipo esta fuera de rango elegible")

def elegirOpcionMenu():
    print("1) Mostrar la producción total de un mes.")
    print("2) Mostrar la producción total de un equipo.")
    print("3) Agregar un nuevo mes de producción de los equipos.")
    print("4) Eliminar toda la información de un equipo.")
    print("5) Mostrar todo.")
    print("0) Salir")

    return int(input("Opcion: "))



   
def menu():
    matrizEquiposxMes = definirMatrizMxN(int(input("Cantidad de equipos: ")),int(input("Cantidad de meses registrados hasta la fecha: ")))
    CargarMat(matrizEquiposxMes,len(matrizEquiposxMes),len(matrizEquiposxMes[0]))

    opcion = elegirOpcionMenu()
    while(opcion != 0):
        match(opcion):
            case 1:
                total = ProdMes(matrizEquiposxMes,len(matrizEquiposxMes),len(matrizEquiposxMes[0]),int(input("Mes: ")))
                if(total!=0): print("Total: ",total)
            case 2:
                total = ProdEquipo(matrizEquiposxMes,len(matrizEquiposxMes),len(matrizEquiposxMes[0]),int(input("Equipo: ")))
                if(total!=0): print("Total: ",total)
            case 3:
                AgregarCol(matrizEquiposxMes,len(matrizEquiposxMes),len(matrizEquiposxMes[0]))
            case 4:
                EliminarEquipo(matrizEquiposxMes,len(matrizEquiposxMes),len(matrizEquiposxMes[0]),int(input("Equipo: ")))
            case 5:
                MostrarMat(matrizEquiposxMes,len(matrizEquiposxMes),len(matrizEquiposxMes[0]))
            case _:
                resultado = "Operación no reconocida"

        opcion = elegirOpcionMenu()

menu()