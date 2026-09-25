# database.py
#
# Aqui vive o desafio de verdade: conectar no PostgreSQL e implementar
# as operações de CRUD com segurança (queries parametrizadas, nunca
# concatenando dados do usuário direto na string SQL).
#
# As variáveis de conexão já são lidas do .env (nunca hardcode senha
# de banco no código-fonte). Complete as funções marcadas com TODO.

import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def obter_conexao():
    """
    TODO: crie e retorne uma conexão psycopg2 com o PostgreSQL usando as
    variáveis DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD carregadas
    do .env.

    Dica:
        return psycopg2.connect(
            host=DB_HOST, port=DB_PORT, dbname=DB_NAME,
            user=DB_USER, password=DB_PASSWORD,
        )
    """
    pass


def inserir_usuario(nome, email, senha_hash):
    """
    TODO: insira um novo usuário na tabela 'usuarios'.

    Regras de segurança:
    - Use uma query parametrizada com %s — NUNCA use f-string, .format()
      ou concatenação para colocar 'nome'/'email' direto na string SQL
      (isso abre brecha para SQL Injection).
    - Abra a conexão com obter_conexao(), execute o INSERT, faça
      connection.commit() e feche cursor e conexão (de preferência com
      'with' ou try/finally, para garantir o fechamento mesmo se der erro).
    """
    pass


def listar_usuarios():
    """
    TODO: retorne uma lista de tuplas/dicionários com (id, nome, email)
    de todos os usuários cadastrados, ordenados por id.

    Importante: NUNCA inclua 'senha_hash' no retorno desta função — ela
    alimenta o template HTML, e a senha (nem o hash) deve aparecer na tela.
    """
    pass


def buscar_usuario_por_id(usuario_id):
    """
    TODO: retorne um único usuário (id, nome, email) pelo id informado,
    ou None se não existir nenhum usuário com esse id.
    """
    pass


def atualizar_usuario(usuario_id, nome, email):
    """
    TODO: atualize nome e email do usuário com o id informado, usando
    uma query UPDATE parametrizada (mesma regra de segurança do INSERT).
    """
    pass


def deletar_usuario(usuario_id):
    """
    TODO: remova da tabela o usuário com o id informado.
    """
    pass


def email_ja_cadastrado(email):
    """
    TODO: retorne True se já existir um usuário com esse email, False
    caso contrário. Usada em app.py para não deixar cadastrar duas
    contas com o mesmo email.
    """
    pass
