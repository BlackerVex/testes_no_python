class Quadrante():
    def __init__(self):
        self.x = 0
        self.y = 0

    def obter(self):
        try:
            self.x = int(input("Digite os Valores da Coordenadas X e Y: "))
            self.y = int(input())
        except ValueError:
            print("Error ao Ler Coordenadas, Tente apenas Com Números!!")

    def calculo(self):
        while (self.x != 0 or self.y == 0) and (self.x == 0 or self.y != 0):
            if (self.x > 0 and self.y > 0):
                print("Quadrante Q1")
            elif (self.x < 0 and self.y > 0):
                print("Quadrante Q2")
            elif (self.x < 0 and self.y < 0):
                print("Quadrante Q3")
            elif (self.x > 0 and self.y < 0):
                print("Quadrante Q4")
            else:
                print("")
            try:
                self.x = int(input("Digite os Valores da Coordenadas X e Y: "))
                self.y = int(input())
            except ValueError:
                print("Error ao Ler Coordenadas, Tente apenas Com Números!!")

    def __str__(self):
        if self.x == 0 or self.y == 0:
            return f"Coordenada x:{self.x} y:{self.y}, encontrado número nulo."


def main():
    quadrante = Quadrante()
    quadrante.obter()
    quadrante.calculo()
    print(quadrante)


if __name__ == "__main__":
    main()
