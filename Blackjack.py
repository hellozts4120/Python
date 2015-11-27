# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
outcome1 = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        str = "Hand contains: "	# return a string representing the deck
        if(len(self.cards) == 0):
            return str
        for i in self.cards:
            str += i + ' '
        return str

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        AceNum = 0
        point = 0
        if(len(self.cards) == 0):
            return point
        for index in range(0,len(self.cards)):
            num = self.cards[index].get_rank()
            point += VALUES[num]
            if(num == 'A'):
                AceNum += 1
        if((AceNum > 0) and (point + 10 <= 21)):
            point += 10
        return point
   
    def draw(self, canvas, pos):
        curPos=pos[:]
        if(len(self.cards) == 0):
            return
        for i in range(0,len(self.cards)):
            self.cards[i].draw(canvas,curPos)
            curPos[0] += 100
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for i1 in SUITS:
            for i2 in RANKS:
                curCard = Card(i1,i2)
                self.cards.append(curCard)

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)
        
    def deal_card(self):
        outCard = self.cards.pop()
        return outCard	# deal a card object from the deck
    
    def __str__(self):
        str = "Deck contains: "	# return a string representing the deck
        if(len(self.cards) == 0):
            return str
        for i in self.cards:
            str += i + ' '
        return str


#define event handlers for buttons
def deal():
    global outcome, outcome1, in_play, dealer, player, deck, score

    player = Hand()
    dealer = Hand()
    deck = Deck()
    deck.shuffle()
    
    card1 = deck.deal_card()
    player.add_card(card1)
    card2 = deck.deal_card()
    dealer.add_card(card2)
    card3 = deck.deal_card()
    player.add_card(card3)
    card4 = deck.deal_card()
    dealer.add_card(card4)
    
    if(in_play):
        outcome = "You choose to give up!"
        outcome1 = "Hit or stand?"
        score -= 1
    else:
        outcome = "New game start!"
        outcome1 = "Hit or stand?"
    
    in_play = True

def hit():
    global in_play, score, outcome, outcome1	# replace with your code below
    if(in_play):
        curCard = deck.deal_card()
        player.add_card(curCard)
        if(player.get_value() > 21):
            outcome = "You have busted!"
            outcome1 = "New deal?"
            in_play = False
            score -= 1
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_play, score, outcome, outcome1	# replace with your code below
    if not in_play:
        return;
    if(player.get_value() > 21):
        outcome = "You have busted!"
        outcome1 = "New deal?"
        score -= 1
    else:
        while(dealer.get_value() < 17):
            curCard = deck.deal_card()
            dealer.add_card(curCard)
    if(dealer.get_value() > 21):
        outcome = "Dealer have busted!"
        outcome1 = "New deal?"
        score += 1
    else:
        if(player.get_value() > dealer.get_value()):
            outcome = "You win!"
            outcome1 = "New deal?"
            score += 1
        elif(player.get_value() < dealer.get_value()):
            outcome = "You lose!"
            outcome1 = "New deal?"
            score -= 1
        else:
            outcome = "Ties! Nobody wins!"
            outcome1 = "New deal?"
    in_play = False

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack",[50,100],50,"Red")
    canvas.draw_text(outcome,[230,225],24,"White")
    canvas.draw_text(outcome1,[230,425],24,"White")
    canvas.draw_text('Score = '+str(score), [450, 100], 24, "White")
    canvas.draw_text("Dealer:",[100,225],30,"Black")
    canvas.draw_text("Player:",[100,425],30,"Black")
    
 
    pos = [100,250]
    dealer.draw(canvas,pos)
    player.draw(canvas, [pos[0],pos[1]+200])
    
    if(in_play):
        canvas.draw_image(card_back, (36,48), (72,96), [136,298], CARD_BACK_SIZE)
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric