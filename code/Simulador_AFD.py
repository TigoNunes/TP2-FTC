import json

class Dfa_Simulator:
    def __init__(self, dfa_json_filename):
        with open(dfa_json_filename, 'r') as file:
            self.dfa = json.load(file)

    def simulate(self, input_string):
        current_state = self.dfa['start_state']
        transitions = self.dfa['transition_function']
        
        # Create a dictionary for quick lookup of transitions
        transition_dict = {}
        for (from_state, symbol, to_state) in transitions:
            if from_state not in transition_dict:
                transition_dict[from_state] = {}
            transition_dict[from_state][symbol] = to_state
        
        for symbol in input_string:
            if symbol in transition_dict.get(current_state, {}):
                current_state = transition_dict[current_state][symbol]
            else:
                return False

        return current_state in self.dfa['final_states']
