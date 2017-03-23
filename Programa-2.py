#-- 2.realiza una funcion que permita tener el volumen de una esfera. --

def esfera(x):

	volu = (4/3)*(3.1416)*(x^3)

	return volu,x

volumen, a = esfera(10)

print "el resultado de " , a , " su volumen es: " , volumen