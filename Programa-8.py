#-- 8. Realiza un programa que permita generar un intervalo de n numeros entre 20 y 60 --
def intervaloN (x):
        cont=1
        while cont<=x:
                if cont>=20 and cont<=60:
                        print cont
                cont+=1

x=input("Cantidad de numeros ?: ")
intervaloN(x)