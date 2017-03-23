#-- 10. Crear un programa que por medio de recursion calcule la suma de los cuadrados de n numeros. --
def recursive (dato, variable=0):
    if(dato>=0):
        variable+=dato**2
        return recu(dato-1,variable)
    else:
        print variable

recursive(3, 1)