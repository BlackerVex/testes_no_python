# esse comando importa a classe datetime que demonstra a hora e o tempo atual

from datetime import datetime

# Cria nova classe
class Tarefa: # Cria uma nova classe chamada tarefa
    def __init__(self, descricao): # inicia uma nova função, self é o objeto e descricao é um parametro que  mostra a descrição do objeto
        self.descricao = descricao # esse trecho cria o atributo descricao para o objeto (self)
        self.feito = False # esse trecho cria um atributo feito no objeto atual (self) e coloca um valor booleano
        self.criacao = datetime.now() # esse trecho cria um atributo criação para o objeto atual (self) e atribui a ele data e horas atuais

    # Código para gerar representação de String para o Objeto
    def concluir(self): # Cria uma função concluir com o objeto self
        self.feito = True # quando estiver concluido o atributo feito séra True para ser concluido

    def __str__(self): # Transforma o objeto em String
        return self.descricao + (" (Concluído)" if self.feito else "") # retorna o objeto string como concluido se self.feito for True
    
    # Adiciona tarefas dentro de uma tupla
def main():
    casa = []
    casa.append(Tarefa("Passar Roupa"))
    casa.append(Tarefa("Fazer Faxina"))
    casa.append(Tarefa("Fazer Comida"))
    casa.append(Tarefa("Fazer Ioga"))
    # Concluí as tarefa que foi adicionada como concluida
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == "Fazer Comida"]
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == "Fazer Ioga"]

    for tarefa in casa:
        print(f"- {tarefa}")

if __name__ == "__main__":
    main()

