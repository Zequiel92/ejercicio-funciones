# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def añoBisiesto(año):

	if año % 4 == 0:
		if año % 100:
			if año % 400:

				print("es bisiesto")

			else:
				print("el año no es bisiesto")
		else:
			print("el año no es bisiesto")
	else:
		print("el año no es bisiesto")


añoBisiesto(2016)
		
