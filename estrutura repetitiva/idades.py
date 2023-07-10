class Idades():
    def __init__(self):
        self.contador = 0
        self.media = 0
        self.soma = 0
        self.idade = 0

    def obter_numeros(self):
        while True:
            try:
                self.idade = int(input("Digite a sua Idade: "))
                break
            except ValueError:
                print("Entrada Inválida, Tente Botar Números Inteiros!")
        
    def calculo(self):
        while self.idade >= 0:
            self.soma += self.idade
            self.contador = self.contador + 1
            try:
                self.idade = int(input())
            except ValueError:
                print("Entrada Inválida, Tente Botar Números Inteiros!")
        if self.contador > 0:
            self.media = self.soma / self.contador
            print(f"MEDIA: {self.media:.2f}")
        else:
            print("IMPOSSIVEL DE CALCULAR!!")


def main():
    idades = Idades()
    idades.obter_numeros()
    idades.calculo()


if __name__ == "__main__":
    main()
