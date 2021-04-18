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
    def change_organ(body_A, body_b, organ_A, organ_B):
        comodin = organ_A
        for organ_body_A in body_A["organs"]:
            if organ_body_A["organ"] == organ_A:
                for organ_body_B in body_b["organs"]:
                    if organ_body_B["organ"] == organ_B:
                        organ_body_B["organ"] = comodin