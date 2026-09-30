# produto.py
#
# Classe base abstrata de todos os produtos da loja.
#
# Encapsulamento: os atributos ficam guardados com um underscore na
# frente (_nome, _preco, _quantidade_estoque) - convenção Python para
# "isso é privado, não mexa direto por fora da classe". O acesso de
# fora acontece só pelas @property (getters) e pelos métodos de
# escrita (setters), que é onde você vai validar os valores.
#
# Polimorfismo: usamos o módulo abc (Abstract Base Classes) para
# tornar isso formal, do mesmo jeito que o "abstract" do Java - se uma
# subclasse não implementar calcular_preco_final ou exibir_detalhes,
# o Python nem deixa instanciar essa subclasse. Tente rodar
# Produto("X", "Y", 1, 1) direto e vai ver: "Can't instantiate
# abstract class Produto..."

from abc import ABC, abstractmethod


class Produto(ABC):

    def __init__(self, codigo, nome, preco, quantidade_estoque):
        self._codigo = codigo
        self.nome = nome  # passa pelo setter (property.setter) abaixo
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    @property
    def codigo(self):
        return self._codigo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        """
        TODO: valide que 'valor' (depois de um .strip()) não seja vazio
        antes de guardar em self._nome. Se for inválido, lance
        raise ValueError("mensagem clara aqui").
        """
        pass

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        """
        TODO: valide que 'valor' seja maior que zero antes de guardar
        em self._preco. Se for inválido, lance ValueError.
        """
        pass

    @property
    def quantidade_estoque(self):
        return self._quantidade_estoque

    @quantidade_estoque.setter
    def quantidade_estoque(self, valor):
        """
        TODO: valide que 'valor' não seja negativo antes de guardar em
        self._quantidade_estoque. Se for inválido, lance ValueError.
        """
        pass

    @abstractmethod
    def calcular_preco_final(self, quantidade):
        """
        TODO (o coração do polimorfismo): calcula o preço final para uma
        dada quantidade. Cada subclasse implementa a regra dela (desconto
        por volume, sem desconto, preço por litro...). Por ser abstrato,
        o Python obriga cada subclasse concreta a implementar isso.
        """
        raise NotImplementedError

    @abstractmethod
    def exibir_detalhes(self):
        """
        TODO (polimorfismo também): monta uma string com a descrição do
        produto, incluindo os dados específicos de cada subtipo além
        dos comuns (nome, código, preço, quantidade).
        """
        raise NotImplementedError
