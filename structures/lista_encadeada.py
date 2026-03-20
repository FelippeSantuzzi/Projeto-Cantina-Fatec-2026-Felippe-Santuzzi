class ListaEncadeada:
    def __init__(self):
        self.head = None  # Onde a lista começa

    def inserir_no_final(self, novo_produto):
        if self.head is None:
            self.head = novo_produto
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_produto

    def exibir_estoque(self):
        atual = self.head
        if not atual:
            print("\n[!] O estoque está vazio.")
            return
        
        print("\n--- RELATÓRIO DE ESTOQUE ATUAL ---")
        while atual:
            print(f"Item: {atual.nome:.<20} | Preço: R${atual.preco_venda:>6.2f} | Qtd: {atual.quantidade:>3}")
            atual = atual.proximo
        print("----------------------------------")