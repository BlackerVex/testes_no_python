# nota1 + nota2 = media, media >= 60 APROVADO 

class Nota():
    def __init__(self, n1, n2, media):
        self.n1 = n1
        self.n2 = n2
        self.media = media
        
    
    def calculo(self):
        if self.media >= 60:
            return 'APROVADO'
        else:
            return 'REPROVADO'

def main():
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    nota_final = n1 + n2
    print(f"NOTA FINAL = {nota_final}")
    media = (n1 + n2)
    n = Nota(n1, n2, media)
    print(n.calculo())

if __name__ == "__main__":
    main()
