class Tempo():
    def __init__(self):
        self.hora_inicial = 0
        self.hora_final = 0
        self.duracao = 0

    def obter_horas(self):
        self.hora_inicial = int(input("Digite a Hora inicial: "))
        self.hora_final = int(input("Digite a Hora final: "))

    def calculo(self):
        if (self.hora_inicial < self.hora_final):
            self.duracao = self.hora_final - self.hora_inicial
        else:
            self.duracao = (24 - self.hora_inicial) + self.hora_final

    def __str__(self):
        return f"O Jogo Durou {self.duracao} Hora(s)."


def main():
    tempo_de_jogo = Tempo()
    continuar = True

    while continuar:
        tempo_de_jogo.obter_horas()
        tempo_de_jogo.calculo()
        print(tempo_de_jogo)

        resposta = input("Deseja Continuar ? (S/N): ")
        if resposta.lower() != "s":
            continuar = False


if __name__ == "__main__":
    main()
