from produto import Produto
from venda import Venda
from pagamento_debito import PagamentoDebito
from pagamento_pix import PagamentoPix
from pagamento_dinheiro import PagamentoDinheiro
from pagamento_cartao import PagamentoCartao


def montar_venda():
    produto1 = Produto(descricao="mouse", preco_unitario=100, estoque=2)
    produto2 = Produto(descricao="pendrive", preco_unitario=50, estoque=7)
    produto3 = Produto(descricao="monitor", preco_unitario=1000, estoque=10)
    venda = Venda()
    venda.adicionar_item(produto=produto1, quantidade=1)
    venda.adicionar_item(produto=produto2, quantidade=4)
    venda.adicionar_item(produto=produto3, quantidade=3)
    return venda


print(f"Vendas no sistema (início): {Venda.get_quantidade_vendas()}")

venda1 = montar_venda()
venda1.finalizar_venda(PagamentoDebito(venda1.calcular_valor_total()))
print(venda1)

venda2 = montar_venda()
venda2.finalizar_venda(PagamentoPix(venda2.calcular_valor_total()))
print(venda2)

venda3 = montar_venda()
venda3.finalizar_venda(PagamentoDinheiro(venda3.calcular_valor_total()))
print(venda3)

venda4 = montar_venda()
venda4.finalizar_venda(PagamentoCartao(venda4.calcular_valor_total()))
print(venda4)

print(f"\nVendas no sistema (final): {Venda.get_quantidade_vendas()}")