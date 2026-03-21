class ListaPagamentos:
    def __init__(self):
        # O início da lista é privado (Encapsulamento)
        self.__inicio = None

    def inserir_no_final(self, novo_pagamento):
        """Lógica FIFO: Adiciona o novo pagamento sempre ao fim da corrente."""
        if self.__inicio is None:
            self.__inicio = novo_pagamento
        else:
            atual = self.__inicio
            
            while atual.get_proximo() is not None:
                atual = atual.get_proximo()
            
            # O último nó agora aponta para o novo integrante
            atual.set_proximo(novo_pagamento)

    def listar_pagamentos(self):
        """Percorre a lista do início ao fim imprimindo cada nó."""
        print("\n--- 💸 RELATÓRIO DE PAGAMENTOS (PIX) ---")
        atual = self.__inicio
        
        if not atual:
            print("📭 Nenhuma transação registrada até o momento.")
            return

        while atual:
            # Aqui o Python chama automaticamente o __str__ que criamos no modelo
            print(atual) 
            atual = atual.get_proximo()
        print("-" * 50)

    def get_inicio(self):
        """Getter para permitir que o sistema de salvamento acesse a lista."""
        return self.__inicio