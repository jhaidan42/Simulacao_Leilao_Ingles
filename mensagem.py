#É definida aqui a Classe Mensagem, que será instanciada na função de executar o leilão no ambiente do leilão.
#Suas funções são utilizadas para troca de mensagens entre o agente leiloeiro e os agentes participantes
#A troca de mensagens é feita pela linguagem de comunicação FIPA, como um exemplo simples que usa três performativos:
# o "propose", o "inform" e o "request".
class Mensagem :
    def __init__(self, conteudo, id_produto, leiloeiro, participantes, tipo_mensagem, FIPAperformative):
        self.conteudo = conteudo
        self.leiloeiro = leiloeiro
        self.participantes = participantes
        self.tipo_mensagem = tipo_mensagem
        self.FIPAperformative = FIPAperformative
        self.id_produto = id_produto
        self.numero_agente = 0

    #Esta função possibilita a solicitação, pelo agente leiloeiro, aos agentes participantes realizarem suas propostas e as retornar.
    #As mensagens aqui, podem ser de anúncio (para que seja anunciado no leilão a solicitação e o retorno de propostas) ou
    #efetivamente de mensagem (para a troca de mensagens entre o agente leiloeiro e os agentes participantes).
    def propose(self) :
        if self.tipo_mensagem == "anuncio" :
            print('"Leiloeiro anuncia o inicio do Leilao e envia mensagem para participantes realizarem suas propostas."')
        elif self.tipo_mensagem == "mensagem" :
            print('"Leiloeiro envia mensagem para participantes realizarem suas propostas."')

        lances = []
        divisao_conteudo = self.conteudo.split(":")
        preco = divisao_conteudo[0]
        conteudo = divisao_conteudo[1]
        protocolo_fipa = divisao_conteudo[2]

        if self.tipo_mensagem == "mensagem" :
            print('"Enviando --> ' + preco +" "+ conteudo+'"')
        elif self.tipo_mensagem == "anuncio" :
            print('"Enviando --> ' + conteudo+'"')

        for participante in self.participantes :
            self.numero_agente += 1
            participantes_lances = participante.interagir(self.conteudo, preco, protocolo_fipa, self.numero_agente)
            lances.append(participantes_lances)

        return lances

    #Esta função possibilita que o agente leiloeiro informe aos agentes participantes que o leilão teve um vencedor
    #e foi finalizado. Permite também que essa informação sej anunciada no leilão.
    def inform(self) :
        print('"Leiloeiro envia mensagem para participantes informando o fim do leilão, o participante vencedor e o valor pago."')
        divisao_conteudo = self.conteudo.split(":")
        maior_lance = divisao_conteudo[0]
        protocolo_fipa = divisao_conteudo[3]
        for participante in self.participantes :
            self.numero_agente += 1
            participante.interagir(self.conteudo, maior_lance, protocolo_fipa, self.numero_agente)

    #Esta função permite que o agente leiloeiro solicite ao agente vencedor o pagamento.
    def request(self, id_agente):
        print('"Leiloeiro solicita o pagamento do produto ao vencedor"')
        divisao_conteudo = self.conteudo.split(":")
        maior_lance = divisao_conteudo[0]
        protocolo_fipa = divisao_conteudo[3]
        self.participantes[id_agente].interagir(self.conteudo, maior_lance, protocolo_fipa, id_agente)