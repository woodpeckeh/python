#-- 4. realiza una funcion que permita tener el maximo de 3 numeros --

def mayor(a,b,c):

	may = ''

	if a > b:
		if a > c:
			may=a
	else:
		if b > a:
			if b > c:
				may=b
			else:
				may=c

	return may,a,b,c
mayo, x , y , z = mayor(4,10,3)

print "de los numeros: " , x , " , " , y , " , " , z , " el mayor es: " , mayo