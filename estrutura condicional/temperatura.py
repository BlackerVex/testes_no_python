
class Temperatura():
    def __init__(self):
        self.escala = input(
            "Você vai digitar a temperatura com qual escala ? (C/F):")

    def Calculo(self):
        if self.escala == "C":
            print("Digite o valor em Celsius: ")
            celsius = float(input())
            fahrenheit = 9/5 * celsius + 32
            return f"A temperatura equivalente em Fahrenheit é: {fahrenheit:.2f}°F"

        elif self.escala == "F":
            print("Digite o Valor em fahrenheit: ")
            fahrenheit = float(input())
            celsius = (fahrenheit - 32) * 5/9
            return f"A temperatura equivalente em fahrenheit é: {celsius:.2f}°C"
        else:
            print("Escalas inválidas, tente novamente!")


def main():
    calculo = Temperatura()
    resultado = calculo.Calculo()
    print(resultado)


if __name__ == "__main__":
    main()
