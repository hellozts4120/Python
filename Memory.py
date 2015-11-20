# implementation of card game - Memory

import simplegui
import random


num = []
turn = 0
cur = 0
FirstCard = 0
LastCard = 0
# helper function to initialize globals
def new_game():
    global cur,num,turn,exposed
    cur = 0
    turn = 0
    num = range(0,8)
    num.extend(range(0,8))
    random.shuffle(num)
    exposed = [False,False,False,False,False,False,False,False,
             False,False,False,False,False,False,False,False,]
    
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global cur,num,exposed,turn,FirstCard,LastCard
    index = pos[0]/50
    exposed[index] = True
    if cur == 0:
        cur = 1
        FirstCard = index
    elif cur == 1:
        cur = 2
        LastCard = index
        turn += 1
    else:
        if (num[FirstCard] != num[LastCard]):
            exposed[FirstCard] = False
            exposed[LastCard] = False
        FirstCard = index
        cur = 1
        
        
                        
# cards are logically 50x100 pixels in size  
def draw(canvas):
    global exposed,num
    index = 0
    NowPos = 0
    label.set_text("Turns = " + str(turn))
    for i in num:
        if exposed[index]:
            canvas.draw_text(str(i), (NowPos, 100), 100, "White")
            canvas.draw_line((NowPos, 0), (NowPos, 100),
                                 1,"red")
        else:
            canvas.draw_polygon([(NowPos, 0), (NowPos, 100),
                                 (NowPos+50, 100),(NowPos+50, 0)],
                                1, "Green", "Green")
            canvas.draw_line((NowPos, 0), (NowPos, 100),
                                 1,"red")
        NowPos += 50
        index += 1


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric