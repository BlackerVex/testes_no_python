from .pessoa import Pessoa
from functools import reduce

class Cliente(Pessoa): # cria uma subclasse da classe Pessoa
    def __init__(self, nome, idade): # Aqui ele adiciona 2 objetos e depois herda esse comportamento da Classe pessoa
        super().__init__(nome, idade) 
        self.compras = [] # Além disso adiciona um atributo compras recebendo uma lista vázia

    def registrar_compra(self, compra): # Adiciona um objeto compra a lista de compras do cliente
        self.compras.append(compra)

    def get_data_ultima_compra(self):
        return None if not self.compras else sorted(self.compras, key=lambda compra: compra.data)[-1].data
    # retorna a data da ultima compra realizada pelo cliente. Se o cliente não tiver compras registradas retorna 'None'.
    # o método sorted é usado para ordenar a lista de compras do cliente com base na sua data.
    # utilizando uma função "lambad" que extrai a sua compra.
    # o parâmatro "key" é utilizado para indicar a chave de ordenação, neste caso, a data da compra
    # o resultado da chamada sorted() é uma lista de suas compras na ordem crescente e a expressão [-1] é indicado para pegar o ultimo elemento da lista

    def total_compras(self):
        return reduce (lambda c1, c2: c1 + c2, (compra.valor for compra in self.compras))
    # retorna o valor total das compras realizadas pelo cliente, somando o valor de todas as compras registradas da lista
    # ele chama a função "reduce" para realiza uma operação em dois valores e um iteravel
    # no caso desse método é a função, lambda que soma dois valores c1 e c2, e o iteravel é uma expressão geradora 
    # que gera os atributos "valor" de cada objeto "compra" presente na lista "self.compras"