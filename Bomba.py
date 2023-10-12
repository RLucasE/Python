pi = 3.141592653
longitud = int(input("Longitud en metros: "))
diametro = float(input("Diametro en metros: "))
velocidad_agua_ms = float(input("velocidad del agua ms: "))
factor_friccion = float(input("factor de friccion: "))
densidad_agua = int(input("Densidad del agua en kg: "))


presion = factor_friccion * ((velocidad_agua_ms ** 2)/diametro) * (2*longitud) * densidad_agua   #kg/m * s ^2
pot = presion * (velocidad_agua_ms * pi) * (diametro/2)**2

print(format((pot * 0.001 )/ 0.736498,'.2f'),"HP aproximadamente")

