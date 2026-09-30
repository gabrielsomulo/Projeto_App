# ferramenta.py
#
# Ferramentas: martelo, furadeira, serra. Regra propria: tem garantia em
# meses, e (diferente de MaterialBasico) nao tem desconto por quantidade.

from produto import Produto


class Ferramenta(Produto):

    def __init__(self, codigo, nome, preco, quantidade_estoque, meses_garantia):
        super().__init__(codigo, nome, preco, quantidade_estoque)
        self.meses_garantia = meses_garantia

    def calcular_preco_final(self, quantidade):
        """
        TODO: total = self.preco * quantidade. Sem desconto por
        quantidade aqui - repare que essa regra e diferente da de
        MaterialBasico, mesmo com a mesma assinatura de metodo.
        """
        pass

    def exibir_detalhes(self):
        """
        TODO: monte e retorne uma string com nome, codigo, preco,
        quantidade em estoque, E os meses de garantia.
        """
        pass
