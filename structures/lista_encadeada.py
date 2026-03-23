class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.__inicio = None

    def get_inicio(self):
        return self.__inicio

    def inserir_no_final(self, dado):
        novo_nodo = Nodo(dado)
        if self.__inicio is None:
            self.__inicio = novo_nodo
            return
        atual = self.__inicio
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_nodo

    def exibir_lista(self):
        atual = self.__inicio
        if atual is None:
            print("\n📭 Estoque vazio.")
            return
        
        print(f"\n{'PRODUTO':<18} | {'CUSTO':<12} | {'VENDA':<12} | {'QTD'}")
        print("-" * 60)
        while atual:
            print(atual.dado) # Aqui ele chama o __str__ que editamos acima
            atual = atual.proximo
        print("-" * 60)

    def realizar_baixa_estoque(self, nome_produto):
        atual = self.__inicio
        while atual:
            if atual.dado.get_nome().lower() == nome_produto.lower():
                qtd_atual = atual.dado.get_quantidade()
                if qtd_atual > 0:
                    nova_qtd = qtd_atual - 1
                    atual.dado.set_quantidade(nova_qtd)
                    # Alerta visual no console durante a venda
                    if nova_qtd <= 3:
                        print(f"\n⚠️  ALERTA: Estoque baixo de {atual.dado.get_nome()} ({nova_qtd} restantes)")
                    return atual.dado.get_preco_venda()
                return "SEM_ESTOQUE"
            atual = atual.proximo
        return "NAO_ENCONTRADO"

    def obter_relatorio_reposicao(self, limite=3):
        produtos_criticos = []
        atual = self.__inicio
        while atual:
            if atual.dado.get_quantidade() <= limite:
                produtos_criticos.append({
                    'nome': atual.dado.get_nome(),
                    'qtd': atual.dado.get_quantidade()
                })
            atual = atual.proximo
        return produtos_criticos