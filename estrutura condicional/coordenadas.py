# Q1 = positivo(x), positivo(y)
# Q2 = negativo(x), positivo(y)
# Q3 = negativo(x), negativo(y)
# Q4 = positivo(x), negativo(y)
# nulo = zero(x), zero(y)

class Coordenada():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.resultado = 0

    def obter_valores(self):
        self.x = float(input("Digite o Valor de x: "))
        self.y = float(input("Digite o valor de y: "))

    def calculo(self):
        if (self.x > 0 and self.y > 0):
            self.resultado = "Q1"

        elif (self.x < 0 and self.y > 0):
            self.resultado = "Q2"

        elif (self.x < 0 and self.y < 0):
            self.resultado = "Q3"

        elif (self.x > 0 and self.y < 0):
            self.resultado = "Q4"

        else:
            self.resultado = "Origem"
    
    def __str__(self):
        return f"{self.resultado}"


def main():
    coordenadas = Coordenada()
    continuar = True

    while continuar:
        coordenadas.obter_valores()
        coordenadas.calculo()
        print(coordenadas)

        resposta = input("Deseja Continuar á procurar Coordenadas ? (S/N) ")
        if resposta.lower() != "s":
            continuar = False


if __name__ == "__main__":
    main()
