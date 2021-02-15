import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

idade = ctrl.Antecedent(np.arange(0, 81, 1), 'idade')
idade['jovem'] = fuzz.trapmf(idade.universe, [0, 0, 12, 35])
idade['moderado'] = fuzz.trimf(idade.universe, [30, 42, 55])
idade['avancado'] = fuzz.trapmf(idade.universe, [50, 57, 80, 80])
# idade.view()

idade_primeira_relacao = ctrl.Antecedent(np.arange(0, 50, 1), 'idade_primeira_relacao')
idade_primeira_relacao['crianca/adolesc'] = fuzz.trapmf(idade_primeira_relacao.universe, [0, 0, 15, 20])
idade_primeira_relacao['jovem/adult'] = fuzz.trapmf(idade_primeira_relacao.universe, [15, 20, 50, 50])
# idade_primeira_relacao.view()

ist = ctrl.Antecedent(np.arange(0, 5, 1), 'ist')
ist['fraco'] = fuzz.trimf(ist.universe, [0, 0, 1])
ist['medio'] = fuzz.trimf(ist.universe, [0, 2, 3])
ist['forte'] = fuzz.trimf(ist.universe, [2, 3, 4])
# ist.view()

fumante = ctrl.Antecedent(np.arange(0, 2, 1), 'fumante')
fumante.automf(names=['sim', 'nao'])
# fumante.view()

historico_familiar = ctrl.Antecedent(np.arange(0, 11, 1), 'historico_familiar')
historico_familiar['fraco'] = fuzz.trimf(historico_familiar.universe, [0, 0, 2])
historico_familiar['medio'] = fuzz.trimf(historico_familiar.universe, [1, 4, 6])
historico_familiar['forte'] = fuzz.trimf(historico_familiar.universe, [5, 10, 10])
# historico_familiar.view()

parceiros = ctrl.Antecedent(np.arange(0, 10, 1), 'parceiros')
parceiros['pouco'] = fuzz.trapmf(parceiros.universe, [0, 0, 2, 5])
parceiros['moderado'] = fuzz.trimf(parceiros.universe, [3, 5, 7])
parceiros['muito'] = fuzz.trapmf(parceiros.universe, [6, 8, 10, 10])
# parceiros.view()

vacina_hpv = ctrl.Antecedent(np.arange(0, 2, 1), 'vacina_hpv')
vacina_hpv.automf(names=['sim', 'nao'])
# vacina_hpv.view()


chance = ctrl.Consequent(np.arange(0, 55, 1), 'chance')
chance['muito baixa'] = fuzz.trapmf(chance.universe, [0, 0, 5, 12])
chance['baixa'] = fuzz.trimf(chance.universe, [9, 15, 20])
chance['moderada'] = fuzz.trimf(chance.universe, [17, 23, 29])
chance['alta'] = fuzz.trimf(chance.universe, [26, 40, 52])
chance['muito alta'] = fuzz.trapmf(chance.universe, [49, 52, 55, 55])
# chance.view()

archive = open('rules2.csv', 'r')
content = archive.readlines()

rules = []
for x in content:
    a = x.rstrip('\n')
    rules.append(eval(a))

chance_ctrl = ctrl.ControlSystem(rules)
chance_simulator = ctrl.ControlSystemSimulation(chance_ctrl)

chance_simulator.input['idade'] = 28
chance_simulator.input['idade_primeira_relacao'] = 12
chance_simulator.input['historico_familiar'] = 2
chance_simulator.input['ist'] = 1
chance_simulator.input['fumante'] = 1
chance_simulator.input['parceiros'] = 2
chance_simulator.input['vacina_hpv'] = 0

chance_simulator.compute()
print(chance_simulator.output['chance'])
chance.view(sim=chance_simulator)
idade.view(sim=chance_simulator)
idade_primeira_relacao.view(sim=chance_simulator)
historico_familiar.view(sim=chance_simulator)
ist.view(sim=chance_simulator)
fumante.view(sim=chance_simulator)
parceiros.view(sim=chance_simulator)
vacina_hpv.view(sim=chance_simulator)
print('acabou')