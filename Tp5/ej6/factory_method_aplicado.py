from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):

# -> anotation, permite indicar que es lo que se devuelve, pero no obliga.
    @abstractmethod
    def factory_method(self):
        pass

    def notificar(self) -> str:
        notificador = self.factory_method()
        result = f"Creator: notifico al usuario con: {notificador.notificar_usuario()}"

        return result


class ConcreteCreatorEmail(Creator):

    def factory_method(self) -> Notificacion:
        return EmailNotificacion()

class ConcreteCreatorSMS(Creator):
    def factory_method(self) -> Notificacion:
        return SMSNotificacion()

class ConcreteCreatorPush(Creator):
    def factory_method(self) -> Notificacion:
        return PushNotificacion()


class Notificacion(ABC):
    @abstractmethod
    def notificar_usuario(self) -> str:
        pass

class EmailNotificacion(Notificacion):
    def notificar_usuario(self) -> str:
        return "Envio email"


class SMSNotificacion(Notificacion):
    def notificar_usuario(self) -> str:
        return "Envio SMS"

class PushNotificacion(Notificacion):
    def notificar_usuario(self) -> str:
        return "Envio notificación push"


def enviar_notificacion(creator: Creator) -> None:
    print(f"Cliente: No se sabe de que forma se envia la notificación, pero se que se lo puedo pedir.\n"
        f"{creator.notificar()}", end="")



print("Enviar notificación por EMAIL")
enviar_notificacion(ConcreteCreatorEmail())
print("\n")

print("Enviar notificación por SMS")
enviar_notificacion(ConcreteCreatorSMS())