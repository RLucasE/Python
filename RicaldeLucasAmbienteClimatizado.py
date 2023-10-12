gan = int(input("Ganancia: "))
multa = 0

m1 = int(input("Medicion 1: "))
m2 = int(input("Medicion 2: "))
m3 = int(input("Medicion 3: "))
m4 = int(input("Medicion 4: "))
m5 = int(input("Medicion 5: "))

prom = (m1 + m2 + m3 + m4 + m5)/5

if prom <= 220: 
   multa = 0
if 220 < prom <= 450:
   multa = gan * 0.05
if 450 < prom <= 675:
   multa = gan * 0.10
if 675 < prom <= 1120:
   multa = gan * 0.25
if 1120 < prom <= 1695:
   multa = gan * 0.50
if 1595 < prom:
   multa = gan * 0.75


print(f"La multa es de : {multa}")