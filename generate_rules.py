import random

idade = ['jovem ', 'moderado ', 'avancado ']
idade_primeira_relacao = ['crianca/adolesc ', 'jovem/adult ']

ist = ['fraco ', 'medio ', 'forte ']
fumante = ['sim ', 'nao ']

historico_familiar = ['fraco ', 'medio ', 'forte ']

parceiros = ['pouco ', 'moderado ', 'muito ']
vacina_hpv = ['sim', 'nao']

# print(tamanho)
regras = []

for x in range(0, 10000):
    texto = random.choice(idade) + random.choice(idade_primeira_relacao) + random.choice(ist) + random.choice(fumante) \
            + random.choice(historico_familiar) + random.choice(parceiros) + random.choice(vacina_hpv)
    if texto not in regras:
        regras.append(texto)



for x in regras:
    points = 0
    crop = x.split(' ')
    if crop[0] == 'jovem':
        points += 1
    if crop[0] == 'moderado':
        points += 3
    if crop[0] == 'avancado':
        points += 2
    if crop[1] == 'crianca/adolesc':
        points += 1
    if crop[2] == 'fraco':
        points += 2
    if crop[2] == 'medio':
        points += 6
    if crop[2] == 'forte':
        points += 10
    if crop[3] == 'sim':
        points += 2
    if crop[4] == 'fraco':
        points += 2
    if crop[4] == 'medio':
        points += 6
    if crop[4] == 'forte':
        points += 10
    if crop[5] == 'pouco':
        points += 1
    if crop[5] == 'moderado':
        points += 3
    if crop[5] == 'muito':
        points += 4
    if crop[6] == 'nao':
        points += 1
    archive = open('rules2.csv', 'a')
    if points < 9:
        escrever = "ctrl.Rule(idade['%s'] | idade_primeira_relacao['%s'] | ist['%s'] | fumante['%s'] | " \
                   "historico_familiar['%s'] | parceiros['%s'] | vacina_hpv['%s'], chance['muito baixa'])" % \
                   (crop[0], crop[1], crop[2], crop[3], crop[4], crop[5], crop[6]) + "\n"
    if 10 <= points <= 14:
        escrever = "ctrl.Rule(idade['%s'] | idade_primeira_relacao['%s'] | ist['%s'] | fumante['%s'] | " \
                   "historico_familiar['%s'] | parceiros['%s'] | vacina_hpv['%s'], chance['baixa'])" % \
                   (crop[0], crop[1], crop[2], crop[3], crop[4], crop[5], crop[6]) + "\n"
    if 15 <= points <= 19:
        escrever = "ctrl.Rule(idade['%s'] | idade_primeira_relacao['%s'] | ist['%s'] | fumante['%s'] | " \
                   "historico_familiar['%s'] | parceiros['%s'] | vacina_hpv['%s'], chance['moderada'])" % \
                   (crop[0], crop[1], crop[2], crop[3], crop[4], crop[5], crop[6]) + "\n"
    if 20 <= points <= 27:
        escrever = "ctrl.Rule(idade['%s'] | idade_primeira_relacao['%s'] | ist['%s'] | fumante['%s'] | " \
                   "historico_familiar['%s'] | parceiros['%s'] | vacina_hpv['%s'], chance['alta'])" % \
                   (crop[0], crop[1], crop[2], crop[3], crop[4], crop[5], crop[6]) + "\n"
    if points > 27:
        escrever = "ctrl.Rule(idade['%s'] | idade_primeira_relacao['%s'] | ist['%s'] | fumante['%s'] | " \
                   "historico_familiar['%s'] | parceiros['%s'] | vacina_hpv['%s'], chance['muito alta'])" % \
                   (crop[0], crop[1], crop[2], crop[3], crop[4], crop[5], crop[6]) + "\n"

    archive.write(escrever)