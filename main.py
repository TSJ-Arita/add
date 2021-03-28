def chokobo1():
    music.set_tempo(39)
    music.play_tone(587, music.beat(BeatFraction.EIGHTH))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(494, music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.EIGHTH))
    music.play_tone(330, music.beat(BeatFraction.EIGHTH))
    music.play_tone(587, music.beat(BeatFraction.EIGHTH))
    music.play_tone(494, music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.EIGHTH))
    music.play_tone(494, music.beat(BeatFraction.EIGHTH))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.EIGHTH))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(494, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(440, music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.SIXTEENTH))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(392, music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(440, music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(392, music.beat(BeatFraction.SIXTEENTH))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(349, music.beat(BeatFraction.SIXTEENTH))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(349, music.beat(BeatFraction.EIGHTH))
    music.play_tone(392, music.beat(BeatFraction.SIXTEENTH))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(392, music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(494, music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(587, music.beat(BeatFraction.SIXTEENTH))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(659, music.beat(BeatFraction.SIXTEENTH))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(698, music.beat(BeatFraction.HALF))

def on_button_pressed_a():
    global Start
    Start = 1
    basic.show_string("R")
input.on_button_pressed(Button.A, on_button_pressed_a)

def chokobo2():
    music.play_tone(659, music.beat(BeatFraction.EIGHTH))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(523, music.beat(BeatFraction.EIGHTH))
    music.play_tone(440, music.beat(BeatFraction.EIGHTH))
    music.play_tone(349, music.beat(BeatFraction.EIGHTH))
    music.play_tone(440, music.beat(BeatFraction.EIGHTH))
    music.play_tone(523, music.beat(BeatFraction.EIGHTH))
    music.play_tone(659, music.beat(BeatFraction.EIGHTH))
    music.play_tone(587, music.beat(BeatFraction.EIGHTH))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(784, music.beat(BeatFraction.EIGHTH))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(587, music.beat(BeatFraction.HALF))
    music.play_tone(494, music.beat(BeatFraction.EIGHTH))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(523, music.beat(BeatFraction.EIGHTH))
    music.play_tone(440, music.beat(BeatFraction.EIGHTH))
    music.play_tone(349, music.beat(BeatFraction.EIGHTH))
    music.play_tone(349, music.beat(BeatFraction.EIGHTH))
    music.play_tone(440, music.beat(BeatFraction.EIGHTH))
    music.play_tone(523, music.beat(BeatFraction.EIGHTH))
    music.play_tone(494, music.beat(BeatFraction.SIXTEENTH))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(494, music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(523, music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(494, music.beat(BeatFraction.SIXTEENTH))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(440, music.beat(BeatFraction.SIXTEENTH))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(494, music.beat(BeatFraction.HALF))

def on_button_pressed_b():
    global Start
    Start = 2
    basic.show_string("L")
input.on_button_pressed(Button.B, on_button_pressed_b)

_L_SPD = 0
_R_SPD = 0
Start = 0
Start = 0
debug = 0
if debug:
    _R_SPD = 51
    _L_SPD = 38
else:
    _R_SPD = 255
    _L_SPD = 190
strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
basic.show_string("" + str(Start))
while Start == 0:
    basic.pause(1000)
basic.show_string("" + str(Start))
basic.pause(2000)

def on_forever():
    global _L_SPD, Start, _R_SPD
    if maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1:
        if Start == 1:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, _L_SPD)
        if Start == 2:
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, _R_SPD)
    if maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
        _L_SPD = 11
        Start = 2
    else:
        _L_SPD = 38
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1:
        _R_SPD = 17
        Start = 1
    else:
        _R_SPD = 51
basic.forever(on_forever)

def on_in_background():
    pass
control.in_background(on_in_background)
