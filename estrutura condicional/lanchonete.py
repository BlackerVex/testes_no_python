# Código do Produto
# Preço do Produto
# Quantidade
# Valor a pagar

class Lanchonete():
    def __init__(self):
        self.codigo = int(input("Digite o Código do Produto: "))
        self.quantidade = int(input("Digite a Quantidade do Produto: "))
    
    def calculo(self):
        if self.codigo == 1:
              self.produto = 5.00
              return (self.produto * self.quantidade)
        elif self.codigo == 2:
              self.produto = 3.50
              return (self.quantidade * self.produto)
        elif self.codigo == 3:
              self.produto = 4.80
              return (self.quantidade * self.produto)
        elif self.codigo == 4:
              self.produto = 8.90
              return (self.quantidade * self.produto)
        elif self.codigo == 5:
              self.produto = 7.32
              return (self.quantidade * self.produto)
        else:
              print("Código Inválido!!!")

def main():
      l = Lanchonete()
      valor_a_pagar = l.calculo()
      print("Valor a Pagar:", valor_a_pagar, "R$")

if __name__ == "__main__":
      main()
