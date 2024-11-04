"""El sistema nacional de datos del mar cuenta con 2 boyas ubicadas en el golfo San
Jorge, llamadas CIDMAR-1 y CIDMAR-2 estas cuentan con una gran cantidad de
sensores pero solo se pedirán los siguientes:
● Temperatura ambiente (Termómetro): los valores promedio rondan
entre 5.0 a 30.0 grados centígrados
● Velocidad del viento (Anemómetro): los valores promedio rondan
entre 0 a 60km/h Las clases Termómetro y anemómetro
implementan la interfaz sensor, que es la siguiente:
public interface Sensor {
public Double sensar();
}
La boya debe generar 5 paquetes de datos y enviarlos al servidor, el cual se encarga de
almacenarlos en su cola de paquetes.

El envío de paquete tiene una probabilidad del 40% de fallar, cuando eso pase debe
imprimir en consola el mensaje:
“ERROR: CIDMAR-1 Hubo una falla en la comunicación, se
perdió el paquete”
con la ayuda de una excepción creada por usted mismo.
El proceso de enviar un paquete consume 5000 milisegundos.
Al momento de almacenar un paquete y consultar el servidor se encarga de imprimir
por pantalla la acción.
El científico se encarga de consultar los datos al servidor y anotarlos en su cuaderno
(colaPaquetes), por último, realiza un informe con los promedios de temperatura y
velocidad de viento para cada boya.
El programa no se debe bloquear, debe respetar el orden de producción y consumición
y finalizar su ejecución correctamente.
"""

from multiprocessing import Process, Queue
from abc import ABC, abstractmethod
import random 
import time

class Sensor(ABC):
    
    @abstractmethod
    def sensar(self):
        pass
    

class Termometro(Sensor):
    
    def __init__(self):
        self.__temp_ambiente=self.sensar()
    
    def sensar(self):
        self.__temp_ambiente=random.uniform(5.0,30.0)
        return self.__temp_ambiente
    
    
class Anemometro(Sensor):
    
    def __init__(self):
        self.__vel_viento=self.sensar()
        
    def sensar(self):
        self.__vel_viento=random.uniform(0.0,60.0)
        return self.__vel_viento
    

class Boya(Process):
    
    def __init__(self, nombre_boya, cola_paquetes, termometroX=Termometro, anemometroX=Anemometro):
        super().__init__()
        self.__nombre_boya = nombre_boya
        self.__paquetes = cola_paquetes
        self.__anemometro = anemometroX
        self.__termometro = termometroX
    
    def run(self):
        for paquete in range(5):
            mensaje = {
                'nombre_boya': self.__nombre_boya,
                'datos': f'Temperatura: {self.__anemometro.sensar()} Velocidad del viento: {self.__termometro.sensar()}'
            }
            self.__paquetes.put(mensaje)

            

class Packet_loss(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class Servidor(Process):
    
    def __init__(self, cola_paquetes):
        super().__init__()
        self.__cola_paquetes = cola_paquetes
        
    def run(self):
        while not self.__cola_paquetes.empty():
            try:
                prob_falla = random.random()  # Evaluar en cada iteración
                if prob_falla < .4:
                    mensaje = self.__cola_paquetes.get()
                    nombre_boya = mensaje['nombre_boya']
                    raise Packet_loss(f"ERROR: {nombre_boya} Hubo una falla en la comunicación, se perdió el paquete")
                else:
                    mensaje = self.__cola_paquetes.get()
                    print(f"Servidor recepcionó: {mensaje['nombre_boya']} - {mensaje['datos']}")
            except Packet_loss as e:
                print(e)  # Captura la excepción y sigue la ejecución
            
    
    
    
packet_sharing=Queue()
anem1=Anemometro()
term1=Termometro()
server=Servidor(packet_sharing)
boya1=Boya('CIDMAR-1', packet_sharing, term1, anem1)


if __name__ == '__main__':
    
    boya1.start()
    server.start()
    
    boya1.join()
    server.join()