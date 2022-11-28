from mensagem import Mensagem
#É definica aqui a classe Ambiente do Leilão, que será instanciada no painel do leilão.
#É aqui que o leilão acontece de fato.
class Ambiente_leilao :
    def __init__(self, leiloeiro, participantes, rodada = 0) :
        self.leiloeiro = leiloeiro
        self.participantes = participantes
        self.rodada = rodada

    #Esta função é que executa o leilão do início ao fim, até que o produto seja vendido ou que haja um
    #empate que seja impossível de resolver neste código.
    #Aqui são instanciados objetos da classe Mensagem para a realização da troca de mensagens entre
    #os agentes participantes e o agente leiloeiro, durante o leilão.
    def executar_leilao(self) :
        vencedor = []
        produto_vendido = False
        lances_e_agentes = {}
        maior_lance = 0
        indice_vencedor = []
        numero_agente = 0
        num_participantes = len(self.participantes)
        preco_inicial = int(0.6 * self.leiloeiro.preco_produto)

        print("*" * 50, "Informações do leilão")
        print("Tipo: Inglês")
        print("Produto:", self.leiloeiro.id_produto, "| Preço inicial:", preco_inicial)
        print("Participantes interessados:")
        p=1
        for participante in self.participantes :
            print("Participante",p, ": Para o leilao do ",participante.id_produto,"--> Força de vontade = ", participante.forca_de_vontade," |  Quantia em banco =", participante.capacidade_banco, "| Teto = ", participante.preco_teto)
            p+=1
        print("*" * 50)

        empates = 0
        #Esta repetição permite executar as rodadas do leilão enquanto o produto não está vendido.
        while produto_vendido == False :
            desistencias = 0
            if self.rodada == 0:
                print("*"*50, "Rodada 1")
                conteudo_mensagem1 = self.leiloeiro.interagir_inicio()
                chamada_para_proposta1 = Mensagem(conteudo_mensagem1, self.leiloeiro.id_produto, self.leiloeiro, self.participantes, "anuncio", "propose")
                lances_anuncio = chamada_para_proposta1.propose()
                if maior_lance == 0:
                    for lance in lances_anuncio:
                        if lance > maior_lance:
                            maior_lance = lance

                print("Todos os lances na ordem do número do participante: ", lances_anuncio)
                print("Maior lance: ", maior_lance)
                self.rodada += 1

            #Esta condição permite a execução do leilão até que apenas um agente participante não desista de adquirir o produto.
            if desistencias != len(lances_anuncio)-1 and len(lances_anuncio) >= 1 :
                print("*"*50, "Rodada", self.rodada+1)
                conteudo_mensagem2 = self.leiloeiro.interagir(maior_lance)
                chamada_para_proposta2 = Mensagem(conteudo_mensagem2, self.leiloeiro.id_produto, self.leiloeiro, self.participantes, "mensagem", "propose")
                lances_anuncio = chamada_para_proposta2.propose()
                lances_e_agentes = { i : lances_anuncio[i] for i in range(0, len(lances_anuncio) ) }
                for lance in lances_anuncio :
                    if lance > maior_lance:
                        maior_lance = lance
                print("Todos os lances na ordem do número do participante: ", lances_anuncio)
                print("Maior lance: ", maior_lance)

                self.rodada += 1

            for lance in lances_anuncio :
                if lance == 0 :
                    desistencias += 1

            for i in range(0, len(lances_anuncio), 1) :
                for j in range(i + 1, len(lances_anuncio), 1) :
                    if lances_anuncio[i] == lances_anuncio [j] :
                        empates +=1

            #Esta condição, juntamente com o laço acima, encerra o leilão em caso de empates consecutivos, efetuando uma
            #solução parcial em relação ao empate. Este código não traz uma solução real para empate principalmente
            #pelo fato de ser umna simulação de leilão na qual a ordem do tempo não é levada em consideração.
            #Ou seja, não é determinado qual agente participante propôs primeiro.
            if empates >= 12 :
                produto_vendido = True
                print("Empate! Os participantes discutirão a possibilidade de dividir o produto.")
                return 1

            #Esta condição finaliza o leilão quando resta apenas 1 agente participante.
            if desistencias == (len(lances_anuncio)-1) and len(lances_anuncio) >= 1 :
                produto_vendido = True
                print("Fim do leilao!")
                print("Maior lance: ", maior_lance)

            #Esta condição faz com que o leiloeiro informe a redução do lance mínimo, para uma próxima rodada, quando todos
            #os agentes participantes preferem não propor mais.
            if desistencias == len(lances_anuncio) and len(lances_anuncio) >= 1 :
                conteudo_mensagem5 = self.leiloeiro.interagir(maior_lance)
                chamada_para_proposta3 = Mensagem(conteudo_mensagem5, self.leiloeiro.id_produto, self.leiloeiro, self.participantes, "mensagem", "propose")
                lances_anuncio = chamada_para_proposta3.propose()
                lances_e_agentes = {i: lances_anuncio[i] for i in range(0, len(lances_anuncio))}
                for lance in lances_anuncio:
                    if lance > maior_lance:
                        maior_lance = lance

                desistencias = 0
                for lance in lances_anuncio:
                    if lance == 0:
                        desistencias += 1

                if desistencias == (len(lances_anuncio)-1) and len(lances_anuncio) >= 1 :
                    produto_vendido = True
                    print("Fim do leilao!")
                    print("Maior lance: ", maior_lance)

        if len(lances_e_agentes) >= 1 :
            for x, y in lances_e_agentes.items() :
                if y == maior_lance :
                    indice_vencedor.append(x)

        #A partir daqui, são executadas as ações de anunciar o fim do leilão e o vencedor, informar aos agentes e solocitar o pagamento.
        if len(indice_vencedor) > 0:
            posicao_vencedor = len(indice_vencedor) - 1

            indice_agente_vencedor = indice_vencedor[posicao_vencedor]
            numero_agente = indice_vencedor[posicao_vencedor] + 1

            print("#"*50)
            print("O participante numero "+ str(numero_agente) + " ganhou o leilao do produto "+self.leiloeiro.id_produto)
            conteudo_mensagem3 = self.leiloeiro.interagir_fim(numero_agente, maior_lance, "anuncio", "inform")
            informar_agentes = Mensagem(conteudo_mensagem3, self.leiloeiro.id_produto, self.leiloeiro, self.participantes, "anuncio", "inform")
            informar_agentes.inform()

            conteudo_mensagem4 = self.leiloeiro.interagir_fim(indice_agente_vencedor, maior_lance, "mensagem", "request")
            solicitar_pagamento_agente = Mensagem(conteudo_mensagem4, self.leiloeiro.id_produto, self.leiloeiro, self.participantes, "mensagem", "request")
            solicitar_pagamento_agente.request(indice_agente_vencedor)
            print("#"*50)

        return vencedor