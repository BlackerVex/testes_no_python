from datetime import datetime
from loja import Cliente, Vendedor, Compra

def main():
    juracy = Cliente("Mateus Arruda", 18) # Cria uma instância chamada juracy 
    leo = Vendedor("Leonardo Leitão", 38, 3200) # Cria uma instância chamada leo
    compra1 = Compra(leo, datetime.now(), 512) # cria uma instância de compra feita no momento atual
    compra2 = Compra(leo, datetime(2018, 6, 4), 256) # cria outra instância de compra feita em 04/06/2018
    juracy.registrar_compra(compra1) # registra a compra1
    juracy.registrar_compra(compra2) # registra a compra2

    print(f"Cliente: {juracy}, '(adulto)'" if juracy.isAdult() else "") # mostra o nome e a idade do cliente se for maior de idade caso contrario mostra ""
    print(f"Vendedor: {leo}") # printa nome e idade do vendedor
    print(f"Total: {juracy.total_compras()}R$ em {len(juracy.compras)} compras") # printa o total de compras do juracy e mostra a quantidade de compras
    print(f"Ùltima compra: {juracy.get_data_ultima_compra()}") # mostra a data da ultima compra feita

if __name__ == "__main__":
    main()