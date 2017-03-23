#-- 7. Realiza un programa que permita generar un intervalo de los cuadrados de n numeros mayores a 100. --
def intervaloMayor(x):
        vacio=[(conta**2) for conta in range(1,x+1)]        
        num=1
        while num<len(vacio):
                if vacio[num]>100:
                        print vacio[num]
                num+=1

x=input("Ingresa el rango: ")
intervaloMayor(x)