# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
BallPos = [300,200]
BallVel = [random.randrange(120, 240), random.randrange(60, 180)]


# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global BallPos, BallVel # these are vectors stored as lists
    BallPos = [300,200]
    BallVel = [random.randrange(120, 240), random.randrange(60, 180)]
    if(direction == LEFT):
        BallVel[0] = -BallVel[0]
        BallVel[1] = -BallVel[1]
    else:
        BallVel[1] = -BallVel[1]
        BallVel[0] = BallVel[0]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    BallPos = [300,200]
    BallVel = [random.randrange(120, 240), random.randrange(60, 180)]
    if(score1 >= score2):
        spawn_ball(LEFT)
    elif(score1 < score2):
        spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if((BallPos[1] <= BALL_RADIUS) or (BallPos[1] >= HEIGHT - BALL_RADIUS)):
        BallVel[1] = -BallVel[1]
    if(BallPos[0] <= BALL_RADIUS):
        if(paddle1_pos-HALF_PAD_HEIGHT <= BallPos[1] and BallPos[1] <= paddle1_pos+HALF_PAD_HEIGHT):
            BallVel[0] = BallVel[0] * (-1.1)
            BallVel[1] = BallVel[1] * 1.1
        else:
            spawn_ball(RIGHT)
            score2 += 1
    elif(BallPos[0] >= WIDTH - BALL_RADIUS):
        if(paddle2_pos-HALF_PAD_HEIGHT <= BallPos[1] and BallPos[1] <= paddle2_pos+HALF_PAD_HEIGHT):
            BallVel[0] = BallVel[0] * (-1.1)
            BallVel[1] = BallVel[1] * 1.1
        else:
            spawn_ball(LEFT)
            score1 += 1
    BallPos[0] += BallVel[0] / 60
    BallPos[1] += BallVel[1] / 60
    # draw ball
    canvas.draw_circle(BallPos,20,1,"Green","White")
    # update paddle's vertical position, keep paddle on the screen
    if(HALF_PAD_HEIGHT <= paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel
    if(HALF_PAD_HEIGHT <= paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos += paddle2_vel
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT],   
                [HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],   
                PAD_WIDTH, "White")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT],   
                [WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT],   
                PAD_WIDTH, "White")  
    # determine whether paddle and ball collide    
    
    # draw scores
    canvas.draw_text(str(score1),(WIDTH / 4, 40), 40, "Yellow")  
    canvas.draw_text(str(score2),(3 *WIDTH / 4, 40), 40, "Blue")   
def keydown(key):
    global paddle1_vel, paddle2_vel
    if(key == simplegui.KEY_MAP["w"]):
        paddle1_vel = -4
    elif(key == simplegui.KEY_MAP['s']):
        paddle1_vel = 4
    elif(key == simplegui.KEY_MAP['down']):
        paddle2_vel = 4
    elif(key == simplegui.KEY_MAP['up']):
        paddle2_vel = -4
def keyup(key):
    global paddle1_vel, paddle2_vel
    if(key == simplegui.KEY_MAP["w"]):
        paddle1_vel = 0
    elif(key == simplegui.KEY_MAP['s']):
        paddle1_vel = 0
    elif(key == simplegui.KEY_MAP['down']):
        paddle2_vel = 0
    elif(key == simplegui.KEY_MAP['up']):
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",new_game,100)


# start frame
new_game()
frame.start()
