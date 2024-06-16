import os, random as r, json
from jff_to_json import Conversor_jff_regex
from Regex_to_NFA import Conversor_Regex_NFA
from NFA_to_DFA import Conversor_NFA_DFA
from json_to_xml import Converter_json_xml
from Simulador_AFD import Dfa_Simulator


def frases_generator(arqv, res):
    with open(arqv, 'r') as arqv:
        get_arq = json.load(arqv)
    
    letters = get_arq['letters']    

    if not os.path.exists(f'Entradas\\t{res}.txt'):

        with open(f'Entradas\\t{res}.txt', 'a') as test_file:
            for _ in range(0, 10):
                text = ''

                for _ in range(r.randint(10,50)):
                    text += r.choice(letters)
                    
                test_file.write(f"{text}\n")

opcoes = os.listdir('arquivos jflpa')
print('Qual ER usar:\n')
cont = 1
for o in opcoes:
    print(f'{cont}: {o}')
    cont += 1

res = input('\n> ')

try:
    converter_jff_to_regex = Conversor_jff_regex(f"arquivos jflpa\\t{res}.jff",res)
    arq_regex = converter_jff_to_regex.extrair_json()

    converter_regex_to_nfa = Conversor_Regex_NFA(regex=arq_regex["structure"], arqv= res)

    converter_nfa_dfa = Conversor_NFA_DFA(nfa_arqv=f"NFA\\t{res}.json", num_arq= res)

    converter_json_xml = Converter_json_xml(dfa= f"DFA\json\\t{res}.json", num_arq= res)

    frases_generator(f"DFA\\json\\t{res}.json", res)

    simulator = Dfa_Simulator(f"DFA\json\\t{res}.json")
    with open(f'Entradas\\t{res}.txt', 'r') as texts:
        input_string = texts.readlines()

        for string in input_string:
            is_accepted = simulator.simulate(string.replace("\n", ""))
            print(f"A sentença '{string}' é aceita pelo AFD: {is_accepted}")
            # print(string)

except FileNotFoundError as e:
    print(e)