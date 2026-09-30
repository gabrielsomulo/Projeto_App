# Desafio: Loja MegaConstrução — Controle de Estoque (Java + Swing)

Requisito da loja: um sistema desktop para cadastrar e controlar o
estoque de três tipos de produto — materiais básicos (cimento, areia,
tijolo), ferramentas e tintas — cada um com uma regra de preço própria.

A interface (`TelaPrincipal.java`, com Swing/JFrame) já está pronta e
funcional. O desafio de verdade está nas classes do modelo: implementar
a herança, o polimorfismo e o encapsulamento corretamente.

## Estrutura

```
src/loja/
├── Produto.java          — classe abstrata (o desafio começa aqui)
├── MaterialBasico.java    — subclasse: desconto por quantidade grande
├── Ferramenta.java        — subclasse: tem garantia, sem desconto
├── Tinta.java              — subclasse: rendimento em m² por litro
├── Estoque.java           — gerencia a coleção de produtos (TODO)
├── TelaPrincipal.java     — interface pronta (Swing/JFrame)
└── Main.java              — ponto de entrada
```

## Como compilar e rodar

**Pelo terminal:**
```bash
cd src
javac -encoding UTF-8 -d ../out loja/*.java
cd ../out
java loja.Main
```
O `-encoding UTF-8` é necessário porque os comentários do código têm
acentuação — sem essa flag, o `javac` pode reclamar de caractere
inválido dependendo da configuração regional do seu Windows.

**Pelo NetBeans:**
Crie um projeto Java novo ("Java with Ant" ou "Java with Maven", tanto
faz para um projeto deste tamanho), copie os arquivos de `src/loja/`
para dentro do pacote `loja` do projeto, defina `Main.java` como
classe principal (já vem assim por padrão, já que só há um `main`), e
rode com F6. O NetBeans já usa UTF-8 por padrão em projetos novos, então
o problema de encoding do terminal não deve aparecer.

## O desafio: completar `Produto`, `MaterialBasico`, `Ferramenta`, `Tinta` e `Estoque`

### Em `Produto.java` (classe abstrata — encapsulamento)
1. `setNome`, `setPreco`, `setQuantidadeEstoque` — validar os valores
   antes de atribuir (nome não vazio, preço > 0, quantidade ≥ 0),
   lançando `IllegalArgumentException` quando inválido.

### Em cada subclasse (herança + polimorfismo)
2. `MaterialBasico.calcularPrecoFinal` — preço × quantidade, com 5% de
   desconto se a quantidade for ≥ 50.
3. `Ferramenta.calcularPrecoFinal` — preço × quantidade, sem desconto.
4. `Tinta.calcularPrecoFinal` — preço × quantidade (em litros).
5. `exibirDetalhes()` nas três — cada uma monta uma descrição incluindo
   seus próprios dados (unidade de medida / meses de garantia /
   rendimento por litro), além dos dados comuns herdados de `Produto`.

### Em `Estoque.java` (comunicação entre classes)
6. `adicionarProduto`, `removerProduto`, `buscarPorCodigo`, `listarTodos`
   — operações básicas sobre a lista de produtos.
7. `calcularValorTotalEstoque` — o ponto central do desafio de
   polimorfismo: percorrer todos os produtos e chamar
   `produto.calcularPrecoFinal(produto.getQuantidadeEstoque())` em cada
   um, **sem nenhum `if (produto instanceof ...)`**. O mesmo método
   chamado em objetos de tipos diferentes deve produzir resultados
   diferentes, porque cada subtipo implementou o método à sua maneira.

## O que será avaliado

- **Encapsulamento real**: os setters rejeitam valores inválidos (não é
  só deixar os atributos `private` por formalidade — o valor de um
  setter está em *validar*, não só em esconder o campo).
- **Herança correta**: as três subclasses reaproveitam o construtor e
  os getters de `Produto` via `super(...)`, sem duplicar código.
- **Polimorfismo genuíno**: `Estoque.calcularValorTotalEstoque()` não
  pode ter nenhum desvio por tipo (`instanceof`, `getClass()` para
  decidir o cálculo) — a diferença de comportamento vem inteiramente
  de cada subclasse ter implementado `calcularPrecoFinal` do seu jeito.
- **Sem `NullPointerException`**: `buscarPorCodigo` e `listarTodos`
  precisam lidar bem com estoque vazio ou código inexistente.

## Como testar

1. Rode o programa e cadastre um `Material Basico` (ex: Cimento, R$
   32,50, 60 sacos) — deve aparecer na tabela.
2. Cadastre uma `Ferramenta` (ex: Martelo, R$ 45,00, 10 unidades, 6
   meses de garantia) e uma `Tinta` (ex: Tinta branca, R$ 89,90, 20
   litros, rendimento 8,5).
3. Clique em "Ver detalhes do selecionado" em cada linha — a descrição
   deve mudar de acordo com o tipo (prova de que o polimorfismo em
   `exibirDetalhes()` está funcionando).
4. Clique em "Calcular valor total do estoque" — o cimento (60 sacos,
   acima do limite de 50) deve entrar com desconto de 5%; martelo e
   tinta, sem desconto.
5. Remova um produto e confirme que ele some tanto da tabela quanto do
   cálculo do valor total.
