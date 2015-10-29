# template for "Stopwatch: The Game"
import simplegui
# define global variables
TryTime = 0
SuccessTime = 0
AllTime = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if (t%600)/10 < 10:
        return str(t/600) + ':0' + str((t%600)/10) + '.' + str((t%600)%10)
    else:
        return str(t/600) + ':' + str((t%600)/10) + '.' + str((t%600)%10)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    TimerTicker.start()
    
def Stop():
    global TryTime,SuccessTime,AllTime
    if TimerTicker.is_running():
        TimerTicker.stop()
        TryTime += 1
        if (AllTime%10 == 0):
            SuccessTime += 1

def Reset():
    global TryTime,SuccessTime,AllTime
    AllTime = 0
    SuccessTime = 0
    TryTime = 0
    TimerTicker.stop()
    
# define event handler for timer with 0.1 sec interval
def tick():
    global AllTime
    AllTime += 1

# define draw handler
def draw(canvas):
    global AllTime,SuccessTime,TryTime
    canvas.draw_text(format(AllTime),[85,120],50,'White')
    canvas.draw_text(str(SuccessTime)+'/'+str(TryTime),[250,30],20,'Green')
    
# create frame
frame = simplegui.create_frame("Stopwatch Game",300,200)

# register event handlers
TimerTicker = simplegui.create_timer(100,tick)
frame.set_draw_handler(draw)
ButtonStart = frame.add_button("Start",Start,100)
ButtonStop = frame.add_button("Stop",Stop,100)
ButtonReset = frame.add_button("Reset",Reset,100)

# start frame
frame.start()

# Please remember to review the grading rubric
