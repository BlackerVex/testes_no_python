class Crescente():
    def __init__(self):
        self.x = 0
        self.y = 0

    def obter_numeros(self):
        self.x = int(input("Digite dois números: "))
        self.y = int(input())

    def calculo(self):
        while self.x != self.y:
            if self.x < self.y:
                print("Crescente!")
            else:
                print("Decrescente!")
            self.x = int(input("Digite outros dois números: "))
            self.y = int(input())
    
    def __str__(self):
        return f"São iguais"


def main():
    c1 = Crescente()
    c1.obter_numeros()
    c1.calculo()
    print(c1)


if __name__ == "__main__":
    main()
