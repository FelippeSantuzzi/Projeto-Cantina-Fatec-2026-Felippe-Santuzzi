import pickle
import os
import random
from faker import Faker
from modelos.produto import Produto

class GerenciadorDados:
    def __init__(self, arquivo='estoque.pkl'):
        self.arquivo = arquivo
        self.fake = Faker('pt_BR')

    def gerar_dados_aleatorios(self, lista_encadeada, quantidade=5):
        """Usa uma lista temática e o Faker para completar os detalhes."""
        itens_reais = [
            'Coca-Cola 350ml', 'Salgadinho Torcida', 'Halls Mentol', 
            'Coxinha de Frango', 'Pão de Queijo', 'Suco Del Valle', 
            'Chocolate Bis', 'Pastel de Carne', 'Água Mineral', 'Trident'
        ]

        print(f"🎲 Gerando {quantidade} produtos reais da Cantina...")
        
        for _ in range(quantidade):
            nome = random.choice(itens_reais) 
            p_compra = round(random.uniform(2.0, 5.0), 2)
            p_venda = round(p_compra * 1.8, 2)
            
            # Faker gerando as datas no formato brasileiro
            data_c = self.fake.date_between(start_date='-10d', end_date='today').strftime('%d/%m/%Y')
            data_v = self.fake.date_between(start_date='today', end_date='+30d').strftime('%d/%m/%Y')
            qtd = random.randint(10, 100)
            
            novo_p = Produto(nome, p_compra, p_venda, data_c, data_v, qtd)
            lista_encadeada.inserir_no_final(novo_p)

    def salvar_estoque(self, lista_encadeada):
        """Salva a estrutura da lista usando Pickle."""
        with open(self.arquivo, 'wb') as f:
            pickle.dump(lista_encadeada, f)
        print("💾 Estoque salvo com sucesso (Pickle)!")

    def carregar_estoque(self):
        """Carrega a lista do arquivo se ele existir."""
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'rb') as f:
                print("📂 Carregando dados existentes via Pickle...")
                return pickle.load(f) # <--- Certifique-se que é LOAD aqui
        return None