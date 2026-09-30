# estoque.py
#
# Gerencia a colecao de produtos da loja. E aqui que a comunicacao entre
# classes acontece: Estoque nunca sabe se um Produto e um MaterialBasico,
# uma Ferramenta ou uma Tinta - ele so guarda referencias a objetos
# Produto e chama os metodos abstratos, confiando que cada objeto sabe
# se comportar do seu proprio jeito (polimorfismo).


class Estoque:

    def __init__(self):
        self._produtos = []

    def adicionar_produto(self, produto):
        """
        TODO: adicione 'produto' na lista self._produtos.
        """
        pass

    def remover_produto(self, codigo):
        """
        TODO: encontre o produto com esse codigo em self._produtos e
        remova da lista. Retorne True se removeu, False se nao achou
        nenhum produto com esse codigo.
        """
        pass

    def buscar_por_codigo(self, codigo):
        """
        TODO: percorra self._produtos e retorne o que tiver esse
        codigo (produto.codigo == codigo), ou None se nao achar.
        """
        pass

    def listar_todos(self):
        """
        TODO: retorne a lista de produtos (pode retornar self._produtos
        diretamente, ou list(self._produtos) para proteger a lista
        interna de alteracoes externas).
        """
        pass

    def calcular_valor_total_estoque(self):
        """
        TODO (o ponto central do desafio de polimorfismo): percorra
        self._produtos e some produto.calcular_preco_final(produto.quantidade_estoque)
        de cada um. Repare que voce chama o MESMO metodo em objetos de
        tipos concretos diferentes (MaterialBasico, Ferramenta, Tinta)
        sem nenhum "if isinstance(produto, ...)" - cada um calcula do
        seu proprio jeito porque implementou calcular_preco_final() a
        sua maneira. Isso E polimorfismo em acao.
        """
        pass
