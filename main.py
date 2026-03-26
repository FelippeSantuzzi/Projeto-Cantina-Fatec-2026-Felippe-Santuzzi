import os
from structures.lista_encadeada import ListaEncadeada
from cantinadados import GerenciadorDados
from modelos.pagamento import Pagamento
from modelos.produto import Produto # Garanta que a classe Produto está importada

def exibir_diario_contabil(estoque, pagamentos):
    """Calcula e exibe o resumo financeiro em tempo real."""
    print("\n" + "="*55)
    print("       📊 DIÁRIO CONTÁBIL - GESTÃO FINANCEIRA")
    print("="*55)
    
    total_caixa = 0
    atual_pag = pagamentos.get_inicio()
    while atual_pag:
        total_caixa += atual_pag.dado.get_valor()
        atual_pag = atual_pag.proximo
    
    total_investido_custo = 0
    total_esperado_venda = 0
    atual_prod = estoque.get_inicio()
    while atual_prod:
        qtd = atual_prod.dado.get_quantidade()
        total_investido_custo += (atual_prod.dado.get_preco_custo() * qtd)
        total_esperado_venda += (atual_prod.dado.get_preco_venda() * qtd)
        atual_prod = atual_prod.proximo
        
    lucro_potencial = total_esperado_venda - total_investido_custo

    print(f"💰 DINHEIRO EM CAIXA (PIX):      R$ {total_caixa:>8.2f}")
    print(f"💸 INVESTIMENTO EM PRODUTOS:     R$ {total_investido_custo:>8.2f}")
    print(f"📦 VALOR DE REVENDA DO ESTOQUE:  R$ {total_esperado_venda:>8.2f}")
    print("-" * 55)
    print(f"📈 LUCRO BRUTO PREVISTO:         R$ {lucro_potencial:>8.2f}")
    print(f"💎 PATRIMÔNIO ATUAL (CAIXA+EST): R$ {total_caixa + total_investido_custo:>8.2f}")
    print("=" * 55)

def main():
    estoque = ListaEncadeada()
    pagamentos = ListaEncadeada()
    gerenciador = GerenciadorDados()

    dados = gerenciador.carregar_tudo()
    if dados:
        estoque = dados['estoque']
        pagamentos = dados['pagamentos']

    while True:
        print("\n" + "—"*50)
        print("      SISTEMA GESTÃO CANTINA - FATEC 2026")
        print("—"*50)
        print("1. Visualizar Estoque (Custo, Venda e Validade)") # Texto atualizado
        print("2. Histórico de Vendas (Pagamentos PIX)")
        print("3. Registrar Nova Venda")
        print("4. Diário Contábil (Lucro e Patrimônio)")
        print("5. Gerar/Resetar Massa de Dados (Qtd Inicial: 4)")
        print("6. Relatório de Reposição (Estoque Crítico)")
        print("7. Cadastrar Produto Manualmente") # Sugestão de nova opção para testar a Validade
        print("0. Sair e Salvar")
        print("—"*50)
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\n" + "—"*10 + " ESTOQUE ATUAL (COM VALIDADE E ENTRADA) " + "—"*10)
            # Este método vai chamar o __str__ de cada Produto automaticamente
            estoque.exibir_lista() 
            input("\nPressione Enter para continuar...")

        elif opcao == "2":
            print("\n" + "—"*15 + " HISTÓRICO DE PAGAMENTOS " + "—"*15)
            pagamentos.exibir_lista()
            input("\nPressione Enter para continuar...")

        elif opcao == "3":
            print("\n--- REGISTRAR VENDA ---")
            nome_p = input("Nome do produto: ")
            resultado = estoque.realizar_baixa_estoque(nome_p)
            
            if isinstance(resultado, float):
                print(f"✅ Produto encontrado! Valor: R$ {resultado:.2f}")
                cliente = input("Nome do Cliente: ")
                categoria = input("Categoria (Aluno/Professor/Servidor): ")
                curso = input("Curso (IA/ESG/Nenhum): ")
                
                novo_pg = Pagamento(cliente, categoria, curso, resultado)
                pagamentos.inserir_no_final(novo_pg)
                print(f"\n✨ Venda registrada com sucesso!")
            elif resultado == "SEM_ESTOQUE":
                print("❌ Erro: Este produto está esgotado!")
            else:
                print("❌ Erro: Produto não cadastrado.")

        elif opcao == "4":
            exibir_diario_contabil(estoque, pagamentos)
            input("\nPressione Enter para continuar...")

        elif opcao == "5":
            print("\n⚠️ Isso apagará os dados atuais.")
            confirmar = input("Confirmar reset e gerar novos dados? (s/n): ")
            if confirmar.lower() == 's':
                estoque = ListaEncadeada()
                pagamentos = ListaEncadeada()
                # O GerenciadorDados deve estar atualizado para criar Produtos com Validade
                gerenciador.gerar_dados_iniciais(estoque, pagamentos)
                gerenciador.salvar_tudo(estoque, pagamentos)
                print("\n✅ Sistema reiniciado com 4 unidades por produto.")

        elif opcao == "6":
            print("\n" + "!"*15 + " RELATÓRIO DE COMPRAS " + "!"*15)
            criticos = estoque.obter_relatorio_reposicao(limite=3)
            if not criticos:
                print("\n✅ Estoque saudável! Nenhum item crítico.")
            else:
                print(f"\n{'PRODUTO':<20} | {'QTD':<5} | {'STATUS'}")
                print("-" * 40)
                for item in criticos:
                    print(f"{item['nome']:<20} | {item['qtd']:<5} | [⚠️ REPOR]")
            input("\nPressione Enter para continuar...")

        elif opcao == "7": # OPÇÃO PARA TESTAR O "ESCURINHO"
            print("\n--- CADASTRAR NOVO PRODUTO ---")
            n = input("Nome: ")
            c = float(input("Preço Custo: "))
            v = float(input("Preço Venda: "))
            val = input("Validade (DD/MM/AA): ")
            ent = input("Entrada (DD/MM/AA): ")
            q = int(input("Quantidade: "))
            
            novo = Produto(n, c, v, val, ent, q)
            estoque.inserir_no_final(novo)
            print("✅ Produto cadastrado com sucesso!")

        elif opcao == "0":
            gerenciador.salvar_tudo(estoque, pagamentos)
            print("\n💾 Dados salvos. Saindo...")
            break
        else:
            print("\n🚫 Opção inválida!")

if __name__ == "__main__":
    main()