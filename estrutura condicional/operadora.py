# R$ 50.00 reais por 100 minutos no telefone
# 2 reais a mais a cada minuto que exerce 100 minutos

class Operadora():
    def __init__(self):
     self.franquia_minutos = 100
     self.valor_plano_basico = 50.00
     self.valor_excedente_minuto = 2.00   

    def calculo(self, minutos_consumidos):
       if minutos_consumidos <= self.franquia_minutos:
          valor_a_pagar = self.valor_plano_basico
       else:
          minutos_excedentes = minutos_consumidos - self.franquia_minutos
          valor_excedente = minutos_excedentes * self.valor_excedente_minuto
          valor_a_pagar = self.valor_plano_basico + valor_excedente
       return valor_a_pagar
    
def main():
   plano = Operadora()
   minutos_consumidos = float(input("Digite os Minutos Consumidos: "))
   valor_a_pagar = plano.calculo(minutos_consumidos)
   print(f"Valor a se pagar R${valor_a_pagar}")

    
if __name__ == "__main__":
    main()



