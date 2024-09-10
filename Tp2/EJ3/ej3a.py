from Tp2.EJ3.ej3 import Alumno

alumno1 = Alumno()
alumno1=alumno1.iniciar()
alumno1.setnombre("Alejandro")
alumno1.setapellido("Rojas")
alumno1.setdni(1111111111)


alumno2=Alumno().iniciar_con_nom_ape("Martin","Rosales")
alumno2.setdni(1111111112)


print(f'{alumno1.getNombreYapellido()}{" - DNI: "}{alumno1.getDni()}')
print(f'{alumno2.getNombreYapellido()}{" - DNI: "}{alumno2.getDni()}')