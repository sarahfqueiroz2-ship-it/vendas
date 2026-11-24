from datetime import datetime
from item_venda import Item_Venda
from produto import Produto
from pagamento import Pagamento


class Venda:

    _quantidade_vendas = 0

    def __init__(self, data_venda: datetime = None):
        self._valor_total = 0.0
        self._data_venda = data_venda or datetime.now()
        self._itens: list[Item_Venda] = []
        self._pagamento = None 
        Venda._quantidade_vendas += 1             

    @property
    def itens(self):
        return self._itens

    @property
    def pagamento(self):
        return self._pagamento

    @classmethod
    def get_quantidade_vendas(cls):
        return cls._quantidade_vendas

    def adicionar_item(self, produto: Produto, quantidade: int):
        if produto.decrementar_estoque(quantidade):
            novo_item = Item_Venda(produto, quantidade)
            self._itens.append(novo_item)
            self._valor_total += novo_item.valor
            return True
        else:
            return False

    def remover_item(self, produto: Produto):
        for item in self._itens:
            if item.produto == produto:
                self._itens.remove(item)
                self._valor_total -= item.valor
                produto.incrementar_estoque(item.quantidade)
                return True
        return False

    def calcular_valor_total(self):
        return self._valor_total

    def finalizar_venda(self, pagamento: Pagamento):
        if len(self._itens) == 0:
            print("Não é possível finalizar uma venda sem itens.")
            return None
        pagamento.valor_base = self.calcular_valor_total()
        self._pagamento = pagamento
        return pagamento.calcular_valor_final()

    def __str__(self):
        string = "\n========== COMPROVANTE =========="
        string += f"\nVenda: {self._data_venda.strftime('%d/%m/%Y %H:%M:%S')}"
        string += "\n---------------------------------"

        for item in self._itens:
            string += (
                f"\n{item.produto.descricao} | "
                f"{item.quantidade}x | "
                f"R$ {item.produto.preco_unitario:.2f} | "
                f"Subtotal: R$ {item.valor:.2f}"
            )
        string += "\n---------------------------------"
        string += f"\nValor total: R$ {self.calcular_valor_total():.2f}"

        if self._pagamento is not None:
            string += f"\nPagamento: {self._pagamento.__class__.__name__}"
            string += f"\nValor final a pagar: R$ {self._pagamento.calcular_valor_final():.2f}"

        string += "\n================================="
        return string