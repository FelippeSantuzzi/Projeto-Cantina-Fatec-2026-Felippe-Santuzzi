class Produto:
    def __init__(self, nome, preco_custo, preco_venda, validade, data_entrada, quantidade):
        self.__nome = nome
        self.__preco_custo = preco_custo
        self.__preco_venda = preco_venda
        self.__validade = validade
        self.__data_entrada = data_entrada
        self.__quantidade = quantidade

    # Getters necessários para o sistema
    def get_nome(self): return self.__nome
    def get_preco_custo(self): return self.__preco_custo
    def get_preco_venda(self): return self.__preco_venda
    def get_validade(self): return self.__validade        # <-- ADICIONADO
    def get_data_entrada(self): return self.__data_entrada  # <-- ADICIONADO
    def get_quantidade(self): return self.__quantidade
    def set_quantidade(self, nova_qtd): self.__quantidade = nova_qtd

    def __str__(self):
        # Atualizado para exibir Validade e Data de Entrada no menu
        return (f"📦 {self.__nome:<15} | "
                f"Venda: R$ {self.__preco_venda:>6.2f} | "
                f"Validade: {self.__validade} | "
                f"Entrada: {self.__data_entrada} | "
                f"Qtd: {self.__quantidade:>3}")