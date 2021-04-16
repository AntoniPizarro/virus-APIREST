import pytest
from domain.deck import Deck

from services.db_engine import cards

@pytest.mark.deck
def test_init_1_mallet():
    all_cards = cards[:]
    deck = Deck(all_cards)
    
    player_mallet = deck.init_mallet()
    
    assert len(player_mallet) == 3
    assert len(deck.get_cards_available()) == 65

@pytest.mark.deck
def test_init_2_mallet():
    all_cards = cards[:]
    deck = Deck(all_cards)
    
    player_1_mallet = deck.init_mallet()
    player_2_mallet = deck.init_mallet()
    
    assert len(player_1_mallet) == 3
    assert len(player_2_mallet) == 3
    assert len(deck.get_cards_available()) == 62

@pytest.mark.deck
def test_get_cards_available():
    all_cards = cards[:]
    deck = Deck(all_cards)

    assert 68 == len(deck.get_cards_available())

@pytest.mark.deck
def test_discard_1_cards():
    all_cards = cards[:]
    deck = Deck(all_cards)

    player_mallet = deck.init_mallet()

    cards_discarted = [player_mallet[0]]
    player_mallet = deck.discard_cards(player_mallet, cards_discarted)

    assert len(player_mallet) == 3
    assert len(deck.get_cards_available()) == 65

@pytest.mark.deck
def test_discard_2_cards():
    all_cards = cards[:]
    deck = Deck(all_cards)

    player_mallet = deck.init_mallet()

    cards_discarted = [player_mallet[0], player_mallet[1]]
    player_mallet = deck.discard_cards(player_mallet, cards_discarted)

    assert len(player_mallet) == 3
    assert len(deck.get_cards_available()) == 65

@pytest.mark.deck
def test_discard_3_cards():
    all_cards = cards[:]
    deck = Deck(all_cards)

    player_mallet = deck.init_mallet()

    cards_discarted = [player_mallet[0], player_mallet[1], player_mallet[2]]
    player_mallet = deck.discard_cards(player_mallet, cards_discarted)

    assert len(player_mallet) == 3
    assert len(deck.get_cards_available()) == 65