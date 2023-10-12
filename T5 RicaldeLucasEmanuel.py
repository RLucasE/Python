import os
band = True
listaCodigo = []
listaNombre = []
listaStock = []
listaCantidad = []
listaPrecio = []

os.system('cls')
while band:
    print("Menú:") 
    print("1. Registrar un producto nuevo")
    print("2. Borrar un producto")
    print("3. Mostrar productos")
    print("4. Hacer una venta")
    print("5. Salir")
    opcion = input("Ingresar una opcion: ")


    if opcion == '1': ##Agregar un producto no registrado

        codigo = int(input("Codigo del producto: "))
        
        if codigo in listaCodigo:
            print("Ese producto ya está ")
        else:
            nombre = input("Descripcion: ")
            stock = int(input("Ingrese el stock: "))
            cantidad = 0
            precio = int(input("Ingrese el precio: "))

            listaCodigo.append(codigo)
            listaNombre.append(nombre)
            listaStock.append(stock)
            listaCantidad.append(cantidad)
            listaPrecio.append(precio)

    elif opcion == '2': ##Eliminar un producto registrado
        codigo = int(input("Codigo del producto que quiere eliminar: "))
        if codigo in listaCodigo:
            indice = listaCodigo.index(codigo)

            listaCodigo.pop(indice)
            listaNombre.pop(indice)
            listaStock.pop(indice)
            listaCantidad.pop(indice)
            listaPrecio.pop(indice)
        else: print("El producto no se encuentra en la lista..")
    elif opcion == '3': ##Mostrar productos
        for i in range(len(listaCodigo)):
            print("---------------------------")
            print(f"Codigo del producto: {listaCodigo[i]}")
            print(f"Descripcion: {listaNombre[i]}")
            print(f"Stock: {listaStock[i]}")
            print(f"Cantidad de ventas: {listaCantidad[i]}")
            print(f"Precio: {listaPrecio[i]}")
            print("---------------------------")
    elif opcion == '4': ##Vender un producto
        codigo = int(input("Codigo del producto que quiere vender: "))

        if codigo in listaCodigo:
            cantidad = int(input("Cantidad de ventas: "))

            indice = listaCodigo.index(codigo)
            if(listaStock[indice] >= cantidad):
                listaStock[indice] -= cantidad
                listaCantidad[indice] += cantidad
            else: print("No contamos con stock suficiente")
        else: print("El producto no se encuentra en la lista..")

    elif opcion == '5': 
        print("Saliendo...")
        band = False
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")

    input("Presione una tecla para continuar")
    os.system('cls')

  