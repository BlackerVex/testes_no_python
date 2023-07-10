# primeiro valor
# segundo valor
# terceiro valor

class Menor_de_tres():
    def __init__(self):
        pass

    def menor(self, primeiro, segundo, terceiro):
        self.primeiro = primeiro
        self.segundo = segundo
        self.terceiro = terceiro
        if primeiro < segundo < terceiro:
            print(f"O Menor valor é o: {primeiro}")
        elif segundo < primeiro < terceiro:
            print(f"O Menor valor é o: {segundo}")
        else:
            print(f"O Menor valor é o: {terceiro}")
    
    def __str__(self):
        return f"de {self.primeiro}, {self.segundo}, {self.terceiro}"
    
def main():
    primeiro = int(input("Digite o Primeiro Valor: "))
    segundo = int(input("Digite o Segundo Valor: "))
    terceiro = int(input("Digite o Terceiro Valor: "))
    menor_de_tres = Menor_de_tres()
    menor_de_tres.menor(primeiro, segundo, terceiro)
    print(menor_de_tres)

if __name__ == "__main__":
    main()
