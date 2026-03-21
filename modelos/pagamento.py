import datetime

class Pagamento:
    def __init__(self, pagador, categoria, curso, valor):
        # Atributos PRIVADOS (Encapsulamento)
        self.__pagador = pagador
        self.__categoria = categoria  # Aluno, Servidor ou Professor
        self.__curso = curso          # IA ou ESG
        self.__valor = valor
        self.__data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.__proximo = None         # Ponteiro para o próximo nó

    # --- MÉTODO DE EXIBIÇÃO (Formatação dos dados) ---
    def __str__(self):
        return (f"👤 {self.__pagador.ljust(15)} | "
                f"🏷️ {self.__categoria.ljust(10)} | "
                f"🎓 {self.__curso.ljust(5)} | "
                f"💰 R$ {str(self.__valor).ljust(7)} | "
                f"🕒 {self.__data_hora}")

    # --- GETTERS (Acesso seguro aos dados) ---
    def get_pagador(self): return self.__pagador
    def get_categoria(self): return self.__categoria
    def get_curso(self): return self.__curso
    def get_valor(self): return self.__valor
    def get_data_hora(self): return self.__data_hora
    def get_proximo(self): return self.__proximo

    # --- SETTERS (Alteração segura) ---
    def set_proximo(self, proximo):
        self.__proximo = proximo