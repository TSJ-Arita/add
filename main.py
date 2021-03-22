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

def chokobo():
    music.set_tempo(150)
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
    music.play_tone(330, music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(587, music.beat(BeatFraction.SIXTEENTH))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(659, music.beat(BeatFraction.SIXTEENTH))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(698, music.beat(BeatFraction.HALF))
    music.play_tone(659, music.beat(BeatFraction.SIXTEENTH))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
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
    music.play_tone(659, music.beat(BeatFraction.SIXTEENTH))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
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
_L_SPD = 0
_R_SPD = 0
Start = 0
Start = 1
debug = 1
if debug:
    _R_SPD = 51
    _L_SPD = 34
else:
    _R_SPD = 255
    _L_SPD = 170
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
