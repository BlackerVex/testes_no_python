class Aumento():
    def __init__(self):
        self.salario = int(input("Digite o seu salário: "))

    def calculo(self):
        if self.salario <= 1000:
            self.porcentagem = 20
            self.aumento = self.salario * (self.porcentagem / 100)
            self.novo_salario = self.salario + self.aumento

        if self.salario <= 3000 and self.salario > 1000:
            self.porcentagem = 15
            self.aumento = self.salario * (self.porcentagem / 100)
            self.novo_salario = self.salario + self.aumento

        if self.salario <= 8000 and self.salario > 3000:
            self.porcentagem = 10
            self.aumento = self.salario * (self.porcentagem / 100)
            self.novo_salario = self.salario + self.aumento

        else:
            self.porcentagem = 5
            self.aumento = self.salario * (self.porcentagem / 100)
            self.novo_salario = self.salario + self.aumento

    def __str__(self):
        return f"O novo salário é: R${self.novo_salario}\nAumento: {self.aumento}\nporcentagem: {self.porcentagem}"


def main():
    aumento = Aumento()
    aumento.calculo()
    print(aumento)


if __name__ == "__main__":
    main()
