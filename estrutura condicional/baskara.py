# bhaskara 
import math

class Calculo():
    def __init__(self):
        pass

    def calcular(self,a, b, c, delta):
        self.a = a
        self.b = b
        self.c = c
        self.delta = delta
        self.raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        self.raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        
    def raiz(self):
        return self.raiz1
    
    def raiz_2(self):
        return self.raiz2

def main():
    a = float(input("Insira o valor de a:"))
    b = float(input("Insira o valor de b:"))
    c = float(input("Insira o valor de c:"))
    delta = pow(b,2) - 4 * a * c
    
    if a == 0 or delta < 0:
        print("Não existe raiz com esses valores")
        return main()
    else:
        calculo = Calculo()
    
    calculo.calcular(a, b, c, delta)
    print("A Raiz do valor delta é: ",calculo.raiz())
    print("A Segunda Raiz do valor delta é: ",calculo.raiz_2())

if __name__ == "__main__":
    main()


        

    
    
            

        