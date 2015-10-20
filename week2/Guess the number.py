# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math


NumRange = 100
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global NumRange
    # remove this when you add your code    
    if (NumRange == 100):
        range100()
    elif (NumRange == 1000):
        range1000()


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global RightNum,GuessTime,GuessInit,NumRange
    NumRange = 100
    RightNum = random.randrange(0,100)
    GuessTime = int(math.ceil(math.log(100,2)))
    GuessInit = GuessTime
    print "New game. The number is from 0 to 100."
    print "Number of remaining guess is",GuessTime
    print ""
    # remove this when you add your code    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global RightNum,GuessTime,GuessInit,NumRange
    NumRange = 1000
    RightNum = random.randrange(0,1000)
    GuessTime = int(math.ceil(math.log(1000,2)))
    GuessInit = GuessTime
    print "New game. The number is from 0 to 1000."
    print "Number of remaining guess is",GuessTime
    print ""
    
def input_guess(guess):
    # main game logic goes here	
    global RightNum,GuessTime
    guess = int(guess)
    print "Guess was",guess
    GuessTime -= 1
    print "Number of remaining guess is",GuessTime
    if(guess == RightNum):
        print "Correct!"
        print ""
        new_game()
    elif(guess > RightNum and GuessTime > 0):
        print "Lower!"
        print ""
    elif(guess < RightNum and GuessTime > 0):
        print "Higher!"
        print ""
    elif(guess != RightNum and GuessTime <= 0):
        print "You ran out of guesses","The number was",RightNum
        print ""
        new_game()
    # remove this when you add your code
    

    
# create frame
frame = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame
button1 = frame.add_button("range:[0, 100)",range100,200)
button2 = frame.add_button("range:[0, 1000)",range1000,200)
frame.add_input("Guess a number!",input_guess,200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
