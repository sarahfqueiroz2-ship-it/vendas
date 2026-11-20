from pagamento import Pagamento


class PagamentoPix(Pagamento):

    def calcular_valor_final(self):
    
        desconto = self.valor_base * 5 / 100
        return self.valor_base - desconto