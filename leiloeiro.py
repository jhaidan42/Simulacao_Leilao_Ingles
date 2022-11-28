#É definida aqui a classe Leiloeiro que será instanciada no painel.
#Suas funções são utilizadas na função de executar leilao, com o objetivo de compor mensagens que serão enviadas aos participantes.
class Leiloeiro:
    def __init__(self, id_produto, preco_produto):
        self.id_produto = id_produto
        self.preco_produto = preco_produto

    #Esta função é executada na primeira rodada, para anúncio e envio de informações do início do leilão.
    def interagir_inicio(self): #primeira rodada
        preco_inicial = self.preco_produto * 0.6 # o preço inicial é o valor de reserva (60% do valor real do produto)
        mensagem = str(preco_inicial) + ":" + "Leilao do produto " + self.id_produto + " iniciado. Dêem seus lances! :" + "propose"
        return mensagem

    #Esta função é executada a partir da segunda rodada, até a última, para anúncio e envio de mensagens informando e solicitando os agentes participantes as suas propostas.
    def interagir(self, maior_preco):
        mensagem = str(maior_preco)+":" + "é o novo lance mínimo. Quem dá mais? " +self.id_produto+ ":" + "propose"
        return mensagem

    #Esta função é executada no fim do leilão para anunciar e informar aos agentes participantes o fim do leilão, ou para solicitar o pagamento ao agente vencedor.
    def interagir_fim(self, vencedor, quantia, tipo_mensagem, FIPAperformative):
        if tipo_mensagem == "anuncio" and FIPAperformative == "inform" :
            anuncio = str(quantia) + ":" + "leilao do produto " + self.id_produto + " concluido: vencedor ->" + "Participante " + str(vencedor) + ":" + FIPAperformative
            return anuncio
        if tipo_mensagem == "mensagem" and FIPAperformative == "request" :
            mensagem = str(quantia) + ":" + "leilao do produto" + self.id_produto + " concluido: solcitar pagamento do vencedor->" + "Participante " + str(vencedor) + ":" + FIPAperformative
            return mensagem
