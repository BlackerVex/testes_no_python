# glicose <= 100, Normal
# glicose <= 140, Elevado
# glicose > 140, Diabetes

class Glicose():
    def __init__(self):
        self.glicose = float(input("Digite a Medida da sua Glicose: "))
    
    def calculo(self):
        if self.glicose <= 100:
            print("Classificado: Normal")
        if self.glicose <= 140:
            print("Classificado: Elevado")
        else:
            print("Classificado: Diabetes!!")
        return 
    
def main():
    glicose = Glicose()
    glicose.calculo()
    
if __name__ == "__main__":
    main()