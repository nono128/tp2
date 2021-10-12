from bottle import route, run, template
from compteur import *


@route('/')
def count():

	return "Nombre de visites : " + str(lire_compteur())



run(host='0.0.0.0', port=8098)




