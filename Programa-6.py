#-- 6. Realiza un programa que permita generar un intervalo de la suma de los cubos de los primeros n numeros. Ejemplo suma = 1 + 8 + 27 + n --
def sumaCubos(x):      
        cubos=[(contador**3) for contador in range(1,x+1)]        
        print cubos
        return sum(cubos)

x=input("Cantidad de numeros: ")
sumaCubos(x)