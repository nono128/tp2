from bottle import route, run, template
from compteur.py import *


@route('/')
def count():

    return "yo le sang : " + str(lire_compteur())



run(host='0.0.0.0', port=8098)


