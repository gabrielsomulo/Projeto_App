# Desafio: Sistema de pedidos - Padaria Trigo & Cia
#
# A interface do programa (menu, leitura do pedido, fluxo principal)
# já está pronta. Complete apenas as funções marcadas com TODO.

from datetime import datetime, timedelta

from typing import Final

CARDAPIO: Final = {
    "pao_frances": 0.80,
    "croissant": 6.50,
    "bolo_cenoura": 28.00,
    "torta_salgada": 32.00,
}

LIMITE_DESCONTO : Final = 100.00
PERCENTUAL_DESCONTO : Final = 0.10
LIMITE_ENCOMENDA : Final = 20
MENSAGEM_QTD : Final = "\n Quantidade inválida para cadastro!!!"

def mostrar_cardapio():
    print("=== Cardapio - Padaria Trigo & Cia ===")
    for item, preco in CARDAPIO.items():
        print(f"{item:<15} R$ {preco:.2f}")
    print()


def montar_pedido():
    """Interface pronta: lê itens e quantidades até o usuário digitar 'fim'."""
    pedido = {}
    while True:
        item = input("\n Item (ou 'fim' para encerrar): ").strip()

        if item.lower() == "fim":
            break
        if item not in CARDAPIO:
            print("\n Item nao encontrado no cardapio.\n ")
            continue

        try:
            quantidade = int(input(f"Quantidade de {item}: "))

        except ValueError:
            print(MENSAGEM_QTD)
            continue

        if quantidade <= 0: 
            print(MENSAGEM_QTD)
            continue

        else:
            pedido[item] = pedido.get(item, 0) + quantidade


    return pedido, verificar_quantidade_grande(pedido)


def verificar_quantidade_grande(pedido):
    """
    TODO: se quantidade > LIMITE_ENCOMENDA, avise que esse item precisa
    ser encomendado com 2 dias de antecedencia.
    """
    pedido_grande = {}
    for i in pedido.keys():
        if  pedido[i] > LIMITE_ENCOMENDA:
            pedido_grande[i] =  pedido[i]
    if len(pedido_grande) != 0:
        print("\n Atenção: A entrega só pode ser feita após 2 dias pela alta quantidade do(s) seguinte(s) item(s):")
        for pedido_k, pedido_v in pedido_grande.items():
            print(f"* {pedido_k} - {pedido_v}\n") 
        return True
    return False



def calcular_total(pedido):
    """
    TODO: some (preco * quantidade) de cada item de 'pedido' usando CARDAPIO
    e retorne o subtotal.
    """
    valor_total = 0

    for i in pedido.keys():
       valor_total += CARDAPIO[i] * pedido[i]

    return valor_total



def aplicar_desconto(subtotal):
    """
    TODO: se subtotal > LIMITE_DESCONTO, aplique PERCENTUAL_DESCONTO de desconto.
    Retorne uma tupla (total_final, valor_do_desconto).
    """
    
    if subtotal > LIMITE_DESCONTO:
        desconto = subtotal* PERCENTUAL_DESCONTO
        return subtotal - desconto, desconto

    return subtotal, 0.00


def checar_domingo(data):
    """
    TODO: receba uma data no formato 'DD/MM/AAAA' e retorne True se for domingo.
    Use datetime.strptime(data_str, "%d/%m/%Y") e o metodo .weekday().
    """

    if data.weekday() == 6:
        return True

    return False


def imprimir_recibo(pedido, subtotal, desconto, total, data_entrega):
    """
    TODO: imprima um recibo formatado com os itens, quantidades, subtotal,
    desconto (se houver), total e a data de entrega.
    """
    print(
        '='*100
    )
    for k, v in pedido.items():
        print(f"* Item: {k} - {v}x \n")

    print(
        f'''
        Subtotal: {subtotal:.2f} \n
        Desconto: {desconto:.2f} \n
        Total: {total:.2f} \n
        Data de entrega: {data_entrega}\n
        '''
    )
    print(
            '='*100
        )


def main():
    mostrar_cardapio()
    pedido, entrega_grande = montar_pedido()

    if not pedido:
        print("Nenhum item pedido.")
        return

    subtotal = calcular_total(pedido)
    
    total, desconto = aplicar_desconto(subtotal)

    while True:
    
        data_entrega = input("\n Data de entrega (DD/MM/AAAA): ").strip()

        try:
            dt = datetime.strptime(data_entrega, "%d/%m/%Y")

        except ValueError:
            print("\nData em formato inválido. Use DD/MM/AAAA.\n")
            continue

        data_atual = datetime.now()
        dias_ate_entrega = (dt.date() - data_atual.date()).days

        if (dias_ate_entrega < 0 or dias_ate_entrega > 365):
            print("\n Insira uma data válida!!")
            continue 

        else:
            if entrega_grande and dias_ate_entrega < 2:
                print(f'''
                        \n A entrega só pode ser feita 2 dias após o pedido.
                        \n Data atual: {data_atual.strftime("%d/%m/%Y")}
                        \n Data mínima para a entrega: {(data_atual + timedelta(days=3)).strftime("%d/%m/%Y")}
                    ''')
                continue
                
            if checar_domingo(dt):
                print("\n Atencao: a padaria nao entrega aos domingos. Escolha outra data. \n")
                continue
                
            else:
                break

        

    imprimir_recibo(pedido, subtotal, desconto, total, data_entrega)

if __name__ == "__main__":
    main()
