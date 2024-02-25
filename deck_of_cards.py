from random import shuffle


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:

    def __init__(self):
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        values = ("A", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "J", "Q", "K")
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self

    def _deal(self, card_to_deal):
        deck_size = self.count()
        actual = min([deck_size, card_to_deal])
        if deck_size == 0:
            raise ValueError("All cards have been dealt")
        card_dealt = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return card_dealt

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)


if __name__ == "__main__":
    d = Deck()
    print(d)
    print(d.count())
    print(d.shuffle())
    print(d.deal_card())
    # print(d.shuffle())
    print(d)
    print(d.deal_hand(5))
    print(d)
    print(d.deal_hand(42))
    print(d)
    print(d.deal_hand(5))
    print(d)
    # print(d.deal_card())
