#-- 1. realiza un programa o funcion y que permita tener la media de 3 numeros. --

def media(x,y,z):

	result = (x+y+z)/3 

	return result,x,y,z

valor, v1, v2, v3 = media(10,8,10)

print "la media de:", v1 , "," , v2 , "," , v3 , "," , "es: ", valor