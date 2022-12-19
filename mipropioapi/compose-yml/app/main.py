cesar@op:~/pei2/07apipropio$ ls
api  docker-compose.yml
cesar@op:~/pei2/07apipropio$ vim docker-compose.yml 
cesar@op:~/pei2/07apipropio$ cd app
-bash: cd: app: No such file or directory
cesar@op:~/pei2/07apipropio$ cd api/app
cesar@op:~/pei2/07apipropio/api/app$ vim main.py 
cesar@op:~/pei2/07apipropio/api/app$ rm main.py 
cesar@op:~/pei2/07apipropio/api/app$ vim ma
cesar@op:~/pei2/07apipropio/api/app$ vim main.py 
cesar@op:~/pei2/07apipropio/api/app$ vim main.py 
cesar@op:~/pei2/07apipropio/api/app$ vim main.py 
cesar@op:~/pei2/07apipropio/api/app$ cd
cesar@op:~$ cd pei2/
cesar@op:~/pei2$ cd 07apipropio/
cesar@op:~/pei2/07apipropio$ ls
api  docker-compose.yml
cesar@op:~/pei2/07apipropio$ vim docker-compose.yml 
cesar@op:~/pei2/07apipropio$ sudo service apache2 stop
cesar@op:~/pei2/07apipropio$ cd ..
cesar@op:~/pei2$ cd 07
-bash: cd: 07: No such file or directory
cesar@op:~/pei2$ cd 07apipropio/
cesar@op:~/pei2/07apipropio$ vim docker-compose.yml 
cesar@op:~/pei2/07apipropio$ vim docker-compose.yml 
cesar@op:~/pei2/07apipropio$ cd api
cesar@op:~/pei2/07apipropio/api$ cd app
cesar@op:~/pei2/07apipropio/api/app$ ls
__pycache__  basedatos.py  catalog.py  main.py  static  templates
cesar@op:~/pei2/07apipropio/api/app$ vim main.py 
cesar@op:~/pei2/07apipropio/api/app$ cd ..
cesar@op:~/pei2/07apipropio/api$ cd ..
cesar@op:~/pei2/07apipropio$ ls
api  docker-compose.yml
cesar@op:~/pei2/07apipropio$ vim docker-compose.yml 
cesar@op:~/pei2/07apipropio$ vim /api/app/ma
cesar@op:~/pei2/07apipropio$ vim /api/app/main.py
cesar@op:~/pei2/07apipropio$ cd api
cesar@op:~/pei2/07apipropio/api$ cd app
cesar@op:~/pei2/07apipropio/api/app$ vim main.py 
cesar@op:~/pei2/07apipropio/api/app$ nano main.py 
cesar@op:~/pei2/07apipropio/api/app$ 
cesar@op:~/pei2/07apipropio/api/app$ nano main.py 









  GNU nano 5.4                                        main.py                                                  
#!/usr/bin/env python
 
from flask import jsonify
import flask
import socket
import os
from basedatos import contador_visitas 
from catalog import get_products, create_product 

APP = flask.Flask(__name__)
PORT=os.environ["PORT"]

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
    APP.debug = True
    APP.run(host='0.0.0.0', port=PORT)