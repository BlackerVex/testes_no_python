from .pessoa import Pessoa

class Vendedor(Pessoa): # cria uma subclasse "Vendedor" da classe "Pessoa"
    def __init__(self, nome, idade, salario): # adiciona os atributos "nome", "idade" e "salario"
        super().__init__(nome, idade) # adiciona 2 objeto e herda esse comportamento da classe "Pessoa"
        self.salario = salario # inicialização de atributo de instância, o valor do parâmetro salario esta sendo atributo no atributo instância self.salario
        