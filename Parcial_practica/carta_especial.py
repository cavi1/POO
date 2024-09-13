from carta import Carta
import random

class Carta_especial(Carta):
    def __init__(self,nombre,equipo,pais):
        super().__init__(nombre,equipo,pais)
        self.__lista_habilidades_especiales=[]
        self.set_habilidades_especiales()


    def set_atributos(self):
        super().set_atributos(89,99)
        self._velocidad=int(min(99,self._velocidad+ self._velocidad*0.02))#me esta diciendo que va a ser ó 99 o el valor + el 2% en caso de no ser 99
        self._regate=int(min(99,self._regate+ self._regate*0.02))
        self._pase=int(min(99,self._pase+ self._pase*0.02))
        self._defensa=int(min(99,self._defensa+ self._defensa*0.02))
        self._fisico=int(min(99,self._fisico+ self._fisico*0.02))
        self._tiro=int(min(99,self._tiro+ self._tiro*0.02))
        
    def calcular_quimica(self, pais_fav_plantilla, equipo_fav_plantilla):
        self._quimica= 100
    
    def set_habilidades_especiales(self):
        aleat=random.randint(1,3)
        lista=["ataque","defensa","pase"]
        for i in range(aleat):
            self.__lista_habilidades_especiales.append(random.choice(lista))
            temp=self.__lista_habilidades_especiales[i]
            lista.remove(temp)

    def carta_to_string(self):
        return f"Habilidad Especial: \n{" ".join(self.__lista_habilidades_especiales)}\n{super().carta_to_string()}"