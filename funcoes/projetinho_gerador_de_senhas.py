import random
import string

def gerar_senha(comprimento, caracteres):
    senha = ""
    for i in range(comprimento):
        senha += random.choice(caracteres)
    return senha

comprimento = int(input("Digite o comprimento da senha: "))

print("Quais caracteres você deseja incluir na senha?\n")
print("1 - Apenas letras")
print("2 - Apenas Números")
print("3 - Letras e Números")
print("4 - Letras, números e simbolos")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    caracteres = string.ascii_letters
elif opcao == 2:
    caracteres = string.digits
elif opcao == 3:
    caracteres = string.ascii_letters + string.digits
elif opcao == 4:
    caracteres = string.ascii_letters + string.digits + string.punctuation
else:
    print("Opção Inválida.")

senha = gerar_senha(comprimento, caracteres)
print("Senha gerada: ", senha)

if __name__ == "__main__":
    gerar_senha(comprimento, caracteres)
    