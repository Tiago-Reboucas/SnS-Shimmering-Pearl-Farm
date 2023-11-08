import pyautogui as gui
import time
import keyboard
import threading


# Wait time
def wait(t:float):
    time.sleep(t)


# ----------------Keys----------------
# ----- Movement -----
def w(u):
    if u==0: gui.keyDown("w")
    else: gui.keyUp("w")
def s(u):
    if u==0: gui.keyDown("s")
    else: gui.keyUp("s")
def a(u):
    global right
    if u==0: 
        gui.keyDown("a")
        right = False
    else: gui.keyUp("a")
def d(u):
    global right
    if u==0: 
        gui.keyDown("d")
        right = True
    else: gui.keyUp("d")

# ----- Items -----
def q():
    gui.keyDown("q")
    gui.keyUp("q")
    wait(0.1)
def e():
    gui.keyDown("e")
    gui.keyUp("e")
    wait(0.1)
def item():
    gui.keyDown("f")
    gui.keyUp("f")
    wait(0.3)

# ----- Jump/Dash/Use/Escape -----
def jump():
    gui.keyDown("space")
    gui.keyUp("space")
    wait(0.15)
def dash():
    gui.keyDown("shift")
    gui.keyUp("shift")
    wait(0.25)
def use():
    gui.keyDown("c")
    gui.keyUp("c")
    wait(0.25)
def escape():
    gui.keyDown("esc")
    gui.keyUp("esc")
    wait(0.1)

# ----- Attack/Evade -----
def attack():
    gui.keyDown("j")
    gui.keyUp("j")
    wait(0.7)
def evade():
    global right
    dash()
    wait(0.1)
    t = 0.3
    if right:
        a(0)
        wait(t)
        a(1)
    else:
        d(0)
        wait(t)
        d(1)

def attacknevade():
    attack()
    evade()
    attack()
    evade()
# --------------------------------


# Check mouse position
def check_mouse_position():
    time.sleep(3)
    print(gui.position())

    while True:
        again = input("Check positon again? (y/n) ")
        if again.lower() == 'y': return True
        if again.lower() == 'n': return False


def macro_start(event):
    global first, pause

    while True:
        if first:
            first = False
            event.wait()

        while True:
            # Teleport to sanctuary (when there is a 2nd player to teleport)
            wait(2)
            escape()
            escape()
            use()
            use()
            wait(0.75)
            event.wait()

            # Walk out sactuary
            a(0)
            wait(0.3)
            jump()
            dash()
            event.wait()

            # Walk before gap
            wait(0.7)
            jump()
            dash()
            event.wait()

            # Jump Gap
            wait(0.2)
            jump()
            dash()
            dash()
            event.wait()

            # Walk to the stairs
            wait(0.2)
            jump()
            dash()
            dash()
            wait(0.2)
            jump()
            dash()
            wait(0.1)
            a(1)
            event.wait()

            # Walk to the castle
            jump()
            d(0)
            wait(0.1)
            jump()
            dash()
            wait(1.5)
            jump()
            dash()
            d(1)
            event.wait()

            # #================================= EDIT HERE =================================#
            # ----- Activate drink/spell -----
            # Reaper char
            item()
            e()
            e()
            wait(0.5)
            item()
            wait(1)
            event.wait()

            # # Main Holly char
            # item()
            # e()
            # e()
            # e()
            # item()
            # q()
            # q()
            # q()
            # q()
            # q()
            # item()
            # e()
            # e()
            # wait(1)

            # Other car
            
            # ----- Move to fight -----
            d(0)
            wait(1)
            d(1)
            event.wait()

            # ----- Attack n Evade -----
            attack()
            event.wait()

            # #================================= END HERE =================================#

            # Example to use "attack" and "evade" functions
            # evade()
            # attack()
            # a(0)
            # wait(0.6)
            # a(1)
            # evade()

            break

        pause = True
        event.clear()
        event.wait()


# Pause/Resume Macro
def pause_resume():
    global pause, event

    if pause:
        pause = False
        event.set()
    else:
        pause = True
        event.clear()


# Main Execution
time_0 = time.time()
right = True

first = True
pause = True

event = threading.Event()
t = threading.Thread(target=macro_start, args=(event,))
t.start()

pause_hotkey = 'i'
keyboard.add_hotkey(pause_hotkey, pause_resume)

print(f"Press <{pause_hotkey.capitalize()}> to start macro.")