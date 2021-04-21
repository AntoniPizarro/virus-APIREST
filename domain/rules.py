class Rules:

    @staticmethod
    def check_body(body):
        '''
        Comprueba que un cuerpo tiene 4 cartas sanas para ganar la partida
        '''
        organs = 0
        
        for i in range(5):
            organ_key_name = "organ" + str(i + 1)
            effect_key_name = "effect" + str(i + 1)
            
            if body[organ_key_name] != {}:
                organs += 1
            if body[effect_key_name] != {} and body[effect_key_name]["type"] == "virus":
                organs -= 1

        if organs >= 4:
            return True
        else:
            return False
    
    @staticmethod
    def change_body(player_A, player_B):
        '''
        Cambia el cuerpo entre dos jugadores
        '''
        new_player_A = {
            "id" : player_A["id"],
            "name" : player_A["name"],
            "body" : player_A["body"],
            "mallet" : player_A["mallet"]
        }
        new_player_B = {
            "id" : player_B["id"],
            "name" : player_B["name"],
            "body" : player_B["body"],
            "mallet" : player_B["mallet"]
        }

        comodin_body = new_player_A["body"]
        
        new_player_A["body"] = new_player_B["body"]
        new_player_B["body"] = comodin_body
        
        return [new_player_A, new_player_B]
    
    @staticmethod
    def change_organ(body_A, body_B, organ_A, organ_B):
        '''
        Intercambia un órgano entre dos cuerpos
        '''
        for organ in body_A["organs"]:
            if body_A["organs"][organ] == organ_A:
                body_A["organs"][organ] = organ_B
        for organ in body_B["organs"]:
            if body_B["organs"][organ] == organ_B:
                body_B["organs"][organ] = organ_A
        
        return [body_A, body_B]

    @staticmethod
    def stole_organ(body_A, body_B, organ_to_stole):
        '''
        Roba un órgano de otro cuerpo
        '''
        template = {
            "organ" : {},
            "effect" : {},
            "inmune" : False
        }
        
        for organ in body_B["organs"]:
            if body_B["organs"][organ] == organ_to_stole:
                body_B["organs"][organ] = template
        for organ in body_A["organs"]:
            if body_A["organs"][organ] == template:
                body_A["organs"][organ] = organ_to_stole
        
        return [body_A, body_B]