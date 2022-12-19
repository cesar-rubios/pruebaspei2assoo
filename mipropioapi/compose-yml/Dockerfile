FROM python:3.9
#comenzamos importando la imagen de pytohn 3.9

#creamos una carpeta para la aplicación web
RUN mkdir -p /app

#y la declaramos como la carpeta de trabajo
WORKDIR /app

#copiamos el archivo de requirements.txt dentro 
#de la imagen del contenedor
COPY requirements.txt /app

#instalamos las dependencias descritas en el archivo
RUN pip install --no-cache-dir -r requirements.txt

#copiamos la aplicación web dentro de la imagen
COPY ./app /app

#puerto de escucha del contendor
#dentro del código de python haremos su función
EXPOSE 5000

#ejecutamos el programa principal
CMD python main.py