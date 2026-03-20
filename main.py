import sys
import os


sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from modelos.produto import Produto
from structures.lista_encadeada import ListaEncadeada

def sistema():
    # Iniciando a estrutura manual
    estoque_fatec = ListaEncadeada()

    # Cadastrando alguns itens para testar
    p1 = Produto("Salgado Assado", 4.50, 9.00, "19/03", "20/03", 25)
    p2 = Produto("Suco Natural", 3.00, 7.50, "19/03", "21/03", 15)
    p3 = Produto("Bolo de Pote", 5.00, 12.00, "19/03", "25/03", 10)

    # Colocando na nossa lista manual
    estoque_fatec.inserir_no_final(p1)
    estoque_fatec.inserir_no_final(p2)
    estoque_fatec.inserir_no_final(p3)

    # Mostrando o resultado no terminal
    estoque_fatec.exibir_estoque()

if __name__ == "__main__":
    sistema()