import random

idade = ['jovem ', 'moderado ', 'avancado ']
idade_primeira_relacao = ['crianca/adolesc ', 'jovem/adult ']

ist = ['fraco ', 'medio ', 'forte ']
fumante = ['sim ', 'nao ']

historico_familiar = ['fraco ', 'medio ', 'forte ']

parceiros = ['pouco ', 'moderado ', 'muito ']
vacina_hpv = ['sim', 'nao']

#print(tamanho)
regras = []

for x in range(0, 10000):
    texto = random.choice(idade) + random.choice(idade_primeira_relacao) + random.choice(ist) + random.choice(fumante) \
            + random.choice(historico_familiar) + random.choice(parceiros) + random.choice(vacina_hpv)
    if texto not in regras:
        regras.append(texto)

contador = 0
for x in regras:
    crop = x.split(' ')
    archive = open('rules2.csv', 'a')
    escrever = "ctrl.Rule(idade['%s'] | idade_primeira_relacao['%s'] | ist['%s'] | fumante['%s'] | " \
               "historico_familiar['%s'] | parceiros['%s'] | vacina_hpv['%s'], chance['alta'])" % \
               (crop[0], crop[1], crop[2], crop[3], crop[4], crop[5], crop[6]) + "\n"
    archive.write(escrever)
    contador += 1





