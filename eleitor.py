"""Descrição do problema:
    Desenvolver uma classe chamada Eleitor com os atributos: nome, idade e os métodos conforme a representação gráfica
    abaixo

    #obs: como não é possível colocar um png no meio do código para mostrar a representação, gráfica vou apenas pôr em
    caracteres o diagrama de classe do problema.

                                                    Eleitor
                                        - nome: String
                                        - idade: int

                                        + Eleitor(nome: String, idade: int)
                                        + verificar(): String

    O método verifircar retorna à situação do eleitor conforme a sua idade, seguindo as regras:
     - Idade menor que 16 anos: "<nome do eleitor> ainda não pode votar. Tem apenas <idade>";
     - Idade igual ou superior a 18 anos e menor ou igual a 65 anos: "<nome do eleitor> - <idade> deve votar.";
     - Idade entre 16 e 18 anos e superior a 65 anos: "<nome do eleitor> - <idade> Voto facultativo.";


    Os atributos devem ser privados e criar métodos getter e setter, e acessá-los via propriedade.
"""


"""Meus comentários do problema:
   Apenas um problema para iniciar no mundo orientado a objeto, mas usa os tão famosos getters e setters, são uma boa
   prática de programação. Também pede atributos privados, neste contexto que usa dados pessoais de alguem é útil para
   deixar o código mais seguro de alterações externas.
"""


class Eleitor:

    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    def verificar(self) -> str:
        if self.__idade < 16:
            return f"{self.__nome} ainda não pode votar. Tem apenas {self.__idade}."
        elif self.__idade >= 18 and self.__idade <= 65:
            return f"{self.__nome} - {self.__idade} deve votar."
        elif self.__idade >= 16 and self.__idade <= 18 or self.__idade > 65:
            return f"{self.__nome} - {self.__idade} Voto facultativo."


# testes
eleitor1 = Eleitor('yuri', 12)
print(eleitor1.verificar())

eleitor2 = Eleitor('yuri', 76)
print(eleitor2.verificar())

eleitor3 = Eleitor('yuri', 20)
print(eleitor3.verificar())
