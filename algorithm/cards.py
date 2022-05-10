import random
from .card import Card
import copy


class Cards:
    def __init__(self, cards: list[Card]) -> None:
        self.cards = cards

    def draw_cards(self, amount: int) -> list[Card]:
        # Checks if amount is valid
        if amount > len(self.cards):
            return []

        cards = copy.deepcopy(self.cards)

        picked = []
        for _ in range(amount):
            card = random.choice(cards)
            picked.append(card)
            cards.remove(card)
        return picked
