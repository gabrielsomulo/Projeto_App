# Desafio: Sistema de Cadastro (CRUD) com Flask + PostgreSQL

Requisito da cliente: um sistema simples de cadastro de usuários (nome,
email, senha), rodando localmente, com os dados salvos num banco
PostgreSQL de verdade — nada de simular em memória.

A interface (formulários, rotas, hashing de senha, mensagens de
validação) já está pronta. O desafio está em `database.py`: fazer a
conexão com o PostgreSQL e implementar o CRUD.

## 1. Preparar o ambiente

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Preparar o banco PostgreSQL

Crie um banco local (ajuste o nome se quiser):

```sql
CREATE DATABASE cadastro_db;
```

Depois rode o schema:

```bash
psql -U postgres -d cadastro_db -f schema.sql
```

## 3. Configurar as variáveis de ambiente

Copie o exemplo e preencha com os dados do seu PostgreSQL local:

```bash
cp .env.example .env
```

Edite o `.env` com host, porta, nome do banco, usuário e senha reais.
Esse arquivo nunca deve ir para o git (já está no `.gitignore`).

## 4. Rodar o servidor

```bash
python app.py
```

Acesse **http://localhost:5000** no navegador.

## O desafio: completar `database.py`

Todas as funções abaixo estão como `TODO` — é aí que a conexão e o CRUD
precisam ser implementados:

1. `obter_conexao()` — abrir a conexão com `psycopg2.connect(...)` usando
   as variáveis lidas do `.env`.
2. `inserir_usuario(nome, email, senha_hash)` — INSERT parametrizado.
3. `listar_usuarios()` — SELECT de todos os usuários (sem retornar a senha).
4. `buscar_usuario_por_id(usuario_id)` — SELECT de um usuário específico.
5. `atualizar_usuario(usuario_id, nome, email)` — UPDATE parametrizado.
6. `deletar_usuario(usuario_id)` — DELETE por id.
7. `email_ja_cadastrado(email)` — checagem de duplicidade antes de inserir.

## Boas práticas exigidas (o que será avaliado)

- **Nenhuma query monta SQL com f-string/format/concatenação usando
  dados do usuário.** Sempre `cursor.execute("... WHERE email = %s", (email,))`,
  nunca `f"... WHERE email = '{email}'"` — a segunda forma abre
  brecha para SQL Injection.
- **Senha nunca é salva em texto puro.** `app.py` já chama
  `generate_password_hash()` antes de repassar para `inserir_usuario`
  — a função de banco só deve receber e guardar o hash.
- **Nada de credencial no código-fonte.** Host, porta, nome do banco,
  usuário e senha vêm todos do `.env` via `os.getenv()`.
- **Conexões e cursores fechados corretamente**, mesmo se uma query
  falhar no meio (use `with` ou `try/finally`).
- **`listar_usuarios()` nunca retorna a coluna `senha_hash`** para o
  template — mesmo sendo um hash, não há motivo para ela chegar à
  camada de visualização.

## Como testar se está funcionando

1. Cadastre um usuário pelo formulário da página inicial.
2. Confirme no `psql` que a linha foi criada e que a coluna
   `senha_hash` **não** é a senha em texto puro.
3. Edite o usuário e confirme que nome/email mudaram no banco.
4. Exclua o usuário e confirme que a linha desapareceu.
5. Tente cadastrar dois usuários com o mesmo email — o segundo deve
   ser bloqueado pela mensagem de "email já cadastrado".
