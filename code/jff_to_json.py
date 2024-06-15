import xmltodict, json

class Conversor_jff_regex:
    """Converte arquivo jff para um json"""
    def __init__(_self, xml, arqv):
        _self.arquivo = arqv
        _self._criar_json(xml)

    def _criar_json(_self, xml_file):

        with open(xml_file) as xml_file:
            data_dict = xmltodict.parse(xml_file.read())
            
            json_data = json.dumps(data_dict)
            
            with open(f"Regex/t{_self.arquivo}.json", "w") as json_file:
                json_file.write(json_data)
        
    def extrair_json(_self):
        """Recebe o json referente ao jff"""
        with open(f"Regex/t{_self.arquivo}.json", "r") as jf:
            inf = json.load(jf)
            return inf
