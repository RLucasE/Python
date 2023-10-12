rak1 = 0
rak2 = 0
promDiam = 0
CDP = int(input("CDP del caño: "))
digAux = 0
pintado = False


while (CDP != 0):
   
    for i in range(3):
        digAux = CDP % 10
        CDP = CDP // 10
        print(digAux) 

        if(i == 0):
            if(digAux == 0): pintado = True
        if(i == 1):
            if((digAux >= 4) and pintado):
                rak1+=1
            else: rak2+=1
        if(i == 2) 

    
    CDP = int(input("CDP del caño: "))





