package loja;

/**
 * Materiais vendidos a granel/por unidade simples: cimento, areia, tijolo.
 * Regra de negocio propria: desconto por quantidade grande.
 */
public class MaterialBasico extends Produto {

    private static final int QUANTIDADE_MINIMA_DESCONTO = 50;
    private static final double PERCENTUAL_DESCONTO = 0.05;

    private String unidadeMedida; // ex: "saco", "unidade", "m3"

    public MaterialBasico(String codigo, String nome, double preco, int quantidadeEstoque, String unidadeMedida) {
        super(codigo, nome, preco, quantidadeEstoque);
        this.unidadeMedida = unidadeMedida;
    }

    public String getUnidadeMedida() {
        return unidadeMedida;
    }

    @Override
    public double calcularPrecoFinal(int quantidade) {
        /*
         * TODO: total = getPreco() * quantidade.
         * Se quantidade >= QUANTIDADE_MINIMA_DESCONTO, aplique
         * PERCENTUAL_DESCONTO de desconto sobre esse total antes de
         * retornar (ex.: total - total * PERCENTUAL_DESCONTO).
         */
        return 0;
    }

    @Override
    public String exibirDetalhes() {
        /*
         * TODO: monte e retorne uma String com nome, codigo, preco por
         * unidadeMedida e quantidade em estoque. Use getNome(), getCodigo(),
         * getPreco(), getQuantidadeEstoque() e unidadeMedida.
         */
        return "";
    }
}
