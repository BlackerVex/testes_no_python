class Teste():
    def __init__(self):
        self.x = 0
        self.soma = 0

    def obter_numeros(self):
        self.x = int(input("Digite o Primeiro Número: "))
        
    def calculo(self):
        while self.x != 0:
            self.soma = self.x + self.soma
            self.x = int(input("Digite outro Número: "))
        
    def __str__(self):
        return f"Soma = {self.soma}"

def main():
    t1 = Teste()
    continuar = True
    while (continuar != "N"):
        t1.obter_numeros()
        t1.calculo()
        print(t1)
        continuar = input("Deseja Continuar ? (S/N): ")

if __name__ == "__main__":
    main()