# Ejemplo de Programación Orientada a Objetos: Sistema de Vehículos

# Clase base Vehículo para representar conceptos generales
class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        # Atributos privados
        self.__marca = marca
        self.__modelo = modelo
        self.__velocidad_maxima = velocidad_maxima
        self.__velocidad_actual = 0

    def atributos(self):
        print(f"Vehículo: {self.__marca} {self.__modelo}")
        print(f"· Velocidad máxima: {self.__velocidad_maxima} km/h")
        print(f"· Velocidad actual: {self.__velocidad_actual} km/h")

    def acelerar(self, incremento):
        self.__velocidad_actual += incremento
        if self.__velocidad_actual > self.__velocidad_maxima:
            self.__velocidad_actual = self.__velocidad_maxima
        print(f"{self.__marca} {self.__modelo} ha acelerado a {self.__velocidad_actual} km/h.")

    def frenar(self, decremento):
        self.__velocidad_actual -= decremento
        if self.__velocidad_actual < 0:
            self.__velocidad_actual = 0
        print(f"{self.__marca} {self.__modelo} ha frenado a {self.__velocidad_actual} km/h.")

    # Método abstracto
    def tipo_vehiculo(self):
        raise NotImplementedError("Este método debe ser implementado en una subclase.")


# Subclases que heredan de Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, puertas):
        super().__init__(marca, modelo, velocidad_maxima)
        self.__puertas = puertas

    def atributos(self):
        super().atributos()
        print(f"· Número de puertas: {self.__puertas}")

    def tipo_vehiculo(self):
        return "Auto"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, cilindrada):
        super().__init__(marca, modelo, velocidad_maxima)
        self.__cilindrada = cilindrada

    def atributos(self):
        super().atributos()
        print(f"· Cilindrada: {self.__cilindrada} cc")

    def tipo_vehiculo(self):
        return "Moto"


# Polimorfismo: Uso de diferentes métodos según el tipo de objeto
def mostrar_tipo(vehiculo):
    print(f"Este vehículo es un {vehiculo.tipo_vehiculo()}.")


# Código principal
if __name__ == "__main__":
    # Crear instancias
    auto = Auto("Toyota", "Corolla", 180, 4)
    moto = Moto("Yamaha", "R15", 150, 155)

    # Mostrar atributos y comportamientos
    print("Atributos del Auto:")
    auto.atributos()
    print("\nAtributos de la Moto:")
    moto.atributos()

    # Demostrando el polimorfismo
    print("\nDemostrando el polimorfismo:")
    mostrar_tipo(auto)
    mostrar_tipo(moto)

    # Acciones
    print("\nAcciones:")
    auto.acelerar(50)
    auto.frenar(20)
    moto.acelerar(70)
    moto.frenar(30)
