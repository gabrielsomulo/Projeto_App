# tinta.py
#
# Tintas: vendidas por litro, com um rendimento (quantos m2 um litro cobre).

from produto import Produto


class Tinta(Produto):

    def __init__(self, codigo, nome, preco, quantidade_estoque, rendimento_m2_por_litro):
        super().__init__(codigo, nome, preco, quantidade_estoque)
        self.rendimento_m2_por_litro = rendimento_m2_por_litro

    def calcular_preco_final(self, quantidade):
        """
        TODO: total = self.preco * quantidade (quantidade em litros).
        """
        pass

    def exibir_detalhes(self):
        """
        TODO: monte e retorne uma string com nome, codigo, preco,
        quantidade em estoque, E quantos m2 por litro esse produto rende.
        """
        pass
