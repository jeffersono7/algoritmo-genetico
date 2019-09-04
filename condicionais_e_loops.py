'''
individuo = '101001011'
cont = 0
i = 0

while i < len(individuo):
    if individuo[i] == '1':
        cont += 1
    i += 1
print('Quantidade de 1: ', cont)
print('Quantidade de 0: ', len(individuo) - cont)
'''

individuo = '101001011'
cont = 0

for i in range(len(individuo)):
    if individuo[i] == '1':
        cont += 1

print('Quantidade de 1: ', cont)
print('Quantidade de 0: ', len(individuo) - cont)

