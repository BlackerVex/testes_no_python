class Dardo2():
    def __init__(self):
        self.maior_dardo = 0

    def calculo(self, dado, dado_2, dado_3):
        self.dado = dado
        self.dado_2 = dado_2
        self.dado_3 = dado_3
        self.maior_dardo = max(dado, dado_2, dado_3)

    def __str__(self):
        return f"O Maior Dardo é: {self.maior_dardo}"

def main():
    dado = float(input("Digite o Primeiro Dardo: "))
    dado_2 = float(input("Digite o Segundo Dardo: "))
    dado_3 = float(input("Digite o Terceiro Dardo: "))
    obgDardo = Dardo2()
    obgDardo.calculo(dado, dado_2, dado_3)
    print(obgDardo)


if __name__ == "__main__":
    main()
