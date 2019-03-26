import random

j = int(input('QUANTOS JOGOS VOCÊ VAI APOSTAR: '))
cont = 1
tot1 = tot2 = 0
times=(vasco, flamengo, ponte)

while cont <= j:
    print('{}º JOGO'.format(cont))
    t1 = str(input('Time da casa: ')).strip().upper()
    g1 = str(input('O time da casa GANHOU, PERDEU OU EMPATOU o ultimo jogo? [ G / P / E ] ')).strip().upper()
    if g1 == 'G':
        j1 = str(input('GANHOU FORA OU EM CASA? [F / C ]')).strip().upper()[0]
        if j1 == 'F':
            tot1 = 6
        elif j1 == 'C':
            tot1 = 3
        total1 = tot1 + 10

    elif g1 == 'P':
        j1 = str(input('PERDEU FORA OU EM CASA? [F / C ]')).strip().upper()[0]
        if j1 == 'F':
            tot1 = -1
        elif j1 == 'C':
            tot1 = -3
        total1 = tot1 - 10

    elif g1 == 'E':
        j1 = str(input('EMPATOU FORA OU EM CASA? [F / C ]')).strip().upper()[0]
        if j1 == 'F':
            tot1 = 2
        elif j1 == 'C':
            tot1 = 1
        total1 = tot1 + 5



    t2 = str(input('Time de fora: ')).strip().upper()
    g2 = str(input('O time da casa GANHOU, PERDEU OU EMPATOU o ultimo jogo? [ G / P / E ] ')).strip().upper()
    if g2 == 'G':
        j2 = str(input('GANHOU FORA OU EM CASA? [F / C ]')).strip().upper()[0]
        if j2 == 'F':
            tot2 = 6
        elif j2 == 'C':
            tot2 = 3
        total2 = tot2 + 10

    elif g2 == 'P':
        j2 = str(input('PERDEU FORA OU EM CASA? [F / C ]')).strip().upper()[0]
        if j2 == 'F':
            tot2 = -1
        elif j2 == 'C':
            tot2 = -3
        total2 = tot2 - 10

    elif g2 == 'E':
        j2 = str(input('EMPATOU FORA OU EM CASA? [F / C ]')).strip().upper()[0]
        if j2 == 'F':
            tot1 = 2
        elif j2 == 'C':
            tot1 = 1
        total2 = tot2 + 5

    cont += 1

if g1 > g2:
    print(f'O time a ganhar será {t1}')
elif g1 < g2:
    print(f'O time a ganhar será {t2}')
else:
    print(f'{t1} contra {t2} resultará em um EMPATE')




    '''s = [t1, t2, t3]
  
    sorteio = random.choice(s)
    print(sorteio)
    cont += 1'''

