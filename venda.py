from datetime import datetime
from item_venda import Item_Venda
from produto import Produto


class Venda:

    def __init__(self, data_venda=None):
        self._valor_total = 0.0
        if data_venda is None:
            self._data_venda = datetime.now()
        else:
            self._data_venda = data_venda
        self._itens = []
        self._pagamento = None

    @property
    def itens(self):
        return self._itens

    @property
    def pagamento(self):
        return self._pagamento

    def adicionar_item(self, produto, quantidade):
        if produto.decrementar_estoque(quantidade):
            novo_item = Item_Venda(produto, quantidade)
            self._itens.append(novo_item)
            self._valor_total += novo_item.valor
            return True
        else:
            return False

    def remover_item(self, produto):
        for item in self._itens:
            if item.produto == produto:
                self._itens.remove(item)
                self._valor_total -= item.valor
                produto.incrementar_estoque(item.quantidade)
                return True
        return False

    def calcular_valor_total(self):
        return self._valor_total

    def finalizar_venda(self, pagamento):
    
        if len(self._itens) == 0:
            print("Não é possível finalizar uma venda sem itens.")
            return None

        pagamento.valor_base = self.calcular_valor_total()
        self._pagamento = pagamento
        return pagamento.calcular_valor_final()

    def __str__(self):
        string = "\n========== COMPROVANTE =========="
        string += "\nVenda: " + self._data_venda.strftime("%d/%m/%Y %H:%M:%S")
        string += "\n---------------------------------"

        for item in self._itens:
            string += (
                "\n" + item.produto.descricao +
                " | " + str(item.quantidade) + "x" +
                " | R$ " + str(round(item.produto.preco_unitario, 2)) +
                " | Subtotal: R$ " + str(round(item.valor, 2))
            )

        string += "\n---------------------------------"
        string += "\nValor total: R$ " + str(round(self.calcular_valor_total(), 2))

        if self._pagamento is not None:
            string += "\nPagamento: " + self._pagamento.__class__.__name__
            string += "\nValor final a pagar: R$ " + str(round(self._pagamento.calcular_valor_final(), 2))

        string += "\n================================="
        return string