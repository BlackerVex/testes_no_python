import random
import time

# Lista de palavras para o jogo da forca
palavras = ["marcos", "joão", "luiz", "fabio"]

# função para escolher palavra aleatória da lista de palavras
def escolher_palavra():
    return random.choice(palavras)
    

# função para exibir a lista de palavras que foram advinhadas corretamente
def exibir_letras_advinhadas(palavra, letras_advinhada):
    for letra in palavra:
        if letra in letras_advinhada:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("\n")

# Função principal do jogo da forca
def jogar_forca():
    palavra = escolher_palavra()
    letras_advinhadas = set()
    tentativas = 6

    
    # Loop principal do jogo
    while tentativas > 0:
        exibir_letras_advinhadas(palavra, letras_advinhadas)
        letra = input("Digite uma letra: ")

        if letra in letras_advinhadas:
            print("Você ja tentou essa letra, tente outra.\n")
        elif letra in palavra:
            letras_advinhadas.add(letra)
            print("Você acertou!!")
        else:
            tentativas -= 1
            print("Você errou, você tem ", tentativas, "tentativas restantes.")
            time.sleep(1)
            if tentativas == 1:
                dica = input("Deseja receber uma dica (s/n)?")
                if dica == "s":
                    print("A dica é 'Nome'..")
                else:
                    print("Tudo bem! Continue jogando")
                
                

        # Verificar se o jogador acertou todas as letras da palavra
        if set(palavra) == letras_advinhadas:
            print("Parabéns Você Ganhou!!!!")
            return
        
    # O jogador perdeu todas as tentativas
    print("Você perdeu, A palavra éra: ", palavra)

# Iniciar jogo da forca
if __name__ == "__main__":
    jogar_forca()
