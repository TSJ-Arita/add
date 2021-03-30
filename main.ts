function R_turn () {
    if (Turn == 0) {
        Turn = 1
    } else {
        if (Turn < 8) {
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, _L_SPD)
        }
        Turn = Turn + 1
    }
    _R_SPD = Turn
}
function chokobo1 () {
    music.setTempo(tempo)
    music.playTone(587, music.beat(BeatFraction.Eighth))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(494, music.beat(BeatFraction.Eighth))
    music.playTone(392, music.beat(BeatFraction.Eighth))
    music.playTone(330, music.beat(BeatFraction.Eighth))
    music.playTone(587, music.beat(BeatFraction.Eighth))
    music.playTone(494, music.beat(BeatFraction.Eighth))
    music.playTone(392, music.beat(BeatFraction.Eighth))
    music.playTone(494, music.beat(BeatFraction.Eighth))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(392, music.beat(BeatFraction.Eighth))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(494, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(440, music.beat(BeatFraction.Eighth))
    music.playTone(392, music.beat(BeatFraction.Sixteenth))
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.playTone(392, music.beat(BeatFraction.Sixteenth))
    music.playTone(440, music.beat(BeatFraction.Sixteenth))
    music.playTone(392, music.beat(BeatFraction.Sixteenth))
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.playTone(349, music.beat(BeatFraction.Sixteenth))
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.playTone(392, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(349, music.beat(BeatFraction.Eighth))
    music.playTone(392, music.beat(BeatFraction.Sixteenth))
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.playTone(392, music.beat(BeatFraction.Sixteenth))
    music.playTone(494, music.beat(BeatFraction.Sixteenth))
    music.playTone(587, music.beat(BeatFraction.Sixteenth))
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.playTone(659, music.beat(BeatFraction.Sixteenth))
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.playTone(698, music.beat(BeatFraction.Half))
}
input.onButtonPressed(Button.A, function () {
    Start = 1
    basic.showString("R")
})
function chokobo2 () {
    music.playTone(659, music.beat(BeatFraction.Eighth))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(523, music.beat(BeatFraction.Eighth))
    music.playTone(440, music.beat(BeatFraction.Eighth))
    music.playTone(349, music.beat(BeatFraction.Eighth))
    music.playTone(440, music.beat(BeatFraction.Eighth))
    music.playTone(523, music.beat(BeatFraction.Eighth))
    music.playTone(659, music.beat(BeatFraction.Eighth))
    music.playTone(587, music.beat(BeatFraction.Eighth))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(784, music.beat(BeatFraction.Eighth))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(587, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(494, music.beat(BeatFraction.Eighth))
    music.playTone(523, music.beat(BeatFraction.Quarter))
    music.playTone(440, music.beat(BeatFraction.Eighth))
    music.playTone(349, music.beat(BeatFraction.Eighth))
    music.playTone(294, music.beat(BeatFraction.Eighth))
    music.playTone(349, music.beat(BeatFraction.Eighth))
    music.playTone(440, music.beat(BeatFraction.Eighth))
    music.playTone(523, music.beat(BeatFraction.Eighth))
    music.playTone(494, music.beat(BeatFraction.Sixteenth))
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.playTone(494, music.beat(BeatFraction.Sixteenth))
    music.playTone(523, music.beat(BeatFraction.Sixteenth))
    music.playTone(494, music.beat(BeatFraction.Sixteenth))
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.playTone(440, music.beat(BeatFraction.Sixteenth))
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.playTone(494, music.beat(BeatFraction.Half))
}
function chokobo3 () {
    music.playTone(659, music.beat(BeatFraction.Eighth))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(523, music.beat(BeatFraction.Eighth))
    music.playTone(440, music.beat(BeatFraction.Eighth))
    music.playTone(349, music.beat(BeatFraction.Eighth))
    music.playTone(440, music.beat(BeatFraction.Eighth))
    music.playTone(523, music.beat(BeatFraction.Eighth))
    music.playTone(659, music.beat(BeatFraction.Eighth))
    music.playTone(587, music.beat(BeatFraction.Eighth))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(784, music.beat(BeatFraction.Eighth))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(587, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(494, music.beat(BeatFraction.Eighth))
    music.playTone(440, music.beat(BeatFraction.Sixteenth))
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.playTone(440, music.beat(BeatFraction.Sixteenth))
    music.playTone(392, music.beat(BeatFraction.Sixteenth))
    music.playTone(440, music.beat(BeatFraction.Sixteenth))
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.playTone(392, music.beat(BeatFraction.Sixteenth))
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.playTone(440, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(392, music.beat(BeatFraction.Eighth))
    music.playTone(440, music.beat(BeatFraction.Sixteenth))
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.playTone(440, music.beat(BeatFraction.Sixteenth))
    music.playTone(494, music.beat(BeatFraction.Sixteenth))
    music.playTone(523, music.beat(BeatFraction.Sixteenth))
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.playTone(587, music.beat(BeatFraction.Sixteenth))
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.playTone(659, music.beat(BeatFraction.Sixteenth))
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(740, music.beat(BeatFraction.Quarter))
}
input.onButtonPressed(Button.B, function () {
    Start = 2
    basic.showString("L")
})
let trace = 0
let tempo = 0
let Turn = 0
let _L_SPD = 0
let _R_SPD = 0
let debug = 0
let Start = 0
Start = 0
if (debug) {
    _R_SPD = 51
    _L_SPD = 38
} else {
    _R_SPD = 255
    _L_SPD = 190
}
Turn = 0
let strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
basic.showString("" + (Start))
while (Start == 0) {
    basic.pause(1000)
}
basic.showString("" + (Start))
strip.showColor(neopixel.colors(NeoPixelColors.Blue))
tempo = 39
music.setTempo(tempo)
basic.pause(2000)
basic.forever(function () {
    trace = trace + 1
    if (Start == 1) {
        if (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1) {
            if (trace > 50) {
                R_turn()
            } else {
                _L_SPD = 30
            }
        } else if (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
            if (trace > 50) {
                trace = 0
            }
            _L_SPD = 130
        } else {
            Turn = 0
            _R_SPD = 255
        }
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, _L_SPD)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, _R_SPD)
        _L_SPD = 190
    } else {
        maqueen.motorStop(maqueen.Motors.All)
    }
})
control.inBackground(function () {
    while (tempo != 0) {
        for (let index = 0; index < 2; index++) {
            chokobo1()
        }
        chokobo2()
        chokobo3()
        tempo = tempo + 1
        music.setTempo(tempo)
    }
})
