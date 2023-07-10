# Primeira Chance > Segunda Chance and Primeira Chance > Terceira chance
class Dardo():
    def __init__(self):
        self.dado = float(input("Digite a Distância do Primeiro Dado: "))
        self.dado_2 = float(input("Digite a Distância do Segundo Dado: "))
        self.dado_3 = float(input("Digite a Distância do Terceiro Dado: "))

    def calculo(self):
        if (self.dado > self.dado_2 and self.dado > self.dado_3):
            print(f"O Maior Dardo é o Primeiro:{self.dado}")
        elif (self.dado_2 > self.dado and self.dado_2 > self.dado_3):
            print(f"O Maior Dardo é o Segundo:{self.dado_2}")
        else:
            print(f"O Maior Dardo é o Terceiro:{self.dado_3}")
    
def main():
    objDardo = Dardo()
    objDardo.calculo()

if __name__ == "__main__":
    main()
