from .cliente import Cliente # Aqui a classe Cliente está sendo importada do módulo cliente
from .vendedor import Vendedor # Aqui a classe Vendedor está sendo importada do módulo vendedor
from .compra import Compra # Aqui a classe Compra está sendo importada do módulo compra

__all__ = ["Cliente", "Vendedor", "Compra"] # A variavél __all__ é definida como uma lista de strings
# que contém os nomes dos módulos, no caso a lista contém os 3 nomes das classes que foram importados
# isso permite que o usuario importe o pacote de uma maneira mais simples, sem precisar importar cada módulo individualmente.

