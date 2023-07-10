class Validacao():
    def __init__(self):
        self.media = 0

    def calculo_nota1(self):
        try:
            self.nota1 = float(
                input("Digite a Primeira Nota: "))
        except ValueError:
            print("\nValor inválido, tente novamente com números.")
        while (self.nota1 < 0) or (self.nota1 > 10):
            try:
                self.nota1 = float(
                    input("Valor Inválido, Digite a Nota Corretamente: "))
            except ValueError:
                print("\nValor inválido, tente novamente com números.")
        if (self.nota1 >= 0) and (self.nota1 <= 10):
            print("Nota Arquivada.")

    def calculo_nota2(self):
        try:
            self.nota2 = float(
                input("Digite a Segunda Nota: "))
        except ValueError:
            print("\nValor inválido, tente novamente com números.")

        while (self.nota2 < 0) or (self.nota2 > 10):
            try:
                self.nota2 = float(
                    input("Valor Inválido, Digite a Nota Corretamente: "))
            except ValueError:
                print("\nValor inválido, tente novamente com números.")

        if (self.nota2 >= 0) and (self.nota2 <= 10):
            print("Nota Arquivada.")

    def calculo_media(self):
        self.media = (self.nota1 + self.nota2) / 2

    def __str__(self):
        return f"Media do Aluno: {self.media}"


def main():
    validar = Validacao()
    validar.calculo_nota1()
    validar.calculo_nota2()
    validar.calculo_media()
    print(validar)


if __name__ == "__main__":
    main()
