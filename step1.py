#Fonction pour compter nombre d'occurrances d'un digital dans un chiffre
def nombresoccurrances(num, d):
	count = 0
	while (num > 0):
		if(num % 10 == d):
			count = count + 1

		num = num // 10
	return count

while (True):
	number = input('Entrez un nombre: ')
	n =int(number)
	cont3 = nombresoccurrances(n, 3)
	cont5 = nombresoccurrances(n, 5)
	cont7 = nombresoccurrances(n, 7)

	str_to_print = ""
	if n%3 == 0:
		str_to_print = str_to_print + "Toto"
	if n%5 == 0:
		str_to_print = str_to_print + "Tutu"
	if n%7 == 0:
		str_to_print = str_to_print + "Titi" 

	while (cont3 > 0):
	 	str_to_print = str_to_print + "Toto"
	 	cont3 = cont3 - 1
	while (cont5 > 0):
		str_to_print = str_to_print + "Tutu"
		cont5 = cont5 - 1
	while (cont7 > 0):
		str_to_print = str_to_print + "Titi"
		cont7 = cont7 - 1
	print ( number + " => " + str_to_print )


