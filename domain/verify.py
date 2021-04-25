class Verify:

    @staticmethod
    def ver_virus_color(organs):
        '''
        'Comprueba que cada órgano tiene el efecto
        'correspondientes al color del órgano
        '''
        for organ in organs:
            if organs[organ]["effect"] == {} or organs[organ]["effect"]["color"] == organs[organ]["organ"]["color"] or organs[organ]["effect"]["color"] == "multicolor":
                continue
            else:
                return False
        return True
    
    @staticmethod
    def can_be_inmune(organ):
        if (organ["organ"] == {}
        or organ["effect"] == {}
        or (organ["organ"]["color"] != organ["effect"]["color"]
        and organ["effect"]["color"] != "multicolor"
        and organ["organ"]["color"] != "multicolor")
        or organ["effect"]["type"] != "medicine"):
            return False
        else:
            return True