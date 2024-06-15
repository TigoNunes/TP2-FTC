import os
from jff_to_json import Conversor_jff_regex
from Regex_to_NFA import Conversor_Regex_NFA
from NFA_to_DFA import Conversor_NFA_DFA

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

    converter_nfa_dfa = Conversor_NFA_DFA(nfa_arqv=f"NFA\\t{res}.json", arqv= res)

except FileNotFoundError as e:
    print(e)