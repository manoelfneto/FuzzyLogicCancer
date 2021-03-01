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
ist['forte'] = fuzz.trimf(ist.universe, [2, 4, 4])
# ist.view()

fumante = ctrl.Antecedent(np.arange(0, 2, 1), 'fumante')
fumante.automf(names=['sim', 'nao'])
# fumante.view()

historico_familiar = ctrl.Antecedent(np.arange(0, 8, 1), 'historico_familiar')
historico_familiar['fraco'] = fuzz.trimf(historico_familiar.universe, [0, 0, 2])
historico_familiar['medio'] = fuzz.trimf(historico_familiar.universe, [1, 4, 5])
historico_familiar['forte'] = fuzz.trimf(historico_familiar.universe, [4, 7, 7])
# historico_familiar.view()

parceiros = ctrl.Antecedent(np.arange(0, 25, 1), 'parceiros')
parceiros['pouco'] = fuzz.trapmf(parceiros.universe, [0, 0, 2, 7])
parceiros['moderado'] = fuzz.trimf(parceiros.universe, [5, 11, 18])
parceiros['muito'] = fuzz.trapmf(parceiros.universe, [15, 20, 25, 25])
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

chance_simulator.input['idade'] = 65
chance_simulator.input['idade_primeira_relacao'] = 14
chance_simulator.input['historico_familiar'] = 6
chance_simulator.input['ist'] = 3
chance_simulator.input['fumante'] = 1
chance_simulator.input['parceiros'] = 17
chance_simulator.input['vacina_hpv'] = 1

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