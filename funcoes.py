import random

tam_pop = 10
tam_genes = 5

def gerar_individuo(tam_genes):
    s = ''
    for i in range(tam_genes):
        s += str(random.randrange(0, 2))
    return s

def gerar_populacao(tam_pop):
    populacao = []
    for i in range(tam_pop):
        populacao.append(gerar_individuo(tam_genes))
    return populacao

populacao = gerar_populacao(tam_pop)

for i in range(tam_pop):
    print(populacao[i])

