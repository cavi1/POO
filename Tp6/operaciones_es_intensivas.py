import random
import requests
import sqlite3
from threading import Thread
import time


class ProcesadorArchivos(Thread):

    def run(self):
        timestamp = time.time()
        print("ProcesadorArchivos: inicia escritura de archivo")
        with open("salida.txt", "w") as archivo_escritura:
            for _ in range(10000000):
                archivo_escritura.write(str(random.random()))
        print("ProcesadorArchivos: fin escritura de archivo = "+str(time.time() - timestamp))

class SolicitudRed(Thread):
    
    def run(self):
        timestamp = time.time()
        print("SolicitudRed: inicia petición API")
        url = "https://api.weather.gov/gridpoints/TOP/31,80/forecast"
        respuesta = requests.get(url)

        if respuesta.status_code == 200:
            datos = str(respuesta.json())
       #     print("SolicitudRed: "+ datos)
        print("SolicitudRed: fin petición API = "+str(time.time() - timestamp))

class OperacionDatabase(Thread):
    
    def run(self):
        timestamp = time.time()
        print("OperacionDatabase: inicia petición en BD")
        conexion = sqlite3.connect("base_de_datos.db")
        cursor = conexion.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS datos (
                            id INTEGER PRIMARY KEY,
                            valor INTEGER
                        )''')

        conexion.commit()
        for _ in range(1000):
            cursor.execute("INSERT INTO datos (valor) VALUES ("+str(random.random())+")")
            conexion.commit()
        conexion.close()
        print("OperacionDatabase: fin petición en BD = "+str(time.time() - timestamp))


class DescargarArchivos(Thread):
    
    def run(self):
        timestamp = time.time()
        print("DescargarArchivos: inicia descarga de archivo zip")
        url = "https://drive.google.com/u/0/uc?id=1WswdvJ9Rc3VqLpcuhBjXTKUUSnNod0IJ&export=download&confirm=t&uuid=9654d483-3185-481b-ae6c-cc38467332fc&at=AB6BwCDqi7wMPutkBFfP8Cs73E7a:1696961728349"
        respuesta = requests.get(url, stream=True)

        if respuesta.status_code == 200:
            with open("archivo_descargado.zip", "wb") as archivo:
                for chunk in respuesta.iter_content(chunk_size=1024):
                    if chunk:
                        archivo.write(chunk)
        print("DescargarArchivos: fin descarga de archivo zip = "+str(time.time() - timestamp))

hilos = [ProcesadorArchivos(),SolicitudRed(),OperacionDatabase(),DescargarArchivos()]
timestamp = time.time()
for hilo in hilos:
    hilo.start() #probar ejecucion sencuencial cambiando a run y comentando el join

for hilo in hilos:
    hilo.join()

print("Terminan los procesos = "+str(time.time() - timestamp))
