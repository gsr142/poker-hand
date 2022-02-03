import random
#build a deck of cards
card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['s', 'h', 'd', 'c']
deck = []
for suit in suits:
  for value in card_values:
    deck.append(value+suit)
#print(deck)
def deal(num_players=2):
  hand = random.sample(deck, 9)
  print("Player one has " + str(hand[0]) +str(hand[1]) + ".")
  print("Player two has " + str(hand[2]) +str(hand[3]) + ".")
  print("The flop cards are " + str(hand[4]) + str(hand[5]) + str(hand[6]) + ".")
  print("The turn card is " + str(hand[7]) + ".")
  print("The river card is " + str(hand[8]) + ".")
deal(2)
