import random

cards_test = [
    {"name": "corazón", "type" : "organ", "color" : "red"},
    {"name": "corazón", "type" : "organ", "color" : "red"},
    {"name": "corazón", "type" : "organ", "color" : "red"},
    {"name": "corazón", "type" : "organ", "color" : "red"},
    {"name": "corazón", "type" : "organ", "color" : "red"},
 
    {"name" : "estómago", "type" : "organ", "color" : "green"},
    {"name" : "estómago", "type" : "organ", "color" : "green"},
    {"name" : "estómago", "type" : "organ", "color" : "green"},
    {"name" : "estómago", "type" : "organ", "color" : "green"},
    {"name" : "estómago", "type" : "organ", "color" : "green"},
    
    {"name" : "cerebro", "type" : "organ", "color" : "blue"},
    {"name" : "cerebro", "type" : "organ", "color" : "blue"},
    {"name" : "cerebro", "type" : "organ", "color" : "blue"},
    {"name" : "cerebro", "type" : "organ", "color" : "blue"},
    {"name" : "cerebro", "type" : "organ", "color" : "blue"},
    
    {"name" : "hueso", "type" : "organ", "color" : "yellow"},
    {"name" : "hueso", "type" : "organ", "color" : "yellow"},
    {"name" : "hueso", "type" : "organ", "color" : "yellow"},
    {"name" : "hueso", "type" : "organ", "color" : "yellow"},
    {"name" : "hueso", "type" : "organ", "color" : "yellow"},
    
    {"name" : "comodín", "type" : "organ", "color" : "multicolor"},
    
    {"name" : "virus de corazón", "type" : "virus", "color" : "red"},
    {"name" : "virus de corazón", "type" : "virus", "color" : "red"},
    {"name" : "virus de corazón", "type" : "virus", "color" : "red"},
    {"name" : "virus de corazón", "type" : "virus", "color" : "red"},
 
    {"name" : "virus de estómago", "type" : "virus", "color" : "green"},
    {"name" : "virus de estómago", "type" : "virus", "color" : "green"},
    {"name" : "virus de estómago", "type" : "virus", "color" : "green"},
    {"name" : "virus de estómago", "type" : "virus", "color" : "green"},
    
    {"name": "virus de cerebro", "type" : "virus", "color" : "blue"},
    {"name": "virus de cerebro", "type" : "virus", "color" : "blue"},
    {"name": "virus de cerebro", "type" : "virus", "color" : "blue"},
    {"name": "virus de cerebro", "type" : "virus", "color" : "blue"},
    
    {"name" : "virus de hueso", "type" : "virus", "color" : "yellow"},
    {"name" : "virus de hueso", "type" : "virus", "color" : "yellow"},
    {"name" : "virus de hueso", "type" : "virus", "color" : "yellow"},
    {"name" : "virus de hueso", "type" : "virus", "color" : "yellow"},
    
    {"name" : "virus comodín", "type" : "virus", "color" : "multicolor"},
    
    {"name" : "medicamento de corazón", "type" : "medicine", "color" : "red"},
    {"name" : "medicamento de corazón", "type" : "medicine", "color" : "red"},
    {"name" : "medicamento de corazón", "type" : "medicine", "color" : "red"},
    {"name" : "medicamento de corazón", "type" : "medicine", "color" : "red"},
    
    {"name" : "medicamento de estómago", "type" : "medicine", "color" : "green"},
    {"name" : "medicamento de estómago", "type" : "medicine", "color" : "green"},
    {"name" : "medicamento de estómago", "type" : "medicine", "color" : "green"},
    {"name" : "medicamento de estómago", "type" : "medicine", "color" : "green"},
    
    {"name" : "medicamento de cerebro", "type" : "medicine", "color" : "blue"},
    {"name" : "medicamento de cerebro", "type" : "medicine", "color" : "blue"},
    {"name" : "medicamento de cerebro", "type" : "medicine", "color" : "blue"},
    {"name" : "medicamento de cerebro", "type" : "medicine", "color" : "blue"},
    
    {"name" : "medicamento de hueso", "type" : "medicine", "color" : "yellow"},
    {"name" : "medicamento de hueso", "type" : "medicine", "color" : "yellow"},
    {"name" : "medicamento de hueso", "type" : "medicine", "color" : "yellow"},
    {"name" : "medicamento de hueso", "type" : "medicine", "color" : "yellow"},
    
    {"name" : "medicamento comodín", "type" : "medicine", "color" : "multicolor"},
    {"name" : "medicamento comodín", "type" : "medicine", "color" : "multicolor"},
    {"name" : "medicamento comodín", "type" : "medicine", "color" : "multicolor"},
    {"name" : "medicamento comodín", "type" : "medicine", "color" : "multicolor"},
    
    {"name" : "contagio", "type" : "medicine", "color" : "contagion"},
    {"name" : "contagio", "type" : "medicine", "color" : "contagion"},
    
    {"name" : "robo", "type" : "medicine", "color" : "stole"},
    {"name" : "robo", "type" : "medicine", "color" : "stole"},
    {"name" : "robo", "type" : "medicine", "color" : "stole"},
    
    {"name" : "intercambio", "type" : "medicine", "color" : "exchange"},
    {"name" : "intercambio", "type" : "medicine", "color" : "exchange"},
    {"name" : "intercambio", "type" : "medicine", "color" : "exchange"},
    
    {"name" : "guante de látex", "type" : "medicine", "color" : "discard"},
    
    {"name" : "cambio de cuerpo", "type" : "medicine", "color" : "body_change"}
]

class Deck:
    '''
    'Crea una baraja y su gestión'
    '''

    def __init__(self, cards_available):
        self.cards_available = cards_available
    
    def get_cards_available(self):
        '''
        'Devuelve las cartas disponibles en la baraja'
        '''
        return self.cards_available

    def add_card_available(self, card):
        '''
        'Añade una carta a la baraja'
        '''
        self.cards_available.append(card)

    def init_mallet(self):
        '''
        'Devuelve un mazo eliminando las cartas escogidas'
        'de la baraja'
        '''
        cards_asociated = []
        cards = self.cards_available
        
        for i in range(3):
            if len(cards) > 2:
                ran = random.randrange(1, len(cards))
                card = cards[ran]
                cards_asociated.append(card)
                cards.remove(card)
        
        return cards_asociated
    
    def discard_cards(self, player_mallet, cards_discarted):
        '''
        'Recoge un mazo y le quita las cartas descartadas, añadiéndolas a la baraja'
        '''
        discard_cards_num = len(cards_discarted)
        
        for card in cards_discarted:
            player_mallet.remove(card)
            self.add_card_available(card)
        
        cards = self.get_cards_available()
        
        for i in range(discard_cards_num):
            ran = random.randrange(1, len(cards))
            card = cards[ran]
            player_mallet.append(card)
            cards.remove(card)

        return player_mallet