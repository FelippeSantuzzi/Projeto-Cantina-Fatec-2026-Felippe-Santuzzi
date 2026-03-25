# 🍔 Projeto Cantina Fatec 2026

Este projeto consiste em um sistema de gerenciamento para uma cantina universitária, desenvolvido com foco em **Programação Orientada a Objetos (POO)** e persistência de dados eficiente. O software permite o controle de produtos, categorias e a manipulação de dados estruturados para a operação da cantina.

## 🏗️ Estrutura do Projeto

O repositório está organizado de forma modular para garantir a organização do código:

* **`main.py`**: Ponto de entrada da aplicação, onde a lógica principal e a execução do sistema ocorrem.
* **`cantinadados.py`**: Módulo responsável pela lógica de manipulação e armazenamento de dados.
* **`/modelos`**: Contém as definições das classes (ex: `Produto`, `Categoria`), aplicando conceitos de encapsulamento.
* **`/estruturas`**: Armazena as estruturas de dados ou listas que sustentam o funcionamento do inventário.

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Linguagem:** Python 3.
* **Pickle:** Utilizado para a **serialização e desserialização** de objetos Python, permitindo salvar o estado do sistema em arquivos binários de forma persistente.
* **Faker:** Biblioteca empregada para a **geração de dados fictícios** (mock data), facilitando testes de volume e preenchimento automático do sistema com dados realistas.
* **Paradigma:** Orientação a Objetos (Classes, Atributos e Métodos).

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado.
2. Instale a biblioteca Faker:
   ```bash
   pip install faker