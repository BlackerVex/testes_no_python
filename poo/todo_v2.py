from datetime import datetime

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))
    
    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]
    
    def __str__(self):
        return f"{self.nome} ({len(self.pendentes())}) Tarefas Pendente(s)"
    
class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (" (Concluído)"if self.feito else "")

def main():
       casa = Projeto("Tarefas de Casa")
       casa.add("Lavar os Pratos")
       casa.add("Dar o rabo")
       print(casa)


       mercado = Projeto("Lista de Compras")
       mercado.add("Frutas mamiferas")
       mercado.add("Sacolandia")
       print(mercado)

       casa.procurar("Lavar os Pratos").concluir()
       for tarefa in casa.tarefas:
           print(f"- {tarefa}")

       mercado.procurar("Sacolandia").concluir()
       for tarefa in mercado.tarefas:
           print(f"- {tarefa}")
        

if __name__ == "__main__":
    main()