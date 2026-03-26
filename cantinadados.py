import random # Para geração de preços e valores aleatórios
import pickle # Para salvar e carregar os dados do sistema
from faker import Faker # Para gerar nomes fictícios de clientes
from modelos.produto import Produto # Para criar objetos Produto com atributos como validade e data de entrada
from modelos.pagamento import Pagamento # Para criar objetos Pagamento com atributos como categoria e curso

class GerenciadorDados: # Para gerenciar o salvamento e carregamento dos dados
    def __init__(self): 
        self.arquivo = "sistema_cantina.pkl"
        self.fake = Faker('pt_BR')

    def salvar_tudo(self, estoque, pagamentos): # Salva os dados do estoque e dos pagamentos em um arquivo binário usando pickle. Ele cria um dicionário contendo as duas listas encadeadas e o salva no arquivo especificado. Em caso de erro durante o salvamento, ele captura a exceção e exibe uma mensagem de erro.
        dados = {'estoque': estoque, 'pagamentos': pagamentos}
        try:
            with open(self.arquivo, 'wb') as f: # Abre o arquivo em modo de escrita binária
                pickle.dump(dados, f)
            print("✅ Dados salvos com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar: {e}")

    def carregar_tudo(self):
        try:
            with open(self.arquivo, 'rb') as f:
                return pickle.load(f)
        except:
            return None

    def gerar_dados_iniciais(self, lista_estoque, lista_pagamentos):
        itens_base = [
            {'nome': 'Coca-Cola', 'min': 4.0, 'max': 6.0},
            {'nome': 'Coxinha', 'min': 3.5, 'max': 5.0},
            {'nome': 'Trident', 'min': 2.0, 'max': 3.0},
            {'nome': 'Suco Natural', 'min': 4.5, 'max': 7.0},
            {'nome': 'Pao de Queijo', 'min': 3.0, 'max': 4.5}
        ]
        
        for item in itens_base:
            p_custo = round(random.uniform(item['min'], item['max']), 2)
            p_venda = round(p_custo * 1.30, 2)
            novo_p = Produto(item['nome'], p_custo, p_venda, "12/2026", "22/03/2026", 4)
            lista_estoque.inserir_no_final(novo_p)
        
        categorias = ['Aluno', 'Servidor', 'Professor']
        cursos = ['IA', 'ESG']
        for _ in range(5):
            valor = round(random.uniform(5.0, 15.0), 2)
            novo_pix = Pagamento(self.fake.name(), random.choice(categorias), random.choice(cursos), valor)
            lista_pagamentos.inserir_no_final(novo_pix)