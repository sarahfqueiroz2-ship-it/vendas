from pagamento import Pagamento


class PagamentoDebito(Pagamento):

    def calcular_valor_final(self):
        
        return self.valor_base