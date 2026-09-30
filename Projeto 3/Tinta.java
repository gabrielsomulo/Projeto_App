package loja;

/**
 * Tintas: vendidas por litro, com um rendimento (quantos m2 um litro cobre).
 */
public class Tinta extends Produto {

    private double rendimentoM2PorLitro;

    public Tinta(String codigo, String nome, double preco, int quantidadeEstoque, double rendimentoM2PorLitro) {
        super(codigo, nome, preco, quantidadeEstoque);
        this.rendimentoM2PorLitro = rendimentoM2PorLitro;
    }

    public double getRendimentoM2PorLitro() {
        return rendimentoM2PorLitro;
    }

    @Override
    public double calcularPrecoFinal(int quantidade) {
        /*
         * TODO: total = getPreco() * quantidade (quantidade em litros).
         */
        return 0;
    }

    @Override
    public String exibirDetalhes() {
        /*
         * TODO: monte e retorne uma String com nome, codigo, preco,
         * quantidade em estoque, E quantos m2 por litro esse produto
         * rende (rendimentoM2PorLitro).
         */
        return "";
    }
}
