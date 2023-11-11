# T8. Buzón de envío de la actividad obligatoria. (copia)
# ACTIVIDAD OBLIGATORIA DEL TEMA 8

# Como se vio en el video del Ing. López de San Martín (si no recuerda véalo nuevamente), Cerámica del Norte fabrica ladrillos primordialmente huecos para la construcción. Los ladrillos se cargan en vagonetas que ingresan secuencialmente al horno túnel. El departamento de mantenimiento administra el mantenimiento periódico de todos los equipos de producción, especialmente de los quemadores.

# Redactar e implementar todos los métodos la clase quemador con la siguiente estructura:

# Nombre de clase: quemador
# Lista de atributos (todos privados)

# idQuem, entero: Identificador univoco del quemador.
# hsTrab, entero: Cantidad de horas acumuladas de trabajo.
# ubic, char: "I": Lateral izquierdo. "d": Lateral derecho. "b": Bóveda.
# proxService: Horas de trabajo que debe alcanzar para el próx. mantenimiento.
# tecnico, string: Nombre de la persona que realizó el último mantenimiento.
# estado, entero: 0: Fuera de servicio. 1:En servicio. 2: En mantenimiento.
# Lista de métodos

# __init__: Parametrizado para inicializar todos los atributos.
# mostrar: Muestra el estado completo del objeto (todos sus atributos).
# get_idQuem: Retorna el número identificador del objeto.
# get_hsTrab: Retorna las horas de trabajo.
# get_ubic: Retorna la ubicación.
# get_proxService: Retorna las horas para el próximo mantenimiento.
# set_tecnico: Parametrizado para modificar el nombre del técnico de mantenimiento.
# set_estado: Parametrizado para modificar el estado del quemador.

# Redactar los siguiente módulos para procesar una
#   
##     lista de quemadores.

# 1. Solicitar la entrada de la cantidad de quemadores (N) para procesar. Luego verificar que el valor de N sea menor o igual a 28, en caso de incumplimiento solicitar nuevamente el ingreso de N.
# Ingresar N
# N = Verificar (N, tope)

# 2. Procedimiento para solicitar la entrada de la información de N quemadores en una lista previamente vacía.
# CargarLista(lista, N)

# 3. Procedimiento para mostrar los atributos de todos los quemadores almacenados en la lista.
# MostraLista(lista, N)

# 4. Procedimiento para mostrar los atributos de un quemador conociendo su número Id.
# MostrarQuem(lista, N, id)

# 5. Procedimiento para mostrar un listado de los quemadores (idQuem, hsTrab, ubic) "en servicio" que requieren mantenimiento (hsTrab >= proxService)

# 6. Sabiendo el Id de un quemador y nombre del técnico encargado de hacerlo, enviarlo al departamento de mantenimiento.

# 7. Mostrar los atributos del quemador enviado a mantenimiento, invocando al procedimiento del punto 4.

# 8. El jefe del departamento de mantenimiento requiere periódicamente un informe de los quemadores con horas de trabajo próxima al mantenimiento. Redactar un procedimiento para mostrar la información de todos los quemadores que le faltan XHs horas o menos para su mantenimiento. ((proxMan - hsTrab) <= XHs)
# QuemProxService(lista, N, XHs)

# 9. Invocar todos los módulos solicitados en el orden especificado.

# Pautas para la presentación de la actividad

# Primero declare e implemente la clase y las funciones/procedimientos. Luego en el bloque del programa principal invóquelas ordenadamente para resolver todo lo solicitado.
# Utilice comentarios para definir claramente las secciones del programa (clase, func.proc, prog.principal, entradas, procesamiento y salidas).
# Todos los datos deben ser ingresados por el usuario desde el teclado.
# Solo utilice estructuras de datos, de control, paradigmas e instrucciones estudiados previamente en el curso.
# No utilice la instrucción break ni continue para afectar la ejecución de los ciclos.
# Nombre del archivo que debe adjuntar:   T7 - Apellidos - nombres . py
# No acceder a un atributo directamente, hacerlo mediante la invocación de un método.


from typing import Any

def Verificar(N, tope):
    while(N >= tope):
        N = int(input(f"Error, ingresar quemaadores menor a {tope}: "))
    return N


        


class quemador:
    _idQuem = 0

    # idQuem, entero: Identificador univoco del quemador.
    # hsTrab, entero: Cantidad de horas acumuladas de trabajo.
    # ubic, char: "I": Lateral izquierdo. "d": Lateral derecho. "b": Bóveda.
    # proxService: Horas de trabajo que debe alcanzar para el próx. mantenimiento.
    # tecnico, string: Nombre de la persona que realizó el último mantenimiento.
    # estado, entero: 0: Fuera de servicio. 1:En servicio. 2: En mantenimiento.

    def __init__(self):
        quemador._idQuem += 1 
        self._idQuem = quemador._idQuem
        self.hsTrab = int(input("Horas trabajadas: "))
        self.ubic = input("Ubicacion: ")
        self.proxService = int(input("Horas nesesarias para un servicio: "))
        self.tecnico = input("Tecnico: ")
        self.estado = int(input("Estadao: "))

    def mostrarQum(self):
        print(f"Id: {self._idQuem}")
        print(f"Ubicacion: {self.ubic}" )
        print(f"Horas nesesarias para un servicio: {self.proxService}" )
        print(f"Horas nesesarias para un servicio: {self.hsTrab}" )
        print(f"Tecnico: {self.tecnico}")
        print(f"Estado: {self.estado}")

    def get_idQuem(self):
        return self._idQuem
    def get_hsTrab(self):
        return self.hsTrab
    def getUbi(self):
        return self.ubic
    def get_proxService(self):
        return self.proxService
    def getTecnico(self):
        return self.tecnico
    def setTecnico(self,tecnico):
        self.tecnico = tecnico
    def setEstado(self,estado):
        self.estado = estado
    def requService(self):
        if (self.estado == 1) and (self.hsTrab >= self.proxService):
            return True
        else: return False



##--------------------Modulos

def CargarLista(lista, N):
    for i in range(N):
        print("-----------------")
        lista.append(quemador())

def MostraLista(lista):
    for i in range(len(lista)):
        lista[i].mostrarQum()

def MostrarQuem(lista, id):
    for i in range(len(lista)):
        if(lista[i].get_idQuem() == id):
            lista[i].mostrarQum()

def mostrarQuemReqSer(lista):
    for i in range(len(lista)):
        if(lista[i].requService()):
            lista[i].mostrarQum()

def mandarMantenimiento(lista,id,tecnico):
    for i in range(len(lista)):
        if(lista[i].get_idQuem() == id) and (lista[i].getTecnico() == tecnico):
            lista[i].setEstado(2)

def informe(lista,XHs):
    for i in range(len(lista)):
        if(lista[i].get_proxService() - lista[i].get_hsTrab()) <= XHs:
            lista[i].mostrarQum()


##----------------------MAIN-----------------------
MAXQUEM = 28
N = int(input("Numero de quemadores: "))
N = Verificar(N,MAXQUEM)
lista = []
CargarLista(lista,N)
MostraLista(lista)
id = int(input("Id del quemador a mostrar: "))
MostrarQuem(lista,id)
mostrarQuemReqSer(lista)
id = int(input("Id del quemador para mandaar a mantenimiento: "))
mandarMantenimiento(lista,id,input("Nombre del tecnico encargado: "))
MostrarQuem(lista,id)
informe(lista,int(input("horas minimas para el informe: ")))