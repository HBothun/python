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
    pairs = int()
    def __init__(self, name, cards, ask, pairs):
        self.name = name
        self.cards = cards
        self.ask =  ask
        self.pairs = pairs

def setUp():
    Players = []
    numPlayers = int(input('How many Players? \n'))
    for x in range(0, numPlayers):
        name = input('Player Name: ')
        Players.append(Player(name, [], '', 0))
    deckSize = int(input('How many Decks would you like? \n'))
    Deck = []
    x = 0
    while x < deckSize:
        for suit in Card.suits:
            for rank in Card.ranks:
                Deck.append(Card(rank, suit))
        x += 1
    return Players, Deck



def giveCard(player, Deck):
    newCard = random.choice(Deck)
    player.cards.append(newCard)
    Deck.remove(newCard)

def Deal(Players, Deck):
    cardsToDeal = 5
    for player in Players:
        player.cards = []
        giveCard(player, Deck)
    x = 1
    while x < cardsToDeal:
        for player in Players:
            giveCard(player, Deck)
        x += 1
    return Players

def castLine(player, Players, Deck):
    caught = False
    place = Players.index(player)
    Players.remove(player)
    bait = input('What are you fishing for? \n')
    for Player in Players:
        if bait in Player.cards:
            print(Player.name, 'has a', bait)
            Player.cards.remove(bait)
            caught = True
            player.pairs += 1
    if caught == False:
        print('No one had a', bait, 'which means you have to draw')
        giveCard(player, Deck)
    if caught == True:
        print('You now have', player.pairs, 'pairs')
    Players.insert(place, player)


Players, Deck = setUp()
print('There are', len(Deck), 'cards and', len(Players), 'players')
print('Dealing...')
Players = Deal(Players, Deck)

for Player in Players:
    while len(Player.cards) > 0:
        print(Player.name, 'its your turn.\nYou have', len(Player.cards), 'cards:')
        for card in Player.cards:
            print(card.rank, card.suit)
        if Player.cards.count(card) > 1:
            print('You have a pair of', card.rank, card.suit + 's')
            Player.pairs += 1
            Player.cards.remove(card)
        castLine(Player, Players, Deck)

