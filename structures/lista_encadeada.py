class ListaEncadeada:
    def __init__(self):
        self.__inicio = None

    def inserir_no_final(self, novo_produto):
        if self.__inicio is None:
            self.__inicio = novo_produto
        else:
            atual = self.__inicio
            while atual.get_proximo() is not None:
                atual = atual.get_proximo()
            atual.set_proximo(novo_produto)

    def realizar_baixa_estoque(self, nome_produto):
        """
        Busca o produto pelo nome. Se encontrar e houver saldo, 
        diminui 1 unidade e retorna o valor de venda.
        """
        atual = self.__inicio
        
        while atual is not None:
            # Comparacao em minusculo para evitar erros de digitacao
            if atual.get_nome().lower() == nome_produto.lower():
                if atual.get_quantidade() > 0:
                    nova_qtd = atual.get_quantidade() - 1
                    atual.set_quantidade(nova_qtd)
                    return atual.get_preco_venda()
                else:
                    return "SEM_ESTOQUE"
            atual = atual.get_proximo()
            
        return "NAO_ENCONTRADO"

    def exibir_estoque(self):
        print("\n--- RELATORIO DE ESTOQUE ATUAL ---")
        atual = self.__inicio
        if not atual:
            print("Estoque vazio.")
            return
        
        while atual:
            print(atual)
            atual = atual.get_proximo()
        print("----------------------------------")

    def get_inicio(self):
        return self.__inicio