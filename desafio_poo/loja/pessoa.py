MaiorIdade = 18

class Pessoa(): # A classe Pessoa tem 3 atributos: "Nome", "idade" e "MaiorIdade". "nome" e "idade" são atributos de instância
    def __init__(self, nome, idade=None): # Enquanto o atributo "MaiorIdade" é um atributo de classe que séra compartilhada por todos os objetos da Pessoa
        self.nome = nome
        self.idade = idade

    def __str__(self): # Aqui diz que se não colocar a idade, retornára o nome.
        if not self.idade:
            return self.nome
        
        return f"{self.nome} e {self.idade} anos"
    
    def isAdult(self): # Chama a função isAdult para verificar se é maior de idade e irá retornar se for maior ou igual a MaiorIdade
        return (self.idade or 0) >= MaiorIdade



    