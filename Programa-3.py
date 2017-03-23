#-- 3.realiza una funcion que permita tener la intercalacion de 10 numeros impares iniciando con el 13 --

def intercala(x):

	num=x
	impar=''
	while num <= 31:
		if num%2 !=0:
			impar+='%i, ' % num 
		num+=1
	return num, impar

numero, lista = intercala(13)

print "lista de numeros impares : ", lista