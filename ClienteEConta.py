"""Crie as classes Conta e Cliente conforme a crepsentação gráfica. Os atributos devem ser privados e cria métodos
getter e setter e acessá-los via propriedades .

    # diagrama de classe:
                                                    Conta
        - numero: String
        - saldo:  double

        +Conta(cliente: Cliente, numero: String, saldo: double)
        +sacar(valor)
        +depositar(valor)
        +resumo(): String

                                                    Cliente

        - nome
        - telefone

        +Cliente(nome: String, telefone: String)

        O saldo  inicial da  conta não pode ser negativo se vier um valor negativo, o seu valor deve ser considerado
        zero;
        O método sacar, recebe o valor do saque como parâmetro, o valor deve ser maior que zero e ter saldo suficente
        para a  conta não ficar negativa. O valor do saque deve ser subtraído do saldo da conta;
        O método depositar deve receber o valor do deposito e acrescido ao saldo da conta.O valor do deposito não pode
        ser negativo;
        O método resumo, deve retornar um texto com as seguintes informações: nome do cliente, número da conta e o valor
        do saldo. Ex: "Cliente: João da Silva - Conta: 12345-6 - Saldo: R$ 502,00.

        Desafio extra:
        Crie um método responsável por exibir um extrato da conta (extrato). Você deve ciar a estrutura para armazenar
        as operações realizadas sobre a conta. O método extrado deve mostrar os dados do cliente, conta e todas as
        operações de Saque e Deposito que foram realizadas sobre a conta. Exemplo do extrato:

        Cliente: João da Silva
        Número da Conta: 12345-6
        Saldo inicial: R$560,00
        Saque: R$200,00
        Saque: R$100,00
        Deposito: R$500,00

        Saldo atual: 760,00
"""

"""Meus comentários sobre o problema:

Uma classe que se aproxima mais do cotidiano de um programador, por mais que tenha bastante detalhes, a grande sacada
deste desafio é que se precisa usar a herança, e como não existe o tipo double no python, irei usar o tipo float. O
problema não pede, mas decidi mostrar no extrato a data e o horário  das operações para melhor detalhamento das info-
rmações. 
"""
from datetime import datetime


class Cliente:
    def __init__(self, nome: str, tefelone: str):
        self.__nome = nome
        self.__telefone = tefelone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone


class Conta(Cliente):

    def __init__(self, numero: str, saldo: float, nome: str, tefelone: str):
        super().__init__(nome, tefelone)
        self.__numero = numero
        self.__extrato = []
        if saldo < 0:
            self.__saldo = 0
        else:
            self.__saldo = saldo
        self.__extrato.append(f'Saldo inicial: {self.__saldo}')

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, novoSaldo):
        self.__saldo = novoSaldo

    def sacar(self, valorSaque):
        if valorSaque > 0 and self.__saldo - valorSaque > 0:
            self.__extrato.append(f'Saque: {valorSaque} no horário: {datetime.utcnow()}')
            self.saldo -= valorSaque
            return 'Saque realizado.'
        else:
            raise ValueError('Não é possível sacar este valor!')

    def depositar(self, valorDeposito):
        if valorDeposito > 0:
            self.__extrato.append(f'Deposito: {valorDeposito} no horário: {datetime.utcnow()}')
            self.saldo += valorDeposito
            return 'Deposito realizado.'
        else:
            raise ValueError('Não é possível depositar este valor!')

    def resumo(self):
        return f"Cliente: {self.nome} - Conta: {self.numero} - Saldo: R${self.saldo}"

    def extrato(self):
        return f'{self.resumo()[:14]}, Número da Conta: {self.resumo()[24:29]}', \
               tuple(self.__extrato), f'Saldo atual: {self.saldo}'


# testes
teste = Conta('123321', 13.00, 'yuri', '104')
print()
print(teste.depositar(20))
print(teste.sacar(21))
print(teste.extrato())
