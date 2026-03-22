import random
import pickle
from faker import Faker
from modelos.produto import Produto
from modelos.pagamento import Pagamento

class GerenciadorDados:
    def __init__(self):
        self.arquivo = "sistema_cantina.pkl"
        self.fake = Faker('pt_BR')

    def salvar_tudo(self, estoque, pagamentos):
        """Salva o dicionario contendo as duas listas encadeadas."""
        dados = {
            'estoque': estoque,
            'pagamentos': pagamentos
        }
        try:
            with open(self.arquivo, 'wb') as f:
                pickle.dump(dados, f)
            print("Dados salvos com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")

    def carregar_tudo(self):
        """Carrega o dicionario do arquivo pkl."""
        try:
            with open(self.arquivo, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return None
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
            return None

    def gerar_dados_iniciais(self, lista_estoque, lista_pagamentos):
        """Gera massa de dados com margem de 30% para teste."""
        
        # Lista de itens padrao para a cantina
        itens_base = [
            {'nome': 'Coca-Cola', 'min': 4.0, 'max': 6.0},
            {'nome': 'Coxinha', 'min': 3.5, 'max': 5.0},
            {'nome': 'Trident', 'min': 2.0, 'max': 3.0},
            {'nome': 'Suco Natural', 'min': 4.5, 'max': 7.0},
            {'nome': 'Pao de Queijo', 'min': 3.0, 'max': 4.5}
        ]
        
        # Gerando os produtos com a margem de 30%
        for item in itens_base:
            p_custo = round(random.uniform(item['min'], item['max']), 2)
            # Aplicando margem de 30% (venda = custo * 1.3)
            p_venda = round(p_custo * 1.30, 2)
            
            novo_p = Produto(
                item['nome'], 
                p_custo, 
                p_venda, 
                "12/2026", 
                "22/03/2026", 
                20 # Quantidade inicial padrao
            )
            lista_estoque.inserir_no_final(novo_p)
        
        # Gerando alguns pagamentos aleatorios para o Caixa
        categorias = ['Aluno', 'Servidor', 'Professor']
        cursos = ['IA', 'ESG']
        
        for _ in range(5):
            # Simulando vendas passadas com valores aleatorios
            valor_venda = round(random.uniform(5.0, 15.0), 2)
            novo_pix = Pagamento(
                self.fake.name(), 
                random.choice(categorias), 
                random.choice(cursos), 
                valor_venda
            )
            lista_pagamentos.inserir_no_final(novo_pix)