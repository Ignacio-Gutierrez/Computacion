class Persona:
    def __init__(self, nombre, dni, pais):
        self.nombre = nombre
        self.dni = dni
        self.pais = pais

class Alumno (Persona):
    def __init__(self, legajo, nombre, dni, pais):
        super().__init__(nombre, dni, pais)
        self.legajo = legajo

class Pais:
    def __init__(self, nombre):
        self.nombre = nombre


arg = Pais('argentina')
pepe = Alumno(1234, 'Pepe','30433210', arg)
print(pepe.nombre)
print(pepe.pais.nombre)