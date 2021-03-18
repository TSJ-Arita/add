def on_button_pressed_a():
    global Start
    Start = 1
    basic.show_string("R")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Start
    Start = 2
    basic.show_string("L")
input.on_button_pressed(Button.B, on_button_pressed_b)

Start = 0
方向 = 0
Start = 0

def on_forever():
    if Start == 1:
        pass
    else:
        pass
    basic.show_string("" + str((Start)))
basic.forever(on_forever)

def on_in_background():
    pass
control.in_background(on_in_background)
