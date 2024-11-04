"""7) Dado el escenario en el cual se encuentran dos personas intentando comer sopa pero
se encuentran con que solo tienen una cuchara para hacerlo. ¿Qué tipo de problema
con hilos se produce? ¿Cómo se resolvería?"""

#se van turnando, esto se resuelve con una queue

from multiprocessing import Process, Queue

class Sopa(Process):
    
    def __init__(self, cola):
        super().__init__()
        self.plato = cola
    
    def run(self):
        for cucharada in range(1, 7):  # Total de 6 cucharadas
            self.plato.put(f'Cucharada {cucharada}')
            
        
class Mogo1(Process):
    
    def __init__(self, cola):
        super().__init__()
        self.estomago = cola
        
    def run(self):
        for _ in range(3):  # Mogo1 consume 3 cucharadas
            cucharada = self.estomago.get()
            print(f'Mogolico1 - mi estómago recibe: la {cucharada}')
            
            
class Mogo2(Process):
    
    def __init__(self, cola):
        super().__init__()
        self.estomago = cola
        
    def run(self):
        for _ in range(3):  # Mogo2 consume 3 cucharadas
            cucharada = self.estomago.get()
            print(f'Mogolico2 - mi estómago recibe: la {cucharada}')
            

if __name__ == '__main__':
    sopa_compartida = Queue()
    
    sopa = Sopa(sopa_compartida)
    down1 = Mogo1(sopa_compartida)
    down2 = Mogo2(sopa_compartida)
    
    sopa.start()
    down1.start()
    down2.start()

    sopa.join()
    down1.join()
    down2.join()
