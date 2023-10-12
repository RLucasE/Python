##Primer ingreso
precioDeVta = int(input("Ingreese el presio unitario: "))
codigo = int(input("Ingreese el codigo del producto: "))

prom = 0
descuento15Cont = 0
descuento18Cont = 0
total = 0


while(codigo != 0):
   codigo = codigo // 10 ##Quitar el primer digito

   for i in range(5):
      digAux = codigo % 10
      prom += digAux
      codigo = codigo // 10



   ##Calcular promdio, contar y sumar
   prom = prom / 5
   if(prom >= 5):
      descuento15Cont = descuento15Cont + 1
      total = total + precioDeVta * 0.15
   else:
      descuento18Cont = descuento18Cont + 1
      total = total + precioDeVta * 0.18

       
   codigo = int(input("Ingreese el codigo del producto: "))
   prom = 0


##Salida de datos
print(f"Total de vasitos con deescuento del 15%: {descuento15Cont}")
print(f"Total de vasitos con deescuento del 18%: {descuento18Cont}")
print(f"See deberá resignar un total de ${total} para llevar a cabo esta premiación")
