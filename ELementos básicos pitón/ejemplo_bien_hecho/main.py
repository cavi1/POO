from Serie import Serie
from Categoria import Categoria

serie = Serie("imagen", "breaking bad", "Estrena todos los jueves")
serie1 = Serie("imagen", "game of thrones", "Estrena todos los jueves")
serie2 = Serie("imagen", "morty", "Estrena todos los jueves")
categoria = Categoria("Estreno semanal")
categoria.agregar_serie(serie)
categoria.agregar_serie(serie1)
categoria.agregar_serie(serie2)
categoria.imprimir()