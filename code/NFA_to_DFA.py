import json

class Conversor_NFA_DFA:
    def __init__(self, nfa_arqv, arqv):
        self.dfa = {}
        self.nfa = {}
        self.nfa_states = []
        self.dfa_states = []

        self.load_nfa(nfa_arqv)
    
        self.dfa['states'] = []
        self.dfa['letters'] = self.nfa['letters']
        self.dfa['transition_function'] = []
        
        for state in self.nfa['states']:
            self.nfa_states.append(state)

        self.dfa_states = self.get_power_set(self.nfa_states)

        self.dfa['states'] = []
        for states in self.dfa_states:
            temp = []
            for state in states:
                temp.append(state)
            self.dfa['states'].append(temp)

        for states in self.dfa_states:
            for letter in self.nfa['letters']:
                q_to = []
                for state in states:
                    for val in self.nfa['transition_function']:
                        start = val[0]
                        inp = val[1]
                        end = val[2]
                        if state == start and letter == inp:
                            if end not in q_to:
                                q_to.append(end)
                q_states = []
                for i in states:
                    q_states.append(i)
                self.dfa['transition_function'].append([q_states, letter, q_to])

        self.dfa['start_states'] = []
        for state in self.nfa['start_states']:
            self.dfa['start_states'].append([state])
        self.dfa['final_states'] = []
        for states in self.dfa['states']:
            for state in states:
                if state in self.nfa['final_states'] and states not in self.dfa['final_states']:
                    self.dfa['final_states'].append(states)
        
        self.out_dfa(arqv)

    def load_nfa(self, nfa_arqv):
        self.nfa
        with open(nfa_arqv, 'r') as inpjson:
            self.nfa = json.loads(inpjson.read())

    def get_power_set(self,nfa_st):
        powerset = [[]]
        for i in nfa_st:
            for sub in powerset:
                powerset = powerset + [list(sub) + [i]]
        return powerset

    def out_dfa(self,aqrv):
        self.dfa
        with open(f"DFA\\t{aqrv}.json", 'w') as outjson:
            outjson.write(json.dumps(self.dfa, indent = 4))