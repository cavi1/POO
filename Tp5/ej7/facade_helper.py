

"""7. Patrón Facade.
Cree una clase Helper con un método que permita traducir una palabra de español a
inglés. Establezca traducciones para al menos 5 palabras.
Cree una clase Helper dos métodos: uno que convierta una cadena a mayúsculas y
otro que convierta a minúsculas.
Luego, implemente un patrón Facade para permitir el acceso a estos tres métodos
desde una nueva clase.
Para probar la solución, elija tres palabras e imprima para cada una
● Su traducción a inglés
● Su versión con solo mayúsculas
● Su versión con solo minúsculas"""

from googletrans import Translator  

class Facade:

    def __init__(self):  # los atributos de mi fachada son los subsistemas o bien se los paso de parametro en el cliente
        self.__subsistema1 = Helper1()
        self.__subsistema2 = Helper2()

    def traduccion_lower_y_upper(self, palabra):  # yo solo rescato lo que me interesa de ellos
        return f'Traducción: {self.__subsistema1.traducir(palabra)}, todo minus: {self.__subsistema2.todo_minus(palabra)} todo mayus: {self.__subsistema2.todo_mayus(palabra)}'

class Helper1:  # subsistema1 con varios métodos, entre ellos..
    
    def traducir(self, palabra):
        translator = Translator()  # Crea una instancia del traductor
        traduccion = translator.translate(palabra, src='es', dest='en')
        return traduccion.text  # Devuelve el texto traducido

class Helper2:  # subsistema2 con varios métodos, entre ellos..

    def todo_minus(self, palabra):
        palabra = palabra.lower()
        return palabra

    def todo_mayus(self, palabra):
        palabra = palabra.upper()
        return palabra

def codigo_cliente(facade: Facade, palabra):
    print(facade.traduccion_lower_y_upper(palabra))

fachada = Facade()
codigo_cliente(fachada, 'auto')