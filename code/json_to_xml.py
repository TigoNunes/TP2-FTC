import json, random

class Converter_json_xml:
    def __init__(self, dfa, num_arq):
        self.dfa = self.open_dfa(dfa)
        self.state_id_map = {state: idx for idx, state in enumerate(self.dfa['states'])}
        self.dfa_to_xmj(num_arq)

    def open_dfa(self, arq_dfa):
        with open(arq_dfa, 'r') as dfa_arq:
            return json.load(dfa_arq)

    def dfa_to_xmj(self, num_arq):
        states = self.dfa['states']
        start_state = self.dfa['start_state']
        final_states = self.dfa['final_states']
        transitions = self.dfa['transition_function']

        xml_content = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
        xml_content += '<!--Created with custom script.-->\n'
        xml_content += '<structure>\n'
        xml_content += '    <type>fa</type>\n'
        xml_content += '    <automaton>\n'

        # Add states to the XML
        xml_content += '        <!--The list of states.-->\n'
        for state in states:
            state_id = self.state_id_map[state]
            x = random.uniform(100, 700)
            y = random.uniform(100, 400)
            xml_content += f'        <state id="{state_id}" name="{state}">\n'
            xml_content += f'            <x>{x}</x>\n'
            xml_content += f'            <y>{y}</y>\n'
            if state == start_state:
                xml_content += '            <initial/>\n'
            if state in final_states:
                xml_content += '            <final/>\n'
            xml_content += '        </state>\n'

        # Add transitions to the XML
        xml_content += '        <!--The list of transitions.-->\n'
        for transition in transitions:
            from_state, symbol, to_state = transition
            from_id = self.state_id_map[from_state]
            to_id = self.state_id_map[to_state]
            xml_content += '        <transition>\n'
            xml_content += f'            <from>{from_id}</from>\n'
            xml_content += f'            <to>{to_id}</to>\n'
            xml_content += f'            <read>{symbol}</read>\n'
            xml_content += '        </transition>\n'

        xml_content += '    </automaton>\n'
        xml_content += '</structure>\n'

        # Write to the output file
        with open(f"DFA\\xml\\t{num_arq}.xmj", 'w') as file:
            file.write(xml_content)