# material_basico.py
#
# Materiais vendidos a granel/por unidade simples: cimento, areia, tijolo.
# Regra de negocio propria: desconto por quantidade grande.

from produto import Produto

QUANTIDADE_MINIMA_DESCONTO = 50
PERCENTUAL_DESCONTO = 0.05


class MaterialBasico(Produto):

    def __init__(self, codigo, nome, preco, quantidade_estoque, unidade_medida):
        super().__init__(codigo, nome, preco, quantidade_estoque)
        self.unidade_medida = unidade_medida  # ex: "saco", "unidade", "m3"

    def calcular_preco_final(self, quantidade):
        """
        TODO: total = self.preco * quantidade.
        Se quantidade >= QUANTIDADE_MINIMA_DESCONTO, aplique
        PERCENTUAL_DESCONTO de desconto sobre esse total antes de
        retornar (ex.: total - total * PERCENTUAL_DESCONTO).
        """
        pass

    def exibir_detalhes(self):
        """
        TODO: monte e retorne uma string com nome, codigo, preco por
        unidade_medida e quantidade em estoque.
        """
        pass
