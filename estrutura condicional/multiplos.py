class Multiplos():
    def __init__(self):
        self.numero = int(input("Digite o Primeiro Número: "))
        self.numero2 = int(input("Digite o Segundo Número: "))
    
    def calculo(self):
        if self.numero % self.numero2 == 0 or self.numero2 % self.numero == 0:
            print("Os dois são Múltiplos!")
        else:
            print("Os dois números não são Multiplos!!!")
    
def main():
    multi = Multiplos()
    multi.calculo()

if __name__ == "__main__":
    main()