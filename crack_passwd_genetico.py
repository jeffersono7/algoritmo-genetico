import random
import string
import sys
import operator


def fitness(senha, palavra):

    tam_senha = len(senha)

    if tam_senha != len(palavra):
        print('senhas incompativeis')
        return
    
    score = 0
    for i in range(tam_senha):
        if senha[i] == palavra[i]:
            score += 1
    
    return score * 100 / tam_senha

def gerar_individuo(tam):
    individuo = ''
    for i in range(tam):
        individuo += random.choice(string.ascii_lowercase)
    return individuo

def gerar_populacao(tam_pop, tam_senha):
    pop = []
    for i in range(tam_pop):
        pop.append(gerar_individuo(tam_senha))
    return pop

def pop_fitness(pop, senha):
    pop_score = {}
    for i in range(len(pop)):
        pop_score[i] = fitness(senha, pop[i])
    return sorted(pop_score.items(), key=operator.itemgetter(1), reverse=True)

def selecionar_pop(pop, pop_ordenada, qtd_melhores, qtd_aleatorios):
    prox_geracao = []
    for i in range(qtd_melhores):
        prox_geracao.append(pop[pop_ordenada[i][0]])
    for i in range(qtd_aleatorios):
        prox_geracao.append(pop[random.choice(pop_ordenada)[0]])
    random.shuffle(prox_geracao)
    return prox_geracao

def gerar_filho(ind1, ind2):
    filho = ''
    for i in range(len(ind1)):
        if int(100 * random.random()) < 50:
            filho += ind1[i]
        else:
            filho += ind2[i]
    return filho

def gerar_filhos(pop, num_filhos):
    prox_pop = []
    for i in range(len(pop) // 2):
        for j in range(num_filhos):
            prox_pop.append(gerar_filho(pop[i], pop[len(pop) -1 -i]))
    return prox_pop

def mutacao_individuo(individuo):
    indice = int(random.random() * len(individuo))
    letra_gene = random.choice(string.ascii_lowercase)
    if indice == 0:
        individuo = letra_gene + individuo[1:]
    else:
        individuo = individuo[:indice] + letra_gene + individuo[indice+1:]
    return individuo

def mutacao(pop, taxa):
    for i in range(len(pop)):
        if random.random()*100 < taxa:
            pop[i] = mutacao_individuo(pop[i])
    return pop

if __name__ == '__main__':

    senha = 'jefferson'
    tam_senha = len(senha)
    tam_pop = 300
    qtd_melhores = int(0.7 * tam_pop)
    qtd_aleatorios = int(0.3 * tam_pop)
    num_filhos = 2
    taxa_mutacao = 5
    max_iter = 30

    pop = gerar_populacao(tam_pop, tam_senha)
    
    for i in range(max_iter):
        pop_ordenada = pop_fitness(pop, senha)
        pop_selecionada = selecionar_pop(pop, pop_ordenada, qtd_melhores, qtd_aleatorios)
        nova_pop = gerar_filhos(pop_selecionada, num_filhos)
        pop = mutacao(nova_pop, taxa_mutacao)

    indice_melhor, score_melhor = pop_fitness(pop, senha)[0]
    print(f'Melhor individuo: {pop[indice_melhor]}')
    print(f'Score melhor individuo: {score_melhor}')
