class Rules:

    @staticmethod
    def check_body(body):
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