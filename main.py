from structures.lista_encadeada import ListaEncadeada
from structures.lista_pagamentos import ListaPagamentos
from modelos.pagamento import Pagamento
from cantinadados import GerenciadorDados

def exibir_diario_contabil(estoque, pagamentos):
    """
    Calcula o saldo das contas Caixa e Estoque percorrendo as listas encadeadas.
    """
    print("\n--- DIARIO CONTABIL (ADMINISTRACAO ATLETICA) ---")
    
    # 1. Calculo do Caixa (Soma de todos os pagamentos realizados)
    total_caixa = 0.0
    atual_pag = pagamentos.get_inicio()
    while atual_pag is not None:
        total_caixa += atual_pag.get_valor()
        atual_pag = atual_pag.get_proximo()
        
    # 2. Calculo do Valor em Estoque (Patrimonio parado)
    valor_total_estoque = 0.0
    atual_prod = estoque.get_inicio()
    while atual_prod is not None:
        valor_total_estoque += (atual_prod.get_preco_venda() * atual_prod.get_quantidade())
        atual_prod = atual_prod.get_proximo()
        
    print(f"CONTA CAIXA (Entradas PIX):    R$ {total_caixa:.2f}")
    print(f"CONTA ESTOQUE (Patrimonio):    R$ {valor_total_estoque:.2f}")
    print(f"VALOR TOTAL DO NEGOCIO:        R$ {(total_caixa + valor_total_estoque):.2f}")
    print("-" * 50)

def mostrar_menu():
    print("\n" + "="*50)
    print("      SISTEMA GESTAO CANTINA - FATEC 2026")
    print("="*50)
    print("1. Visualizar Estoque")
    print("2. Relatorio de Pagamentos PIX")
    print("3. Registrar Venda (Baixa de Estoque + Pagamento)")
    print("4. Diario Contabil (Caixa vs Estoque)")
    print("5. Gerar Massa de Dados (Teste)")
    print("0. Sair e Salvar Sistema")
    print("="*50)
    return input("Selecione uma opcao: ")

def sistema_principal():
    gerenciador = GerenciadorDados()
    dados = gerenciador.carregar_tudo()

    if dados:
        print("Dados recuperados com sucesso.")
        estoque = dados['estoque']
        pagamentos = dados['pagamentos']
    else:
        print("Iniciando novo banco de dados.")
        estoque = ListaEncadeada()
        pagamentos = ListaPagamentos()

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            estoque.exibir_estoque()
        
        elif opcao == "2":
            pagamentos.listar_pagamentos()
        
        elif opcao == "3":
            print("\n--- REGISTRAR VENDA (CONSUMO) ---")
            estoque.exibir_estoque()
            item = input("Digite o nome do produto para venda: ")
            
            # Chama a logica de baixa na estrutura de dados
            resultado = estoque.realizar_baixa_estoque(item)
            
            if resultado == "NAO_ENCONTRADO":
                print("Erro: Produto nao localizado no sistema.")
            elif resultado == "SEM_ESTOQUE":
                print("Erro: Produto com saldo insuficiente em estoque.")
            else:
                # Se encontrou, 'resultado' contem o valor do produto
                print(f"Valor da venda: R$ {resultado}")
                nome_aluno = input("Nome do Aluno: ")
                cat = input("Categoria (Aluno/Servidor/Professor): ")
                curso = input("Curso (IA/ESG): ")
                
                # Cria o lancamento financeiro automaticamente
                novo_pix = Pagamento(nome_aluno, cat, curso, resultado)
                pagamentos.inserir_no_final(novo_pix)
                print("Venda realizada com sucesso e estoque atualizado.")

        elif opcao == "4":
            exibir_diario_contabil(estoque, pagamentos)

        elif opcao == "5":
            gerenciador.gerar_dados_iniciais(estoque, pagamentos)
            print("Massa de dados gerada para testes.")

        elif opcao == "0":
            gerenciador.salvar_tudo(estoque, pagamentos)
            print("Sistema encerrado.")
            break
        else:
            print("Opcao invalida.")

if __name__ == "__main__":
    sistema_principal()