import random

class Card:
    ranks=["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    suits=["Diamonds", "Clubs", "Hearts", "Spades"]
    value = int()
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        if self.rank == "Ace":
            self.value = 1
        elif self.rank == "Jack" or self.rank == "Queen" or self.rank == "King":
            self.value = 10
        elif type(self.rank) is int:
            if self.rank > 1 and self.rank < 11:
                self.value = self.ranks[self.rank-1]

class Player:
    name = str ()    
    cards = []
    score = int()
    cash = int()
    bet = int()
    insured = bool()
    dubDown = bool()
    isSplit = bool()    
    def __init__(self, name, cards, score, cash, bet, insured, dubDown, isSplit):
        self.name = name
        self.cards = cards
        self.score = score
        self.cash = cash
        self.bet =  bet
        self.insured = insured
        self.dubDown = dubDown
        self.isSplit = isSplit

def setUp():
    Players = []
    numPlayers = int(input("How many Players? \n"))
    Players.append(Player('Dealer', [], 0, 0, 0, False, False, False))
    for x in range(0,numPlayers):
        name = input("Player Name: ")
        Players.append(Player(name, [], 0, 5000, 0, False, False, False))
    return Players

def giveCard(player, show=True):
    newCard = Card(random.choice(Card.ranks),random.choice(Card.suits))
    player.cards.append(newCard)
    if show:
        print(player.name,"gets a", newCard.rank,"of", newCard.suit)
    return newCard   

def Deal(Players):
    Players[0].cards = []
    for player in Players[1:]:
        player.cards = []
        player.score = 0
        giveCard(player)
    giveCard(Players[0])  
    for player in Players[1:]:
        giveCard(player)
    giveCard(Players[0], show=False)
    checkScore(Players[0], score=False)
    print("Dealer gets a hidden card")
    return Players

def checkScore(player, cards=False, score=True): 
    player.score = 0
    for card in player.cards:
        player.score += card.value
        if cards:            
            print(card.rank, card.suit)
    if score:
        print(player.name, 'Score:', player.score)
    return player

def bust(player, show=True):    
    if player.score > 21:
        player.score = 0
        cont = False
        if show:
            print('You Busted!')
    else:
        cont = True
    return cont

def play(Players):
    i = 1
    for player in Players[1:]:
        player.dubDown == False
        print(player.name,"Turn")
        checkScore(player, cards=True, score=True)
        DoubleDown(player)
        didSplit = False
        if player.cards[0].value == player.cards[1].value:
            didSplit = offerSplit(player, Players, i)
        i += 1
        if didSplit == True:
            print(player.name, "turn")
            checkScore(player, cards=True)
        if player.dubDown == False:   
            choice = int(input("[1] Hit \n[2] Stay \n"))
            if choice == 2:
                pass
            elif choice == 1:
                newCard = giveCard(player)
                checkScore(player, cards=False, score=True)
                cont = bust(player)
                if cont:
                    if player.score != 21:
                        choice = int(input("[1] Hit \n[2] Stay \n"))
                    if choice == 2:
                        cont = False
                    elif choice == 1:        
                        while cont:            
                            newCard = giveCard(player)
                            print(newCard.rank, newCard.suit)
                            checkScore(player, cards=False, score=True)
                            cont = bust(player)
                            if cont == True:
                                choice = int(input("[1] Hit \n[2] Stay \n"))
                                if choice == 2:
                                    cont = False
        elif player.dubDown == True:
            giveCard(player)
            checkScore(player)
            bust(player)
            player.dubDown ==False
    return didSplit

def dealerCheck(Players):
    print(Players[0].name,"Shows thier Cards")
    checkScore(Players[0], cards=True)
    if Players[0].score == 21:
        for player in Players[1:]:
            if player.insured == True:
                print(player.name, "Has insurance and will be paid", (player.bet//2))
                player.cash += (player.bet//2)
                print(player.name, "has", player.cash)
    elif Players[0].score < 21:
        for player in Players[1:]:
            if player.insured == True:
                print(player.name, "Lost thier Insurance bet of", (player.bet//2))
                player.cash -= (player.bet//2)
                print(player.name, "has", player.cash)
    while Players[0].score <=17:
        giveCard(Players[0])
        checkScore(Players[0])
    if Players[0].score > 18:
        pass

def placeBets(Players):
    for player in Players[1:]:
        print(player.name)
        bet = int(input("Bet between 25 and 2500 \n"))
        player.bet = bet


def insurScan(Players):
    if Players[0].cards[0].value == 10 or Players[0].cards[0].value == 1:
        for player in Players[1:]:
            insure = int(input("Want Insurance? \n[1] Yes\n[2] No \n"))
            if insure == 1:
                player.insured = True
            else:
                player.insured = False

def DoubleDown(player):
    dubs = 0
    if player.score == 9 or player.score == 10 or player.score == 11:
        dubs = int(input("Wanna Double Down? \n[1] Yes \n[2] No \n"))
        if dubs == 1:
            player.bet = player.bet*2
            player.dubDown = True
    dubs = 0

def offerSplit(player, Players, i):
    split = int(input("Wanna Split your pair? \n[1] Yes \n[2] No \n"))
    if split == 1:
        i -+ 1
        didSplit = True
        splitHand = Player('SplitHand', [player.cards[1]], 0, 0, player.bet, False, False, True)
        Players.insert(i, splitHand)
        player.cards.remove(player.cards[1])
        giveCard(player)
        checkScore(player)
        giveCard(splitHand)
        checkScore(splitHand)
        print(splitHand.name, "Turn")
        splitChoice = int(input("[1] Hit \n[2] Stay \n"))
        if splitChoice == 1:
            newCard = giveCard(splitHand)
            checkScore(splitHand, cards=False, score=True)
            cont = bust(splitHand)
            if cont:
                if splitHand.score != 21:
                    splitChoice = int(input("[1] Hit \n[2] Stay \n"))
                if splitChoice == 2:
                    cont = False
                elif splitChoice == 1:        
                    while cont:            
                        newCard = giveCard(splitHand)
                        print(newCard.rank, newCard.suit)
                        checkScore(splitHand, cards=False, score=True)
                        cont = bust(splitHand)
                        if cont == True:
                            splitChoice = int(input("[1] Hit \n[2] Stay \n"))
                            if splitChoice == 2:
                                cont = False
            print('end of slipt turn')
        else:
            pass
    else:
        didSplit = False
    return didSplit
    
Players = setUp()
running = True
while running:
    placeBets(Players)
    Deal(Players)
    insurScan(Players)
    didSplit = play(Players)    
    dealerCheck(Players)
    cont = bust(Players[0], show=False)
    if cont == True:
        dBust = False
    elif cont == False:
        dBust = True
    for player in Players[1:]:        
        bet = player.bet       
        if player.score == 0:
            print(player.name, "Busted and lost thier bet of", bet)
            player.cash -= bet
            print(player.name, "has", player.cash)
        if player.score != 0:     
            print(player.name, "had", player.score, "And bet", bet)
            if dBust == True:
                print("The Dealer Busted")
                print(player.name, "wins", bet)
                player.cash += bet
                print(player.name, "has", player.cash)
            if dBust == False:
                diff = Players[0].score - player.score
                if diff == 0:
                    print(player.name, "Splits")
                    print(player.name, "keeps their bet")
                    print(player.name, "has", player.cash)
                elif diff <= -1:
                    print(player.name, "wins", bet)
                    player.cash += bet
                    print(player.name, "has", player.cash)
                elif diff >= 1:
                    print(player.name, "Lost", bet)
                    player.cash -= bet
                    print(player.name, "has", player.cash)
        if player.isSplit == True:
            subScore = player.cash
            i = int(Players.index(player) + 1)
            Players[i].cash += subScore
            print(player.name, "from", Players[i].name)
            print(Players[i].name, "has", Players[i].cash)

    loop = int(input('[1] Again \n\
[2] Quit \n'))
    if loop == 1:
        pass
    elif loop == 2:
        running = False
    else:
        running = False
print('Good Bye')