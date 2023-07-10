import random

palavras = ["banana", "laranja", "maça"]

def escolher_palavra():
    return random.choice(palavras)

def exibir_letras_advinhadas(palavra, letra_advinhada):
    for letra in palavra:
        if letra in letra_advinhada:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("\n")

def jogar_forca():
    palavra = escolher_palavra()
    letras_advinhadas = set()
    tentativas = 6


    while tentativas > 0:
        exibir_letras_advinhadas(palavra, letras_advinhadas)
        dica = print("Fruta")
        letra = input("Digite uma letra: ")

        if letra in letras_advinhadas:
           print("Você ja usou essa letra, tente outra.\n")
        elif letra in palavra:
            letras_advinhadas.add(letra)
            print("Você acertou uma letra!")
        else:
            tentativas -= 1
            print("Você errou, Você tem ", tentativas, " Tentativas restantes.")

        
        if set(palavra) == letras_advinhadas:
            print("Parabéns Você Ganhou!!!!!!!")
            print("A palavra éra", palavra)
            return

    print("Você perdeu a palavra éra", palavra)
    return

if __name__ == "__main__":
    jogar_forca()