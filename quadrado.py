"""Descrição do problema:

 Crie a classe Qudrado, com o atributo lado, e os métodos: calcularArea, calcularPerimetro e imprimir.
 O método imprimir deve retornar o valor do lado, o valor da área e do perímetro. Ex: "Lado: 2, Área = 4,
 Perímetro = 8".

 Área = lado* lado
Perímetro = 4 * lado

"""

"""Meus comentários sobre:
Apenas um problema para iniciar no mundo orientado a objeto.

"""

class Quadrado:

    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado * self.lado

    def calcularPerimetro(self):
        return 4 * self.lado

    def imprimir(self):
        return f"Lado: {self.lado}, Área = {self.calcularArea()}, Perímetro = {self.calcularPerimetro()}"


# testes

quadrado = Quadrado(5)

print(quadrado.imprimir())

