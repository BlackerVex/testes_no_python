import random
import string

def gerador_senha(comprimento, caracteres):
    senha = ""
    for i in range(comprimento):
        senha += random.choice(caracteres)
    return senha

comprimento = int(input("Digite o comprimento da senha: "))

print("Quais caracteres você deseja escolhar para a sua senha? ")
print("1 - Apenas letras")
print("2 - Apenas Números")
print("3 - Letras e Números")
print("4 - Letras, Números e Simbolos")

opcao = int(input("Digite a sua opção:\n"))

if opcao == 1:
    caracteres = string.ascii_letters
elif opcao == 2:
    caracteres = string.digits
elif opcao == 3:
    caracteres = string.ascii_letters + string.digits
elif opcao == 4:
    caracteres = string.ascii_letters + string.digits + string.punctuation
else:
    print("Opção inválida")

senha = gerador_senha(comprimento, caracteres)
print("Senha gerada:", senha)

if __name__ == "__main__":
    gerador_senha(comprimento, caracteres)