from pagamento import Pagamento


class PagamentoDinheiro(Pagamento):

    def calcular_valor_final(self):
        desconto = self.valor_base * 3 / 100
        return self.valor_base - desconto