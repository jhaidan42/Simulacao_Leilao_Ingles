from ambiente_leilao import Ambiente_leilao
from leiloeiro import Leiloeiro
from participante import Participante
import random
#Este é o código no qual a simulação do leilão é realizada. Define-se uma identificação do produto e
#seu preço e então o código deve ser rodado.
#São instanciados os objetos que representam o agente leiloeiro e o vetor de agentes participantes.
#No caso dos agentes participantes, os valores do teto, quantia em banco e força de vontade são
#selecionados de forma aleatória para a simulação.
#A força de vontade do agente participante representa quantitativamente o interesse deste no produto.
id_produto = 'Item1'
valor_produto = 1000

agente_leiloeiro1 = Leiloeiro(id_produto, valor_produto)

agentes_participantes = []
                                        # ('nome do produto', teto , quantia em banco, força de vontade)
agentes_participantes.append(Participante(id_produto, int(valor_produto * random.uniform(0.8, 1.2)), int(valor_produto * random.uniform(1.2, 2)), int(random.uniform(1, 4))))

agentes_participantes.append(Participante(id_produto, int(valor_produto * random.uniform(0.8, 1.2)), int(valor_produto * random.uniform(1.2, 2)), int(random.uniform(1, 4))))

agentes_participantes.append(Participante(id_produto, int(valor_produto * random.uniform(0.8, 1.2)), int(valor_produto * random.uniform(1.2, 2)), int(random.uniform(1, 4))))

#Aqui é instanciado um objeto para a classe Ambiente do leilão, e executada a função de executar o leilão.
leilao1 = Ambiente_leilao(agente_leiloeiro1, agentes_participantes)
leilao1.executar_leilao()
#Este programa foi baseado na solução de Emeka Onyebuchi.
#Disponível em: < https://github.com/Emeka-darthvader/Multi-Agent-Auction-System >.
#Acessado em 16 de maio de 2021.