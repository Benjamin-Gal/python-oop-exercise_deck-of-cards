from deck_of_cards import Card, Deck
import unittest


class CardTests(unittest.TestCase):
	def setUp(self):
		self.hq = Card("Q", "Hearts")

	def test_init_card(self):
		"""cards should have a suit and a value"""
		self.assertTrue(self.hq.value)
		self.assertTrue(self.hq.suit)

	def test_repr_card(self):
		"""repr should return a string of the form 'VALUE of SUIT'"""
		self.assertEqual(self.hq.__repr__(), "Q of Hearts")


class DeckTests(unittest.TestCase):
	def setUp(self):
		self.td = Deck()

	def test_init_deck(self):
		"""decks should have a cards attribute, which is a list with 52 elements"""
		self.assertTrue(self.td.cards)
		self.assertEqual(len(self.td.cards), 52)

	def test_repr_deck(self):
		"""repr should return a string of the form 'Deck of COUNT cards'"""
		self.assertEqual(self.td.__repr__(), f"Deck of {self.td.count()} cards")

	def test_count(self):
		"""count should return a count of the number of cards in the deck"""
		self.assertEqual(self.td.count(), 52)

	def test_shuffle_full_deck(self):
		"""shuffle should shuffle the deck if the deck is full"""
		self.assertEqual(self.td.count(), 52)
		self.td.shuffle()
		self.assertEqual(self.td.count(), 52)
		before = Deck()._deal(52)
		after = self.td._deal(52)
		self.assertNotEqual(before, after)

	def test_shuffle_not_full_deck(self):
		"""shuffle should throw a ValueError of the deck isn't full"""
		self.td.deal_card()
		with self.assertRaises(ValueError):
			self.td.shuffle()

	def test_deal_card(self):
		"""deal_card should deal a single card from the deck"""
		self.td.deal_card()
		self.assertEqual(self.td.count(), 51)

	def test_deal_hand(self):
		"""deal_hand should deal the number of cards passed into it"""
		num = 5
		self.td.deal_hand(num)
		self.assertEqual(self.td.count(), 52 - num)

	def test_deal_insufficient_cards(self):
		"""_deal should deal the number of cards left in the deck, if more cards are requested"""
		self.td._deal(53)
		self.assertEqual(self.td.count(), 0)

	def test_deal_no_cards(self):
		"""_deal should throw a ValueError if a deck is empty"""
		self.td._deal(52)
		with self.assertRaises(ValueError):
			self.td._deal(1)

	def test_deal_sufficient_cards(self):
		"""_deal should deal the number of cards specified, if possible"""
		num = 5
		self.assertEqual(len(self.td._deal(num)), num)


if __name__ == "__main__":
	unittest.main()
