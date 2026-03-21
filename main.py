import sys
import os

# Ajuste para garantir que o Python encontre as pastas no Mac
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from structures.lista_encadeada import ListaEncadeada
from cantinadados import GerenciadorDados
from modelos.produto import Produto

def mostrar_menu():
    print("\n" + "="*35)
    print("      🛒 CANTINA FATEC 2026")
    print("="*35)
    print("1. Ver Estoque Completo")
    print("2. Adicionar Produto Manualmente")
    print("3. Gerar +5 Itens Aleatórios")
    print("0. Sair e Salvar")
    print("="*35)
    return input("Escolha uma opção: ")

def sistema_principal():
    gerenciador = GerenciadorDados()
    
    # Tenta carregar a lista existente
    estoque = gerenciador.carregar_estoque()
    
    # Se for a primeira vez, cria do zero
    if estoque is None:
        estoque = ListaEncadeada()
        gerenciador.gerar_dados_aleatorios(estoque, 5)
        gerenciador.salvar_estoque(estoque)

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            print("\n--- LISTAGEM DE ESTOQUE ---")
            estoque.exibir_estoque()
            input("\nAperte Enter para voltar ao menu...")

        elif opcao == "2":
            print("\n--- CADASTRO DE PRODUTO ---")
            nome = input("Nome do item: ")
            p_venda = float(input("Preço de venda: R$ "))
            qtd = int(input("Quantidade: "))
            
            # Criando o objeto e inserindo na lista encadeada
            novo = Produto(nome, p_venda/2, p_venda, "21/03", "30/03", qtd)
            estoque.inserir_no_final(novo)
            print(f"✅ {nome} adicionado com sucesso!")

        elif opcao == "3":
            gerenciador.gerar_dados_aleatorios(estoque, 5)
            print("🎲 Mais 5 itens adicionados!")

        elif opcao == "0":
            gerenciador.salvar_estoque(estoque)
            print("💾 Dados salvos. Saindo... tchau!")
            break
        else:
            print("❌ Opção inválida, tente novamente.")

if __name__ == "__main__":
    sistema_principal()