package loja;

import java.util.ArrayList;
import java.util.List;

/**
 * Gerencia a colecao de produtos da loja. E aqui que a comunicacao entre
 * classes acontece: Estoque nunca sabe se um Produto e um MaterialBasico,
 * uma Ferramenta ou uma Tinta — ele so guarda referencias a Produto e
 * chama os metodos abstratos, confiando que cada objeto sabe se comportar
 * do seu proprio jeito (polimorfismo).
 */
public class Estoque {

    private List<Produto> produtos = new ArrayList<>();

    public void adicionarProduto(Produto produto) {
        /*
         * TODO: adicione 'produto' na lista 'produtos'.
         */
    }

    public boolean removerProduto(String codigo) {
        /*
         * TODO: encontre o produto com esse codigo em 'produtos' e
         * remova da lista. Retorne true se removeu, false se nao achou
         * nenhum produto com esse codigo.
         */
        return false;
    }

    public Produto buscarPorCodigo(String codigo) {
        /*
         * TODO: percorra 'produtos' e retorne o que tiver esse codigo
         * (produto.getCodigo().equals(codigo)), ou null se nao achar.
         */
        return null;
    }

    public List<Produto> listarTodos() {
        /*
         * TODO: retorne a lista de produtos (pode retornar 'produtos'
         * diretamente, ou uma copia com new ArrayList<>(produtos) se
         * quiser proteger a lista interna de alteracoes externas).
         */
        return null;
    }

    public double calcularValorTotalEstoque() {
        /*
         * TODO (o ponto central do desafio de polimorfismo): percorra
         * 'produtos' e some produto.calcularPrecoFinal(produto.getQuantidadeEstoque())
         * de cada um. Repare que voce chama o MESMO metodo em objetos de
         * tipos concretos diferentes (MaterialBasico, Ferramenta, Tinta)
         * sem nenhum "if produto instanceof ..." — cada um calcula do seu
         * proprio jeito porque implementou calcularPrecoFinal() a sua
         * maneira. Isso E polimorfismo em acao.
         */
        return 0;
    }
}
