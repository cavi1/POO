from materia import Materia
from profesor import Profesor

poo = Materia("POO","IF153")
algebra = Materia("Algebra",183)
introduccion = Materia("Introducción a la computación"," ")
introduccion.set_codigo("IF300")
algoritmica = Materia("Algoritmica","500")

profesores=[]

profesor1 = Profesor("Pedro","Hernandez")
profesor1.add_materia(poo)
profesor1.add_materia(algebra)
profesores.append(profesor1)

profesor2=Profesor("Romina","Alvarez")
profesor2.add_materia(introduccion)
profesor2.add_materia(algoritmica)
profesores.append(profesor2)
profesor3=Profesor("Laura","Perez")
profesores.append(profesor3)


for pro in profesores:
    print(f"Profesor: {pro.get_nombre()} {pro.get_apellido()}")
    print("Materias: ")
    for mat in pro.get_materias():
        print(mat.getNombre())
        
