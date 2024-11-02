"""12. Patrón Strategy.
En una plataforma de streaming de películas se desea consultar el catálogo. Sin
embargo hay diferentes situaciones que podrían llevar a qué el sea filtrado de diferentes
formas, un ejemplo de ello es cuando la cuenta que está usando el sistema pertenece a
un niño. En este caso el catálogo solo debe mostrar películas que no sean para
mayores de 13 años.
Utilizando el patrón strategy defina una estrategia general que retorne el catálogo
completo y luego una estrategia para niños que filtra las películas por edad.
Escriba en consola el listado implementando la estrategia para todo el catálogo. Luego
imprima el listado usando la estrategia para menores de 13.
Finalmente, implemente una tercera estrategia que retorne el catálogo de películas para
menores de 18 años. Compruebe el resultado en consola. +18  (13;18) -13"""

from abc import ABC, abstractmethod

class Plataforma_streaming:
    
    def __init__(self, tipo_publico):
        self.__restricciones=tipo_publico
        self.__catalogo_peliculas = { #un catálogo ficticio para probar el codigo
            "Coco": "-13",
            "Deadpool": "+18",
            "Mi vecino Totoro": "-13",
            "La La Land": "+13",
            "El rey león": "-13",
            "Pulp Fiction": "+18",
            "Toy Story": "-13",
            "El lobo de Wall Street": "+18",
            "Wonder Woman": "+13",
            "Harry Potter y la piedra filosofal": "-13"
        }
    def get_catalogo(self):
        self.__restricciones.ver_catalogo(self.__catalogo_peliculas)
        

class Publico(ABC):

    @abstractmethod
    def ver_catalogo(self, catalogo):
        pass
    
    
class Nino(Publico):
    
    def ver_catalogo(self, catalogo):
        print("Peliculas disponibles para niños: \n")
        for nombre_pelicula, edad in catalogo.items():
            if edad == '-13':
                print(f'Pelicula: {nombre_pelicula} Edad: {edad}')


class Adolescente(Publico):
    
    def ver_catalogo(self, catalogo):
        print("Peliculas disponibles para adolescentes: \n")
        for nombre_pelicula, edad in catalogo.items():
            if edad == '-13' or edad=='+13':
                print(f'Pelicula: {nombre_pelicula} Edad: {edad}')


class Adulto(Publico):
    
    def ver_catalogo(self, catalogo):
        print("Peliculas disponibles para adultos: \n")
        for nombre_pelicula, edad in catalogo.items():
                print(f'Pelicula: {nombre_pelicula} Edad: {edad}')
                

Nino1=Nino()
Adolescente1=Adolescente()
Adulto1=Adulto()
netflix=Plataforma_streaming(Adulto1)
netflix.get_catalogo()
