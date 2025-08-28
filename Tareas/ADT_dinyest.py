"""
Implementación de un ADT Automóvil
con estructuras Estáticas y Dinámicas
"""


class Automovil:
    """Clase que representa un automóvil."""

    def __init__(self, placa, marca, modelo, anio):
        self._placa = placa
        self._marca = marca
        self._modelo = modelo
        self._anio = anio

    # Getters
    def get_placa(self):
        return self._placa

    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_anio(self):
        return self._anio

    # Setters
    def set_placa(self, placa):
        self._placa = placa

    def set_marca(self, marca):
        self._marca = marca

    def set_modelo(self, modelo):
        self._modelo = modelo

    def set_anio(self, anio):
        self._anio = anio

    def __str__(self):
        return f"{self._placa} - {self._marca} {self._modelo} ({self._anio})"


class GarageEstatico:
    """Garage con estructura de datos estática (arreglo fijo)."""

    def __init__(self, capacidad):
        self._capacidad = capacidad
        self._arr = [None] * capacidad
        self._n = 0

    def agregar(self, auto: Automovil):
        if self._n >= self._capacidad:
            raise OverflowError("Capacidad máxima alcanzada")
        self._arr[self._n] = auto
        self._n += 1

    def buscar(self, placa):
        for i in range(self._n):
            if self._arr[i].get_placa() == placa:
                return self._arr[i]
        return None

    def eliminar(self, placa):
        for i in range(self._n):
            if self._arr[i].get_placa() == placa:
                # Desplazar a la izquierda
                for j in range(i, self._n - 1):
                    self._arr[j] = self._arr[j + 1]
                self._arr[self._n - 1] = None
                self._n -= 1
                return True
        return False

    def tam(self):
        return self._n

    def listar(self):
        return [self._arr[i] for i in range(self._n)]
    

class Nodo:
    """Nodo para la lista enlazada de automóviles."""

    def __init__(self, auto: Automovil, siguiente=None):
        self.auto = auto
        self.siguiente = siguiente


class GarageDinamico:
    """Garage con estructura dinámica (lista enlazada)."""

    def __init__(self):
        self._cabeza = None
        self._n = 0

    def agregar(self, auto: Automovil):
        nodo = Nodo(auto, self._cabeza)
        self._cabeza = nodo
        self._n += 1

    def buscar(self, placa):
        actual = self._cabeza
        while actual:
            if actual.auto.get_placa() == placa:
                return actual.auto
            actual = actual.siguiente
        return None

    def eliminar(self, placa):
        anterior, actual = None, self._cabeza
        while actual:
            if actual.auto.get_placa() == placa:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self._cabeza = actual.siguiente
                self._n -= 1
                return True
            anterior, actual = actual, actual.siguiente
        return False

    def tam(self):
        return self._n

    def listar(self):
        resultado, actual = [], self._cabeza
        while actual:
            resultado.append(actual.auto)
            actual = actual.siguiente
        return resultado


if __name__ == "__main__":
    # Crear autos
    auto1 = Automovil("ABC-123", "Toyota", "Corolla", 2020)
    auto2 = Automovil("DEF-456", "Honda", "Civic", 2022)
    auto3 = Automovil("GHI-789", "Ford", "Focus", 2019)

    print("=== Garage Estático ===")
    g_est = GarageEstatico(2)
    g_est.agregar(auto1)
    g_est.agregar(auto2)
    print([str(x) for x in g_est.listar()])
    print("Buscar DEF-456:", g_est.buscar("DEF-456"))
    g_est.eliminar("ABC-123")
    print("Tamaño:", g_est.tam())
    print([str(x) for x in g_est.listar()])

    print("\n=== Garage Dinámico ===")
    g_din = GarageDinamico()
    g_din.agregar(auto1)
    g_din.agregar(auto2)
    g_din.agregar(auto3)
    print([str(x) for x in g_din.listar()])
    print("Buscar ABC-123:", g_din.buscar("ABC-123"))
    g_din.eliminar("DEF-456")
    print([str(x) for x in g_din.listar()])

