from bottle import route, run, template
from compteur import *
import os, psutil, socket

master = 'Mathieu'

@route('/')
def stat(): 
 
    return "<b> Hostname : </b>" + str(socket.gethostname()) + "<br>" \
           "<b> CPU is : </b>" + str(psutil.cpu_percent()) + "% <br>" \
           "<b> Ram is : </b>" + str(psutil.virtual_memory().percent) + "% <br>" \
	   "<b> Nombre de visites : </b>" + str(lire_compteur())


@route('/hello/<name>')
def index(name):

    return "Hello " + str(name)


@route('/temp')
def temp():

    return "Le grand chef est : " + master


run(host='0.0.0.0', port=80)



