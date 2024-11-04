from  multiprocessing import Process, Pipe

class ProcesoEnvio(Process):
    def __init__(self, canal):
        super(ProcesoEnvio, self).__init__() #es otra forma de llamar al constructor
        self.canal = canal

    def run(self):
        mensajes = ["Hola", "Alumnos","de", "POO"]
        for mensaje in mensajes:
            print(f"Enviando: {mensaje}")
            self.canal.send(mensaje)
        self.canal.send(None)

class ProcesoRecepcion(Process):
    def __init__(self, canal):
        super(ProcesoRecepcion, self).__init__()
        self.canal = canal

    def run(self):  #el none sirve para podefr decirle cuando termina el mensaje
        mensaje = ""
        while mensaje is not None:
            mensaje = self.canal.recv()
            if mensaje is not None: 
                print(f"Recibido: {mensaje}")

if __name__ == '__main__':
    pipe_conn1, pipe_conn2 = Pipe() #devuelve dos pipes siempre

    proceso_envio = ProcesoEnvio(pipe_conn1)
    proceso_recepcion = ProcesoRecepcion(pipe_conn2)

    proceso_envio.start()
    proceso_recepcion.start()

    proceso_envio.join()
    proceso_recepcion.join()
    print("fin de la ejecución")
