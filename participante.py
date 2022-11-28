import random
#É definida aqui a Classe Participante, que será instanciada em um vetor de participantes no painel.
#Suas funções são utilizadas na função de executar leilao, com o objetivo de compor mensagens que serão enviadas ao leiloeiro.
class Participante:
    def __init__(self, id_produto, preco_teto, capacidade_banco, forca_de_vontade):
        self.id_produto = id_produto
        self.preco_teto = preco_teto
        self.capacidade_banco = capacidade_banco
        self.forca_de_vontade = forca_de_vontade
        self.maior_lance_anterior = 0
        self.teto_anterior = 0
        self.cont = 0

    #Esta função é executada nas funções da classe mensagem para envio de mensagens com as propostas de cada participante, ou para
    #indicar o recebimento de mensagens pelos agentes participantes, ou para resposta do agente vencedor à solicitação, do agente leiloeiro,
    #de informações do pagamento.
    def interagir(self, mensagem, preco_atual, FIPAperformative, id_agente = 0):
        if FIPAperformative == "propose" :

            print('"Participante', id_agente, 'envia sua proposta."')

            if self.forca_de_vontade == 1 :
                acrescimo_preco_porcentagem = round(random.uniform(0.01, 0.03), 2)
            elif self.forca_de_vontade == 2 :
                acrescimo_preco_porcentagem = round(random.uniform(0.04, 0.06), 2)
            elif self.forca_de_vontade == 3 :
                acrescimo_preco_porcentagem = round(random.uniform(0.07, 0.09), 2)
            elif self.forca_de_vontade == 4 :
                acrescimo_preco_porcentagem = round(random.uniform(0.1, 0.12), 2)

            preco_atual = float(preco_atual)
            if preco_atual <= self.preco_teto :
                lance = int(preco_atual + (acrescimo_preco_porcentagem * preco_atual))
                if lance > self.preco_teto :
                    lance = self.preco_teto
                    lance = int(lance)
                if self.maior_lance_anterior == preco_atual :
                    lance = int(preco_atual)
            elif preco_atual > self.preco_teto :
                lance = 0
            self.maior_lance_anterior = lance
            return (lance)

        if FIPAperformative == "inform" :
            print('"Participante', id_agente, 'recebe mensagem com a informação."' , mensagem)

        elif FIPAperformative == "request":
            print('"Vencedor retorna solicitação: Transferindo dinheiro para a conta."')
            print("Teto do vencedor --> ", self.preco_teto)
            print("Saldo inicial do banco do vencedor --> ",self.capacidade_banco)
            saldo_atual = self.capacidade_banco - int(preco_atual)
            utilitario_atual = self.preco_teto - int(preco_atual)
            print("Quantia paga pelo vencedor --> ", preco_atual)
            print("Saldo Final do Banco do vencedor --> ", saldo_atual)
            print("Utilitario do vencedor (Teto inicial - Preco da compra) = ", utilitario_atual)
