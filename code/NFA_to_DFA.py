import json
from collections import deque

class Conversor_NFA_DFA:
    def __init__(self,nfa_arqv, num_arq:int):
        self.nfa = self.load_nfa(arq= nfa_arqv)
        self.dfa = {
            "states": [],
            "letters": [letter for letter in self.nfa['letters'] if letter != '$'],
            "transition_function": [],
            "start_state": '',
            "final_states": []
        }
        self.state_map = {}
        self.state_counter = 0

        self.NFA_to_DFA()
        

        self.return_dfa(n = num_arq)

    def load_nfa(self, arq):
        with open(arq, 'r') as nfa_arq:
            return json.load(nfa_arq)
    
    def NFA_to_DFA(self):
        start_state_closure = self.compute_epsilon_closure(self.nfa['start_states'][0])
        start_state = frozenset(start_state_closure)
        self.dfa['start_state'] = start_state
        self.dfa['states'].append(start_state)

        unmarked_states = deque([start_state])
        self.state_map[start_state] = "S0"
        self.state_counter = 1

        while unmarked_states:
            current_dfa_state = unmarked_states.popleft()

            for symbol in self.dfa['letters']:
                new_state = self.get_next_states(current_dfa_state, symbol)
                if new_state:
                    new_state_closure = set()
                    for state in new_state:
                        new_state_closure.update(self.compute_epsilon_closure(state))
                    new_state_closure = frozenset(new_state_closure)

                    if new_state_closure not in self.state_map:
                        self.state_map[new_state_closure] = f"S{self.state_counter}"
                        self.state_counter += 1
                        self.dfa['states'].append(new_state_closure)
                        unmarked_states.append(new_state_closure)

                    self.dfa['transition_function'].append((current_dfa_state, symbol, new_state_closure))

        for state in self.dfa['states']:
            if any(nfa_final in state for nfa_final in self.nfa['final_states']):
                self.dfa['final_states'].append(self.state_map[state])

        remapped_transition_function = []
        for t in self.dfa['transition_function']:
            from_state = self.state_map[t[0]]
            to_state = self.state_map[t[2]]
            remapped_transition_function.append((from_state, t[1], to_state))

        self.dfa['states'] = [self.state_map[state] for state in self.dfa['states']]
        self.dfa['start_state'] = self.state_map[self.dfa['start_state']]
        self.dfa['transition_function'] = remapped_transition_function
    
    def compute_epsilon_closure(self, state):
        closure = set()
        stack = [state]

        while stack:
            current_state = stack.pop()
            if current_state not in closure:
                closure.add(current_state)
                epsilon_transitions = [trans[2] for trans in self.nfa['transition_function'] if trans[0] == current_state and trans[1] == '$']
                stack.extend(epsilon_transitions)

        return closure
    
    def get_next_states(self, states, symbol):
        next_states = set()
        for state in states:
            transitions = [trans[2] for trans in self.nfa['transition_function'] if trans[0] == state and trans[1] == symbol]
            next_states.update(transitions)
        return next_states
    

    def return_dfa(self, n):
        with open(f"DFA\\json\\t{n}.json", 'w') as outjson:
            outjson.write(json.dumps(self.dfa, indent = 4))