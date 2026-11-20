from pagamento import Pagamento


class PagamentoCartao(Pagamento):

    def calcular_valor_final(self):
        acrescimo = self.valor_base * 5 / 100
        return self.valor_base + acrescimo