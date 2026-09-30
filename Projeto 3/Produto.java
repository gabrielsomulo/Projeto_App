package loja;

/**
 * Classe abstrata que representa qualquer produto vendido na loja.
 *
 * Encapsulamento: todos os atributos sao privados. O acesso de fora so
 * acontece pelos getters, e a alteracao so pelos setters — que sao onde
 * voce vai colocar as validacoes (nada de preco negativo, nome vazio, etc).
 *
 * Polimorfismo: calcularPrecoFinal() e exibirDetalhes() sao abstratos —
 * o Java OBRIGA cada subclasse concreta (MaterialBasico, Ferramenta,
 * Tinta) a implementar do seu proprio jeito. Quem usa um Produto (a
 * classe Estoque, por exemplo) nao precisa saber qual subtipo e qual —
 * so chama produto.calcularPrecoFinal(...) e cada objeto responde do
 * seu jeito.
 */
public abstract class Produto {

    private String codigo;
    private String nome;
    private double preco;
    private int quantidadeEstoque;

    public Produto(String codigo, String nome, double preco, int quantidadeEstoque) {
        this.codigo = codigo;
        setNome(nome);
        setPreco(preco);
        setQuantidadeEstoque(quantidadeEstoque);
    }

    public String getCodigo() {
        return codigo;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        /*
         * TODO: valide que 'nome' nao seja nulo nem vazio (depois de um
         * trim()) antes de atribuir a this.nome. Se for invalido, lance
         * new IllegalArgumentException("mensagem clara aqui").
         */
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        /*
         * TODO: valide que 'preco' seja maior que zero antes de atribuir
         * a this.preco. Se for invalido, lance IllegalArgumentException.
         */
    }

    public int getQuantidadeEstoque() {
        return quantidadeEstoque;
    }

    public void setQuantidadeEstoque(int quantidadeEstoque) {
        /*
         * TODO: valide que 'quantidadeEstoque' nao seja negativo antes de
         * atribuir a this.quantidadeEstoque. Se for invalido, lance
         * IllegalArgumentException.
         */
    }

    /**
     * TODO (o coracao do polimorfismo): calcula o preco final para uma
     * dada quantidade. Cada subclasse implementa a regra dela (desconto
     * por volume, taxa de garantia, preco por litro...).
     */
    public abstract double calcularPrecoFinal(int quantidade);

    /**
     * TODO (polimorfismo tambem): monta uma descricao textual do produto,
     * incluindo os dados especificos de cada subtipo alem dos comuns
     * (nome, codigo, preco, quantidade).
     */
    public abstract String exibirDetalhes();
}
