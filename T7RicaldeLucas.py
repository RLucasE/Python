import numpy as np

def ingresarProductos(mat,m,n):

    for i in range (m):
        print(f"Producto {i+1}")
        fila = np.empty(n,dtype="int")
        for j in range(n):
            fila[j] = int(input(f"Mes {j+1}: "))
        mat = np.append(mat,[fila],axis=0)
    
    return mat
       
        

def mostrarFilas(mat):
    for i in range((mat.shape)[0]):
        print(f"Producto {i+1}:")
        for j in range((mat.shape)[1]):
            print(f"Mes {j+1}: {mat[i][j]}")

def mayorVentaDeUnProducto(mat,idProducto):
    indiceProducto = idProducto-1
    maximo = 0
    for j in range(mat.shape[1]):
        if(mat[indiceProducto][j] > mat[indiceProducto][maximo]):
            maximo = j
    return maximo + 1

def menorVentaDeUnMes(mat,mes):
    indiceMes = mes-1
    minimo = 0
    for j in range(mat.shape[0]):
        print(mat[j][indiceMes])
        if(mat[j][indiceMes] < mat[minimo][indiceMes]):
            minimo = j
    return minimo + 1

def agregarUnMes(mat):
       
        col = np.empty(mat.shape[0],dtype="int")
        for j in range(mat.shape[0]):
            col[j] = int(input(f"Producto {j+1} en el mes: "))
        mat = np.append(mat,[col].transpose(),axis=1)
    
        return mat

def main():
    m = int(input("Cantidad de productos:"))
    n = int(input("Cantidad de meses. Máx=12: "))
    mat = np.zeros((0,n),dtype="int")
    mat = ingresarProductos(mat,m,n)
    mostrarFilas(mat)
    producto = int(input(f"Elegir un producto para ver el mes con mayor venta (valor entre 1 y {mat.shape[0]} incluidos): "))
    print(f"Maximo mes= {mayorVentaDeUnProducto(mat,producto)}")
    mes = int(input(f"Elegir un mes para ver el producto con menor venta (valor entre 1 y {mat.shape[1]} incluidos): "))
    print(f"Maximo producto= {menorVentaDeUnMes(mat,mes)}")
    mat = agregarUnMes(mat)
    mostrarFilas(mat)
main()