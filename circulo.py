"""Descrição do problema:
    Crie a classe Circulo contendo o atributo raio e os métodos calcularArea, calcularPerimetro e imprimir.
    O método imprimir deve retornar o valor do raio, da área e do perímetro, ex: "Raio: 2, Área: 12.57,
    Perímetro: 12.57"

    Área = pi* raio²
    Perímetro = 2*pi*raio

    O pi deve ser pego da biblioteca math.
    Formate o retorno dos valores em duas casas decimais.
"""

"""Meus comentários do problema:
   Apenas um problema para iniciar no mundo orientado a objeto, mas agora começando a mostrar porque este mundo é tão
   pragmáticom, começando a aclopar o código junto de outros.
   
   Formatar a string retornada aqui para ser mostrada é muito útil, na minha visão fica muito menos poluído o resultado,
   existem programas que precisam ser mostradas várias ou todas as casas decimais mas este não é o caso.
"""
import math


class Circulo:

    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        return math.pi * self.raio ** 2

    def calcularPerimetro(self):
        return 2 * math.pi * self.raio

    def imprimir(self):
        return "Raio: {:.2f}, Área: {:.2f}, Perímetro: {:.2f} " \
            .format(self.raio, self.calcularArea(), self.calcularPerimetro())


#teste

circulo = Circulo(2)
print(circulo.imprimir())
