class Verify:

    @staticmethod
    def ver_virus_color(organs):
        '''
        'Comprueba que cada órgano tiene el efecto
        'correspondientes al color del órgano
        '''
        for organ in organs:
            if organs[organ]["effect"] != {} or organs[organ]["effect"]["color"] == organs[organ]["organ"]["color"] or organs[organ]["effect"]["color"] == "multicolor":
                return True
            else:
                return False