# Desafio: Loja MegaConstrução — Controle de Estoque (Python + Tkinter)

Mesmo desafio da versão Java, agora em Python: um sistema desktop para
cadastrar e controlar o estoque de três tipos de produto — materiais
básicos (cimento, areia, tijolo), ferramentas e tintas — cada um com
uma regra de preço própria.

A interface (`interface.py`, com Tkinter) já está pronta e funcional.
O desafio de verdade está nas classes do modelo: implementar a
herança, o polimorfismo e o encapsulamento corretamente.

## Estrutura

```
produto.py           — classe base abstrata, via abc.ABC (o desafio começa aqui)
material_basico.py   — subclasse: desconto por quantidade grande
ferramenta.py         — subclasse: tem garantia, sem desconto
tinta.py              — subclasse: rendimento em m² por litro
estoque.py            — gerencia a coleção de produtos (TODO)
interface.py          — interface pronta (Tkinter)
main.py               — ponto de entrada
```

Nenhuma dependência externa é necessária — `tkinter` já vem embutido
no Python (no Windows, a instalação padrão do python.org já inclui;
em algumas distribuições Linux é um pacote separado, tipo
`sudo apt install python3-tk`).

## Como rodar

```bash
python main.py
```

## O desafio: completar `produto.py`, as três subclasses e `estoque.py`

### Em `produto.py` (classe abstrata — encapsulamento)
Usamos o módulo `abc` (Abstract Base Classes) e `@property`/`@x.setter`
— o jeito formal do Python de fazer o que o Java faz com `abstract` e
getters/setters. Se você tentar `Produto("X", "Y", 1, 1)` direto (sem
passar por uma subclasse), o Python já recusa, porque a classe tem
métodos abstratos não implementados — o mesmo espírito do `abstract
class` do Java.

1. `nome.setter`, `preco.setter`, `quantidade_estoque.setter` — validar
   os valores antes de guardar (nome não vazio, preço > 0, quantidade
   ≥ 0), lançando `raise ValueError("mensagem clara")` quando inválido.

### Em cada subclasse (herança + polimorfismo)
2. `MaterialBasico.calcular_preco_final` — preço × quantidade, com 5%
   de desconto se a quantidade for ≥ 50.
3. `Ferramenta.calcular_preco_final` — preço × quantidade, sem desconto.
4. `Tinta.calcular_preco_final` — preço × quantidade (em litros).
5. `exibir_detalhes()` nas três — cada uma monta uma descrição incluindo
   seus próprios dados (unidade de medida / meses de garantia /
   rendimento por litro), além dos dados comuns herdados de `Produto`.

### Em `estoque.py` (comunicação entre classes)
6. `adicionar_produto`, `remover_produto`, `buscar_por_codigo`,
   `listar_todos` — operações básicas sobre a lista de produtos.
7. `calcular_valor_total_estoque` — o ponto central do desafio de
   polimorfismo: percorrer todos os produtos e chamar
   `produto.calcular_preco_final(produto.quantidade_estoque)` em cada
   um, **sem nenhum `isinstance(produto, ...)`**. O mesmo método
   chamado em objetos de tipos diferentes deve produzir resultados
   diferentes, porque cada subtipo implementou o método à sua maneira.

## O que será avaliado

- **Encapsulamento real**: os setters (`@x.setter`) rejeitam valores
  inválidos — o valor está em *validar*, não só em ter o `_` na frente
  do nome do atributo.
- **Herança correta**: as três subclasses reaproveitam o `__init__` de
  `Produto` via `super().__init__(...)`, sem duplicar código.
- **Polimorfismo genuíno**: `Estoque.calcular_valor_total_estoque()`
  não pode ter nenhum desvio por tipo (`isinstance`, `type(produto)`
  para decidir o cálculo) — a diferença de comportamento vem
  inteiramente de cada subclasse ter implementado
  `calcular_preco_final` do seu jeito.
- **Sem retornar `None` por engano**: depois de implementadas, as
  funções de `estoque.py` precisam ter `return` explícito — é comum
  esquecer e a função "funcionar" silenciosamente sem retornar nada
  (o mesmo tipo de bug que já apareceu no desafio da loja com
  `conn.commit` sem parênteses — aqui o equivalente é esquecer o
  `return`).

## Como testar

1. Rode o programa e cadastre um `Material Basico` (ex: Cimento, R$
   32,50, 60 sacos) — deve aparecer na tabela.
2. Cadastre uma `Ferramenta` (ex: Martelo, R$ 45,00, 10 unidades, 6
   meses de garantia) e uma `Tinta` (ex: Tinta branca, R$ 89,90, 20
   litros, rendimento 8,5).
3. Clique em "Ver detalhes do selecionado" em cada linha — a descrição
   deve mudar de acordo com o tipo (prova de que o polimorfismo em
   `exibir_detalhes()` está funcionando).
4. Clique em "Calcular valor total do estoque" — o cimento (60 sacos,
   acima do limite de 50) deve entrar com desconto de 5%; martelo e
   tinta, sem desconto.
5. Remova um produto e confirme que ele some tanto da tabela quanto do
   cálculo do valor total.
