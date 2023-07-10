class Combustivel():
    def __init__(self):
        self.alcool = 0
        self.gasolina = 0
        self.diesel = 0
        self.codigo = 0
    
    def calculo(self):
        while self.codigo != 4:
            try:
                self.codigo = int(
                    input("Informe um codigo (1, 2, 3) ou 4 para parar: "))
            except ValueError:
                print("Código incorreto, Digite apenas Números. ")
            if self.codigo == 1:
                self.alcool = self.alcool + 1
                print(f"\nAlcool: {self.alcool}")
                print(f"Gasolina: {self.gasolina}")
                print(f"Diesel: {self.diesel}")
            elif self.codigo == 2:
                self.gasolina = self.gasolina + 1
                print(f"\nAlcool: {self.alcool}")
                print(f"Gasolina: {self.gasolina}")
                print(f"Diesel: {self.diesel}\n")
            elif self.codigo == 3:
                self.diesel = self.diesel + 1
                print(f"\nAlcool: {self.alcool}")
                print(f"Gasolina: {self.gasolina}")
                print(f"Diesel: {self.diesel}\n")
            else:
                if self.codigo != 4:
                    print("Código inválido, Tente Novamente.")

    def __str__(self):
        return "Muito Obrigado, Volte Sempre."


def main():
    try:
        resposta = input("Deseja abastecer o Tanque ? (S/N): ")
    except ValueError:
        print("Apenas Responda com S para 'Sim' ou N para 'Não'.")
    if resposta.lower() == "s":
        print("\nDigite 1 para Àlcool.")
        print("Digite 2 para Gasolina.")
        print("Digite 3 Para Diesel.\n")
        tanque = Combustivel()
        tanque.calculo()
        print(tanque)
    else:
        print("Tchau, Volte Sempre!")


if __name__ == "__main__":
    main()
