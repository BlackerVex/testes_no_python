def soma_n(a, b, c):
    return a + b + c

if __name__ == "__main__":
    lista = [1, 2, 3]
    resultado = soma_n(*lista)
    print(resultado)


def dados_pessoais(nome, estado, idade):
    print(f"Nome: {nome}")
    print(f"Estado: {estado}")
    print(f"Idade: {idade}")

if __name__ == "__main__":
    dados = { "nome": "Maria", 
             "estado": "São paulo", 
             "idade": 39
            }
    dados_pessoais(**dados)
              





