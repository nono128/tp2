from bottle import route, run, template
from compteur import *
import os, socket, psutil

@route('/')
def stat():

    return "<b> Hostname : </b>" + str(socket.gethostname()) + "<br>" \
           "<b> CPU is : </b>" + str(psutil.cpu_percent()) + "% <br>" \
           "<b> Ram is : </b>" + str(psutil.virtual_memory().percent) + "% <br>" \
	   "<b> Nombre de visites :</b>" + str(lire_compteur())




#return "Nombre de visites : " + str(lire_compteur())



run(host='0.0.0.0', port=8098)



