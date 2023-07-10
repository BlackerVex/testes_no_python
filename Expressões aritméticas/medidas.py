# area do quadrado = lado * lado
# area do triangulo = base * altura / 2
# area do trapézio = base maior + base menor * altura / 2

class Calculo():
    def calc_quadrado(self, lado):
        self.lado = lado
        self.area = lado * lado
        return self.area
    
    def calc_triangulo(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = (base * altura) / 2
        return self.area

    def calc_trapezio(self, base_maior, base_menor, altura):
        self.base_maior = base_maior
        self.base_menor = base_menor
        self.altura = altura
        self.area = (base_maior + base_menor) * altura / 2
        return self.area
    
def main():
    lado = input("Digite o lado do Quadrado: ")
    lado = float(lado)
    quadrado = Calculo()
    area = quadrado.calc_quadrado(lado)
    print(f"A area do Quadrado é: {area:.4f}")

    base = input("Digite a medida da Base do Triangulo: ")
    base = float(base)
    altura = input("Digite a medida da Altura do Triangulo: ")
    altura = float(altura)
    triangulo = Calculo()
    area = triangulo.calc_triangulo(base, altura)
    print(f"A area do Triangulo é: {area:.4f}")

    base_maior = input("Digite a Base Maior do Trapézio: ")
    base_maior = float(base_maior)
    base_menor = input("Digite a Base Menor do Trapézio: ")
    base_menor = float(base_menor)
    altura = input("Digite a altura do Trapézio: ")
    altura = float(altura)
    trapezio = Calculo()
    area = trapezio.calc_trapezio(base_maior, base_menor, altura)
    print(f"A area do Trapezio é: {area:.4f}")
    

if __name__ == "__main__":
    main()


