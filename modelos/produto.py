class Produto:
    def __init__(self, nome, preco_custo, preco_venda, validade, data_entrada, quantidade):
        # Atributos PRIVADOS (Encapsulamento)
        self.__nome = nome
        self.__preco_custo = preco_custo
        self.__preco_venda = preco_venda
        self.__validade = validade
        self.__data_entrada = data_entrada
        self.__quantidade = quantidade
        self.__proximo = None

    # --- GETTERS (Acesso seguro aos dados) ---
    def get_nome(self):
        return self.__nome

    def get_preco_venda(self):
        return self.__preco_venda

    def get_quantidade(self):
        return self.__quantidade

    def get_proximo(self):
        return self.__proximo

    # --- SETTERS (Alteração segura) ---
    def set_quantidade(self, nova_qtd):
        if nova_qtd >= 0:
            self.__quantidade = nova_qtd

    def set_proximo(self, proximo):
        self.__proximo = proximo

    # --- MÉTODO DE EXIBIÇÃO ---
    def __str__(self):
        return (f"Produto: {self.__nome.ljust(15)} | "
                f"Qtd: {str(self.__quantidade).ljust(4)} | "
                f"Preco Venda: R$ {str(self.__preco_venda).ljust(7)}")