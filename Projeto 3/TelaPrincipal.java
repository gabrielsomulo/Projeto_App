package loja;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.util.List;

/**
 * Interface pronta (Swing/JFrame). Nao faz parte do desafio de POO —
 * o desafio esta nas classes do modelo (Produto e subclasses, Estoque).
 * Esta tela so monta objetos e chama os metodos do Estoque.
 */
public class TelaPrincipal extends JFrame {

    private final Estoque estoque = new Estoque();

    private JComboBox<String> comboTipo;
    private JTextField campoCodigo;
    private JTextField campoNome;
    private JTextField campoPreco;
    private JTextField campoQuantidade;
    private JTextField campoExtra1; // unidade de medida OU meses de garantia
    private JTextField campoExtra2; // rendimento m2 (so usado por Tinta)
    private DefaultTableModel modeloTabela;
    private JTable tabela;
    private JLabel labelValorTotal;

    public TelaPrincipal() {
        super("Loja MegaConstrucao - Controle de Estoque");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(780, 540);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout(10, 10));

        add(criarPainelFormulario(), BorderLayout.NORTH);
        add(criarPainelTabela(), BorderLayout.CENTER);
        add(criarPainelRodape(), BorderLayout.SOUTH);
    }

    private JPanel criarPainelFormulario() {
        JPanel grade = new JPanel(new GridLayout(3, 4, 8, 8));
        grade.setBorder(BorderFactory.createTitledBorder("Novo produto"));

        comboTipo = new JComboBox<>(new String[]{"Material Basico", "Ferramenta", "Tinta"});
        campoCodigo = new JTextField();
        campoNome = new JTextField();
        campoPreco = new JTextField();
        campoQuantidade = new JTextField();
        campoExtra1 = new JTextField();
        campoExtra2 = new JTextField();

        grade.add(new JLabel("Tipo:"));
        grade.add(comboTipo);
        grade.add(new JLabel("Codigo:"));
        grade.add(campoCodigo);

        grade.add(new JLabel("Nome:"));
        grade.add(campoNome);
        grade.add(new JLabel("Preco unitario (R$):"));
        grade.add(campoPreco);

        grade.add(new JLabel("Quantidade em estoque:"));
        grade.add(campoQuantidade);
        grade.add(new JLabel("Unidade (material) / Meses garantia (ferramenta):"));
        grade.add(campoExtra1);

        JPanel linhaExtra2 = new JPanel(new FlowLayout(FlowLayout.LEFT));
        linhaExtra2.add(new JLabel("Rendimento m2/litro (so Tinta):"));
        linhaExtra2.add(campoExtra2);

        JButton botaoAdicionar = new JButton("Adicionar produto");
        botaoAdicionar.addActionListener(e -> adicionarProduto());

        JPanel linhaBotao = new JPanel(new FlowLayout(FlowLayout.RIGHT));
        linhaBotao.add(botaoAdicionar);

        JPanel painelCompleto = new JPanel();
        painelCompleto.setLayout(new BoxLayout(painelCompleto, BoxLayout.Y_AXIS));
        painelCompleto.add(grade);
        painelCompleto.add(linhaExtra2);
        painelCompleto.add(linhaBotao);

        return painelCompleto;
    }

    private JScrollPane criarPainelTabela() {
        modeloTabela = new DefaultTableModel(new String[]{"Codigo", "Tipo", "Nome", "Preco", "Estoque"}, 0) {
            @Override
            public boolean isCellEditable(int row, int column) {
                return false;
            }
        };
        tabela = new JTable(modeloTabela);
        return new JScrollPane(tabela);
    }

    private JPanel criarPainelRodape() {
        JPanel painel = new JPanel(new BorderLayout());

        JButton botaoRemover = new JButton("Remover selecionado");
        botaoRemover.addActionListener(e -> removerSelecionado());

        JButton botaoDetalhes = new JButton("Ver detalhes do selecionado");
        botaoDetalhes.addActionListener(e -> exibirDetalhesSelecionado());

        JButton botaoCalcular = new JButton("Calcular valor total do estoque");
        botaoCalcular.addActionListener(e -> calcularValorTotal());

        labelValorTotal = new JLabel("Valor total: R$ 0,00");
        labelValorTotal.setFont(labelValorTotal.getFont().deriveFont(Font.BOLD, 14f));

        JPanel painelBotoes = new JPanel(new FlowLayout(FlowLayout.LEFT));
        painelBotoes.add(botaoRemover);
        painelBotoes.add(botaoDetalhes);
        painelBotoes.add(botaoCalcular);

        painel.add(painelBotoes, BorderLayout.WEST);
        painel.add(labelValorTotal, BorderLayout.EAST);
        painel.setBorder(BorderFactory.createEmptyBorder(4, 4, 8, 10));
        return painel;
    }

    private void adicionarProduto() {
        try {
            String tipo = (String) comboTipo.getSelectedItem();
            String codigo = campoCodigo.getText().trim();
            String nome = campoNome.getText().trim();
            double preco = Double.parseDouble(campoPreco.getText().trim());
            int quantidade = Integer.parseInt(campoQuantidade.getText().trim());

            Produto produto;
            if ("Material Basico".equals(tipo)) {
                String unidade = campoExtra1.getText().trim();
                produto = new MaterialBasico(codigo, nome, preco, quantidade, unidade);
            } else if ("Ferramenta".equals(tipo)) {
                int meses = Integer.parseInt(campoExtra1.getText().trim());
                produto = new Ferramenta(codigo, nome, preco, quantidade, meses);
            } else {
                double rendimento = Double.parseDouble(campoExtra2.getText().trim());
                produto = new Tinta(codigo, nome, preco, quantidade, rendimento);
            }

            estoque.adicionarProduto(produto);
            atualizarTabela();
            limparFormulario();

        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this,
                "Confira os campos numericos (preco, quantidade, garantia/rendimento).",
                "Erro", JOptionPane.ERROR_MESSAGE);
        } catch (IllegalArgumentException ex) {
            JOptionPane.showMessageDialog(this, ex.getMessage(), "Dado invalido", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void removerSelecionado() {
        int linha = tabela.getSelectedRow();
        if (linha == -1) {
            JOptionPane.showMessageDialog(this, "Selecione uma linha da tabela primeiro.");
            return;
        }
        String codigo = (String) modeloTabela.getValueAt(linha, 0);
        estoque.removerProduto(codigo);
        atualizarTabela();
    }

    private void exibirDetalhesSelecionado() {
        int linha = tabela.getSelectedRow();
        if (linha == -1) {
            JOptionPane.showMessageDialog(this, "Selecione uma linha da tabela primeiro.");
            return;
        }
        String codigo = (String) modeloTabela.getValueAt(linha, 0);
        Produto produto = estoque.buscarPorCodigo(codigo);
        String detalhes = (produto == null) ? "Produto nao encontrado." : produto.exibirDetalhes();
        JOptionPane.showMessageDialog(this, detalhes, "Detalhes do produto", JOptionPane.INFORMATION_MESSAGE);
    }

    private void calcularValorTotal() {
        double total = estoque.calcularValorTotalEstoque();
        labelValorTotal.setText(String.format("Valor total: R$ %.2f", total));
    }

    private void atualizarTabela() {
        modeloTabela.setRowCount(0);
        List<Produto> produtos = estoque.listarTodos();
        if (produtos == null) {
            return;
        }
        for (Produto p : produtos) {
            String tipo = p.getClass().getSimpleName();
            modeloTabela.addRow(new Object[]{
                p.getCodigo(), tipo, p.getNome(),
                String.format("R$ %.2f", p.getPreco()), p.getQuantidadeEstoque()
            });
        }
    }

    private void limparFormulario() {
        campoCodigo.setText("");
        campoNome.setText("");
        campoPreco.setText("");
        campoQuantidade.setText("");
        campoExtra1.setText("");
        campoExtra2.setText("");
    }
}
