# Desafio: Sistema de Cadastro (CRUD) com Flask + PostgreSQL
#
# A interface (rotas, formulários, validação básica, hashing da senha)
# já está pronta. O desafio está em database.py: lá você implementa a
# conexão com o PostgreSQL e as funções de CRUD marcadas com TODO.
#
# Como rodar: veja README.md

import os

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash

import database

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "chave-temporaria-trocar-no-env")


@app.route("/")
def index():
    usuarios = database.listar_usuarios()
    return render_template("index.html", usuarios=usuarios)


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form.get("nome", "").strip()
    email = request.form.get("email", "").strip().lower()
    senha = request.form.get("senha", "")

    if not nome or not email or not senha:
        flash("Preencha nome, email e senha.")
        return redirect(url_for("index"))

    if len(senha) < 6:
        flash("A senha precisa ter pelo menos 6 caracteres.")
        return redirect(url_for("index"))

    if database.email_ja_cadastrado(email):
        flash("Esse email já está cadastrado.")
        return redirect(url_for("index"))

    # A senha em texto puro nunca é salva — só o hash sai desta função.
    senha_hash = generate_password_hash(senha)
    database.inserir_usuario(nome, email, senha_hash)

    flash("Usuário cadastrado com sucesso.")
    return redirect(url_for("index"))


@app.route("/editar/<int:usuario_id>")
def editar(usuario_id):
    usuario = database.buscar_usuario_por_id(usuario_id)
    if usuario is None:
        flash("Usuário não encontrado.")
        return redirect(url_for("index"))
    return render_template("editar.html", usuario=usuario)


@app.route("/editar/<int:usuario_id>", methods=["POST"])
def salvar_edicao(usuario_id):
    nome = request.form.get("nome", "").strip()
    email = request.form.get("email", "").strip().lower()

    if not nome or not email:
        flash("Nome e email não podem ficar vazios.")
        return redirect(url_for("editar", usuario_id=usuario_id))

    database.atualizar_usuario(usuario_id, nome, email)
    flash("Usuário atualizado com sucesso.")
    return redirect(url_for("index"))


@app.route("/excluir/<int:usuario_id>", methods=["POST"])
def excluir(usuario_id):
    database.deletar_usuario(usuario_id)
    flash("Usuário removido.")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
