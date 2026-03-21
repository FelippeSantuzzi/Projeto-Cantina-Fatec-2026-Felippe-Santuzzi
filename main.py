from structures.lista_encadeada import ListaEncadeada
from structures.lista_pagamentos import ListaPagamentos
from modelos.pagamento import Pagamento
from cantinadados import GerenciadorDados

def mostrar_menu():
    print("\n" + "="*50)
    print("      🏪 SISTEMA GESTÃO CANTINA - FATEC 2026")
    print("="*50)
    print("1. 📦 Visualizar Estoque (FIFO)")
    print("2. 💸 Relatório de Pagamentos PIX")
    print("3. ➕ Registrar Novo Pagamento")
    print("4. 🎲 Gerar Massa de Dados (Teste)")
    print("0. 💾 Sair e Salvar Sistema")
    print("="*50)
    return input("Selecione uma opção: ")

def sistema_principal():
    # Inicializa o gerenciador de arquivos
    gerenciador = GerenciadorDados()
    
    # Tenta carregar o "pacote" completo de dados
    dados = gerenciador.carregar_tudo()

    if dados:
        print("📂 Sistema recuperado do arquivo com sucesso!")
        estoque = dados['estoque']
        pagamentos = dados['pagamentos']
    else:
        print("✨ Iniciando sistema vazio...")
        estoque = ListaEncadeada()
        pagamentos = ListaPagamentos()

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            estoque.exibir_estoque()
        
        elif opcao == "2":
            pagamentos.listar_pagamentos()
        
        elif opcao == "3":
            print("\n--- NOVO PAGAMENTO PIX ---")
            nome = input("Nome do pagador: ")
            print("Categorias: Aluno | Servidor | Professor")
            cat = input("Categoria: ")
            print("Cursos: IA | ESG")
            cur = input("Curso: ")
            try:
                val = float(input("Valor Pago: R$ "))
                
                # Cria o objeto Pagamento (Encapsulado)
                novo_pix = Pagamento(nome, cat, cur, val)
                # Insere na Estrutura de Dados (Lista Encadeada)
                pagamentos.inserir_no_final(novo_pix)
                print("✅ Pagamento registrado com sucesso!")
            except ValueError:
                print("❌ Erro: Digite um valor numérico válido para o preço.")

        elif opcao == "4":
            # Passamos ambas as listas para o gerador
            gerenciador.gerar_dados_iniciais(estoque, pagamentos)
            print("🎲 Dados de estoque e pagamentos gerados para teste!")

        elif opcao == "0":
            # Salva o dicionário com as duas listas
            gerenciador.salvar_tudo(estoque, pagamentos)
            print("👋 Saindo... Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    sistema_principal()