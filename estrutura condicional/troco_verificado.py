# Preço Unitário
# Quantidade do Produto
# Dinheiro Recebido
# Valor Total
# Troco

class Caixa():
    def __init__(self):
        pass

    def calculo(self, preco_uni, quantidade, dinheiro_rec, valor_total):
        self.preco_unitario = preco_uni
        self.quantidade = quantidade
        self.dinheiro = dinheiro_rec
        self.valor = valor_total

        troco = self.dinheiro - self.valor
        return troco
    
def main():
    caixa = Caixa()
    print("Digite o preço unitário do produto: ")
    preco_uni = float(input())
    print("Digite Quantas Unidades irá levar: ")
    quantidade = float(input())
    print("Digite o Dinheiro Recebido: ")
    dinheiro_rec = float(input())
    valor_total = preco_uni * quantidade
    resultado = caixa.calculo(preco_uni, quantidade, dinheiro_rec, valor_total)
    if resultado > 0 :
        print("O será de R$ {:.2f}".format(resultado))
    else:
        print("Senhor(a) Tem Dinheiro faltando. ")
        return resultado
    
if __name__ == "__main__":
    main()
