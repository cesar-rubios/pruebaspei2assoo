#!/usr/bin/env python
 
from flask import jsonify
import flask
import socket
import os
from basedatos import contador_visitas 
from catalog import get_products, create_product 

APP = flask.Flask(__name__)

userinfo = {
    'nombre': 'César',
    'apellido': 'Rubio',
    'edad': '22',
    'ocupacion': 'estudiante'
}


@APP.route('/')
def index():
    
    hostname = socket.gethostname()

    return flask.render_template('index.html',
                titulo="Indice",
                user=userinfo, 
                server_name=hostname,
                num_visitas=contador_visitas()
                )

@APP.route('/hola')
def saludo():

    #redis_cli.incr('num_visitas')
    #visitas = redis_cli.get('num_visitas')

    return flask.render_template('index.html',
            titulo='Hola, bienvenido',
            user=userinfo,
            num_visitas=contador_visitas()
            )

@APP.route('/adios')
def despedida():

        return flask.render_template('index.html',
            titulo='Adios, nos vemos',
            user=userinfo,
            num_visitas=contador_visitas()
            )    

@APP.route('/catalog')
def catalog():
    response = get_products()
    return jsonify(response)



if __name__ == '__main__':
    PORT = os.environ['PORT']
    APP.debug = True
    APP.run(host='0.0.0.0', port=PORT)
