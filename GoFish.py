import random

class Card:
    ranks=["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    suits=["Diamonds", "Clubs", "Hearts", "Spades"]
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class Player:
    name = str ()
    cards = []
    cash = int()
    ask = str()
    def __init__(self, name, cards, ask):
        self.name = name
        self.cards = cards
        self.ask =  ask

def setUp():
    Players = []
    numPlayers = int(input("How many Players? \n"))
    for x in range(0, numPlayers):
        name = input("Player Name: ")
        Players.append(Player(name, [], ""))
    deckSize = int(input("How many Decks would you like? \n"))
    Deck = []
    x = 0
    r, s = 0, 0
    while x < deckSize:
        for suit in Card.suits:
            for rank in Card.ranks:
                Deck.append(Card(r, s))
                r += 1
            s += 1
        x += 1
    return Players, Deck



def giveCard(player):
    newCard = random.choice(Deck)
    player.cards.append(newCard)
    Deck.remove(newCard)

def Deal(Players):
    cardsToDeal = 5
    for player in Players:
        player.cards = []
        giveCard(player)
    x = 1
    while x < cardsToDeal:
        for player in Players:
            giveCard(player)
        x += 1
    return Players

def castLine(player):
    bait = input("What are you fishing for? \n")
    for player in Players:
        if bait in player.cards:
            print(player.name + "has a" + bait)
        else
            print("Noone had a" + bait)

Players, Deck = setUp()
Players = Deal(Players)
print(len(Deck))
print(Players[0].cards)
# Players are set Cards are dealt

