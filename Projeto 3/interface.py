# interface.py
#
# Interface pronta (Tkinter). Nao faz parte do desafio de POO - o
# desafio esta nas classes do modelo (produto.py e as subclasses,
# estoque.py). Esta tela so monta objetos e chama os metodos do Estoque.

import tkinter as tk
from tkinter import ttk, messagebox

from estoque import Estoque
from material_basico import MaterialBasico
from ferramenta import Ferramenta
from tinta import Tinta


class TelaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Loja MegaConstrucao - Controle de Estoque")
        self.geometry("820x520")

        self.estoque = Estoque()

        self._montar_formulario()
        self._montar_tabela()
        self._montar_rodape()

    def _montar_formulario(self):
        painel = ttk.LabelFrame(self, text="Novo produto")
        painel.pack(fill="x", padx=10, pady=10)

        self.tipo_var = tk.StringVar(value="Material Basico")
        self.campo_codigo = tk.StringVar()
        self.campo_nome = tk.StringVar()
        self.campo_preco = tk.StringVar()
        self.campo_quantidade = tk.StringVar()
        self.campo_extra1 = tk.StringVar()  # unidade OU meses de garantia
        self.campo_extra2 = tk.StringVar()  # rendimento m2 (so Tinta)

        linha1 = ttk.Frame(painel)
        linha1.pack(fill="x", pady=4, padx=6)
        ttk.Label(linha1, text="Tipo:", width=22).pack(side="left")
        combo = ttk.Combobox(
            linha1, textvariable=self.tipo_var,
            values=["Material Basico", "Ferramenta", "Tinta"],
            state="readonly", width=20,
        )
        combo.pack(side="left", padx=(0, 20))
        ttk.Label(linha1, text="Codigo:", width=10).pack(side="left")
        ttk.Entry(linha1, textvariable=self.campo_codigo, width=15).pack(side="left")

        linha2 = ttk.Frame(painel)
        linha2.pack(fill="x", pady=4, padx=6)
        ttk.Label(linha2, text="Nome:", width=22).pack(side="left")
        ttk.Entry(linha2, textvariable=self.campo_nome, width=30).pack(side="left", padx=(0, 20))
        ttk.Label(linha2, text="Preco unitario (R$):", width=18).pack(side="left")
        ttk.Entry(linha2, textvariable=self.campo_preco, width=10).pack(side="left")

        linha3 = ttk.Frame(painel)
        linha3.pack(fill="x", pady=4, padx=6)
        ttk.Label(linha3, text="Quantidade em estoque:", width=22).pack(side="left")
        ttk.Entry(linha3, textvariable=self.campo_quantidade, width=10).pack(side="left", padx=(0, 20))
        ttk.Label(linha3, text="Unidade / Meses garantia:", width=22).pack(side="left")
        ttk.Entry(linha3, textvariable=self.campo_extra1, width=12).pack(side="left")

        linha4 = ttk.Frame(painel)
        linha4.pack(fill="x", pady=4, padx=6)
        ttk.Label(linha4, text="Rendimento m2/litro (so Tinta):", width=28).pack(side="left")
        ttk.Entry(linha4, textvariable=self.campo_extra2, width=10).pack(side="left")

        linha5 = ttk.Frame(painel)
        linha5.pack(fill="x", pady=(8, 4), padx=6)
        ttk.Button(linha5, text="Adicionar produto", command=self._adicionar_produto).pack(side="right")

    def _montar_tabela(self):
        colunas = ("codigo", "tipo", "nome", "preco", "estoque")
        self.tabela = ttk.Treeview(self, columns=colunas, show="headings", height=10)
        for coluna, titulo in zip(colunas, ("Codigo", "Tipo", "Nome", "Preco", "Estoque")):
            self.tabela.heading(coluna, text=titulo)
        self.tabela.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    def _montar_rodape(self):
        painel = ttk.Frame(self)
        painel.pack(fill="x", padx=10, pady=(0, 10))

        ttk.Button(painel, text="Remover selecionado", command=self._remover_selecionado).pack(side="left")
        ttk.Button(painel, text="Ver detalhes do selecionado", command=self._exibir_detalhes_selecionado).pack(side="left", padx=8)
        ttk.Button(painel, text="Calcular valor total do estoque", command=self._calcular_valor_total).pack(side="left")

        self.label_total = ttk.Label(painel, text="Valor total: R$ 0,00", font=("TkDefaultFont", 11, "bold"))
        self.label_total.pack(side="right")

    def _adicionar_produto(self):
        try:
            tipo = self.tipo_var.get()
            codigo = self.campo_codigo.get().strip()
            nome = self.campo_nome.get().strip()
            preco = float(self.campo_preco.get().strip().replace(",", "."))
            quantidade = int(self.campo_quantidade.get().strip())

            if tipo == "Material Basico":
                unidade = self.campo_extra1.get().strip()
                produto = MaterialBasico(codigo, nome, preco, quantidade, unidade)
            elif tipo == "Ferramenta":
                meses = int(self.campo_extra1.get().strip())
                produto = Ferramenta(codigo, nome, preco, quantidade, meses)
            else:
                rendimento = float(self.campo_extra2.get().strip().replace(",", "."))
                produto = Tinta(codigo, nome, preco, quantidade, rendimento)

            self.estoque.adicionar_produto(produto)
            self._atualizar_tabela()
            self._limpar_formulario()

        except ValueError as erro:
            messagebox.showerror(
                "Dado invalido",
                str(erro) if str(erro) else "Confira os campos numericos (preco, quantidade, garantia/rendimento).",
            )

    def _remover_selecionado(self):
        selecionado = self.tabela.selection()
        if not selecionado:
            messagebox.showinfo("Aviso", "Selecione uma linha da tabela primeiro.")
            return
        codigo = self.tabela.item(selecionado[0], "values")[0]
        self.estoque.remover_produto(codigo)
        self._atualizar_tabela()

    def _exibir_detalhes_selecionado(self):
        selecionado = self.tabela.selection()
        if not selecionado:
            messagebox.showinfo("Aviso", "Selecione uma linha da tabela primeiro.")
            return
        codigo = self.tabela.item(selecionado[0], "values")[0]
        produto = self.estoque.buscar_por_codigo(codigo)
        detalhes = produto.exibir_detalhes() if produto else "Produto nao encontrado."
        messagebox.showinfo("Detalhes do produto", detalhes or "(exibir_detalhes ainda nao retorna nada)")

    def _calcular_valor_total(self):
        total = self.estoque.calcular_valor_total_estoque() or 0
        self.label_total.config(text=f"Valor total: R$ {total:.2f}")

    def _atualizar_tabela(self):
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)
        produtos = self.estoque.listar_todos()
        if not produtos:
            return
        for p in produtos:
            tipo = type(p).__name__
            self.tabela.insert("", "end", values=(p.codigo, tipo, p.nome, f"R$ {p.preco:.2f}", p.quantidade_estoque))

    def _limpar_formulario(self):
        self.campo_codigo.set("")
        self.campo_nome.set("")
        self.campo_preco.set("")
        self.campo_quantidade.set("")
        self.campo_extra1.set("")
        self.campo_extra2.set("")
