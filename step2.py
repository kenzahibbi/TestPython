#Fonction pour compter nombre d'occurrances d'un digital dans un chiffre
def nombresoccurrances(num, d):
	count = 0
	while (num > 0):
		if(num % 10 == d):
			count = count + 1

		num = num // 10
	return count


while (True):
	# Driver code
	number = input('Entrez un nombre: ')

	n =int(number)
	#Obtenir le nombre d occurrance de 3
	cont3 = nombresoccurrances(n, 3)
	#Obtenir le nombre d occurrance de 5
	cont5 = nombresoccurrances(n, 5)
	#Obtenir le nombre d occurrance de 7
	cont7 = nombresoccurrances(n, 7)
	#Obtenir le nombre d occurrance de 0
	cont0 = nombresoccurrances(n, 0)

	#variable pour savoir si le nombre est divisble
	div = 0

	str_to_print = ""
	if n%3 == 0:
		str_to_print = str_to_print + "Toto"
		div = 1
	if n%5 == 0:
		str_to_print = str_to_print + "Tutu"
		div = 1
	if n%7 == 0:
		str_to_print = str_to_print + "Titi"
		div = 1 

	while (cont3 > 0):
		div = 1
		str_to_print = str_to_print + "Toto"
		cont3 = cont3 - 1
	while (cont5 > 0):
		div = 1
		str_to_print = str_to_print + "Tutu"
		cont5 = cont5 - 1
	while (cont7 > 0):
		div = 1
		str_to_print = str_to_print + "Titi"
		cont7 = cont7 - 1
	while (cont0 > 0):
		str_to_print = str_to_print + "*"
		cont0 = cont0 - 1

	# verifier si le nombre n'est pas divisible faire un simple replace de 0 par *  
	if div == 0:
		str_to_print = number.replace("0", "*")
	 
	print ( number + " => " + str_to_print )

