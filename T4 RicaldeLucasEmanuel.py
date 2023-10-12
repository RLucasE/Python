##ingreso de datos
nombreYApellido = input("Escriba su apellido y nombre completos: ")
num = int(input("Escriba un número entero de hasta 4 dígitos: ")) 

#Variables principales
nombreYApellido = nombreYApellido.split(",")
apellido = nombreYApellido[0]
nombres = nombreYApellido[1].split()
correo = ""
contraceña = ""

#Generar contraceña y correo a partir de los datos
for i in range(len(nombres)):
    correo += nombres[i][0]

correo += apellido + str(num)

for i in range(len(correo)):
    letra = correo[i]
    if (letra == "a" or letra == "A") :
        letra = 1
    if (letra == "e" or letra == "E") :
        letra = 2
    if (letra == "i" or letra == "I") :
        letra = 3 
    if (letra == "o" or letra == "O") :
        letra = 4
    if (letra == "u" or letra == "U") :
        letra = 5 
    contraceña += str(letra)

correo +=  "@unsa.edu.ar";

#Salida
print(f"Correo sugerido para la universidad: {correo}")
print(f"Contraseña sugerida: {contraceña}")