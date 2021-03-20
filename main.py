def on_button_pressed_a():
    global Start
    Start = 1
    basic.show_string("R")
input.on_button_pressed(Button.A, on_button_pressed_a)

def doSomething():
    pass

def on_button_pressed_b():
    global Start
    Start = 2
    basic.show_string("L")
input.on_button_pressed(Button.B, on_button_pressed_b)

Start = 0
Start = 1
_R_SPD = 51
_L_SPD = 34
strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
basic.show_string("" + str(Start))
basic.pause(2000)

def on_forever():
    global _L_SPD
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, _L_SPD)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, _R_SPD)
    if maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
        _L_SPD = 0
    else:
        _L_SPD = 34
basic.forever(on_forever)
