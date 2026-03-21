import pickle
import os
import random
from faker import Faker
from modelos.produto import Produto
from modelos.pagamento import Pagamento

class GerenciadorDados:
    def __init__(self, arquivo='sistema_cantina.pkl'):
        self.arquivo = arquivo
        self.fake = Faker('pt_BR')

    def gerar_dados_iniciais(self, lista_estoque, lista_pagamentos):
        """Gera massa de dados para teste em ambos os módulos."""
        # Produtos
        itens = ['Coca-Cola', 'Coxinha', 'Trident', 'Suco', 'Pão de Queijo']
        for item in itens:
            p_venda = round(random.uniform(5.0, 10.0), 2)
            novo_p = Produto(item, p_venda/2, p_venda, "21/03", "30/03", 50)
            lista_estoque.inserir_no_final(novo_p)
        
        # Pagamentos
        categorias = ['Aluno', 'Servidor', 'Professor']
        cursos = ['IA', 'ESG']
        for _ in range(3):
            pago = Pagamento(self.fake.name(), random.choice(categorias), random.choice(cursos), 15.50)
            lista_pagamentos.inserir_no_final(pago)

    def salvar_tudo(self, lista_estoque, lista_pagamentos):
        """Salva as duas listas encadeadas em um único arquivo."""
        dados = {
            'estoque': lista_estoque,
            'pagamentos': lista_pagamentos
        }
        with open(self.arquivo, 'wb') as f:
            pickle.dump(dados, f)
        print("\n💾 Todo o sistema foi salvo com sucesso!")

    def carregar_tudo(self):
        """Recupera os dados salvos."""
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'rb') as f:
                return pickle.load(f)
        return None