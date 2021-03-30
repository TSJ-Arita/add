def R_turn():
    global Turn, _R_SPD
    if Turn == 0:
        Turn = 1
    else:
        if Turn < 8:
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, _L_SPD)
        Turn = Turn + 1
    _R_SPD = Turn
def chokobo1():
    music.set_tempo(tempo)
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
    music.play_tone(523, music.beat(BeatFraction.EIGHTH))
    music.play_tone(440, music.beat(BeatFraction.EIGHTH))
    music.play_tone(349, music.beat(BeatFraction.EIGHTH))
    music.play_tone(294, music.beat(BeatFraction.EIGHTH))
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

trace = 0
tempo = 0
Turn = 0
_L_SPD = 0
_R_SPD = 0
debug = 0
Start = 0
Start = 0
if debug:
    _R_SPD = 51
    _L_SPD = 38
else:
    _R_SPD = 255
    _L_SPD = 190
Turn = 0
strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
basic.show_string("" + str((Start)))
while Start == 0:
    basic.pause(1000)
basic.show_string("" + str((Start)))
strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
tempo = 39
music.set_tempo(tempo)
basic.pause(2000)

def on_forever():
    global trace, _L_SPD, Turn, _R_SPD
    trace = trace + 1
    if Start == 1:
        if maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1:
            if trace > 50:
                R_turn()
            else:
                _L_SPD = 30
        elif maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
            if trace > 50:
                trace = 0
            _L_SPD = 130
        else:
            Turn = 0
            _R_SPD = 255
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, _L_SPD)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, _R_SPD)
        _L_SPD = 190
    else:
        maqueen.motor_stop(maqueen.Motors.ALL)
basic.forever(on_forever)

def on_in_background():
    global tempo
    while tempo != 0:
        for index in range(2):
            chokobo1()
        chokobo2()
        tempo = tempo + 1
        music.set_tempo(tempo)
control.in_background(on_in_background)
