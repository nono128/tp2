from bottle import route, run, template
import os, psutil, socket

master = 'Mathieu'

@route('/')
def stat(): 
 
    return "<b> Hostname : </b>" + str(socket.gethostname()) + "<br>" \
           "<b> CPU is : </b>" + str(psutil.cpu_percent()) + "% <br>" \
           "<b> Ram is : </b>" + str(psutil.virtual_memory().percent) + "% <br>"


@route('/hello/<name>')
def index(name):

    return "Hello " + str(name)


@route('/temp')
def temp():

    return "Le grand chef est : " + master


run(host='localhost', port=8095)























#     return "The cpu  is : " + str(psutil.cpu_percent())

#     return "The ram usage is at : " + str(psutil.virtual_memory()) + "%"

#      print(str(socket.gethostname))

