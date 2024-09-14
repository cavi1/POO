class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f'{self.marca} {self.modelo}'

mi_coche = Coche("Toyota", "Corolla")
print(mi_coche)  # Output: Toyota Corolla
