# segundos <- (valor % 3600) % 60
# minutos <- (valor % 3600) / 60
# horas <-  valor / 3600

class Calculo():
    def conversao(self, valor):
        segundos = valor % 60
        minutos = (valor % 3600) // 60
        horas = valor // 3600
        return f"{horas:02d}: {minutos:02d}: {segundos:02d}"
    
    def __str__(self):
        return f"{self.segundos} segundos, {self.minutos} minutos e {self.horas} horas"
    
    
def main():
    valor = int(input("Digite a duração em segundos: "))
    calculo = Calculo()
    print(calculo.conversao(valor))

if __name__ == "__main__":
    main()