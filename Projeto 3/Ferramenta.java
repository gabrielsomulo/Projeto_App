package loja;

/**
 * Ferramentas: martelo, furadeira, serra. Regra propria: tem garantia em
 * meses, e (diferente de MaterialBasico) nao tem desconto por quantidade.
 */
public class Ferramenta extends Produto {

    private int mesesGarantia;

    public Ferramenta(String codigo, String nome, double preco, int quantidadeEstoque, int mesesGarantia) {
        super(codigo, nome, preco, quantidadeEstoque);
        this.mesesGarantia = mesesGarantia;
    }

    public int getMesesGarantia() {
        return mesesGarantia;
    }

    @Override
    public double calcularPrecoFinal(int quantidade) {
        /*
         * TODO: total = getPreco() * quantidade. Sem desconto por
         * quantidade aqui — repare que essa regra e diferente da de
         * MaterialBasico, mesmo com a mesma assinatura de metodo.
         */
        return 0;
    }

    @Override
    public String exibirDetalhes() {
        /*
         * TODO: monte e retorne uma String com nome, codigo, preco,
         * quantidade em estoque, E os meses de garantia (mesesGarantia).
         */
        return "";
    }
}
