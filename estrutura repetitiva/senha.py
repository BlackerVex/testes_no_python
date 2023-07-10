class Senha():
    def __init__(self):
        self.senha = 0
        self.senha_correta = 2002
        self.tentativas = 3

    def obter_senha(self):
        try:
            self.senha = int(input("Digite a Senha: "))
        except ValueError:
            print("A Senha só pode ser digitada por Números, Tente Novamente: ")

    def calculo(self):
        while self.senha != self.senha_correta:
            print("\nSenha Incorreta! Tente Novamente.")
            print(f"{self.tentativas} Tentativas Restantes\n")
            try:
                self.senha = int(input("Digite a Senha: "))
            except ValueError:
                print("A Senha só pode ser digitada por Números, Tente Novamente: ")
                self.tentativas += 1

            self.tentativas -= 1
            if (self.tentativas == 0) and self.senha != self.senha_correta:
                print("Acabou as tentativas!!")
                break

        if self.senha == self.senha_correta:
            print("Senha Correta!!")

    def __str__(self):
        if self.senha != self.senha_correta:
            return f"Tentativas Restantes: {self.tentativas}\n"
        else:
            return "Você Ganhou o Jogo!"


def main():
    senha = Senha()
    senha.obter_senha()
    senha.calculo()
    print(senha)
    return


if __name__ == "__main__":
    main()
