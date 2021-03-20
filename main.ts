input.onButtonPressed(Button.A, function () {
    Start = 1
    basic.showString("R")
})
input.onButtonPressed(Button.B, function () {
    Start = 2
    basic.showString("L")
})
let Start = 0
Start = 1
let _R_SPD = 51
let _L_SPD = 34
let strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
basic.showString("" + Start)
basic.pause(2000)
basic.forever(function () {
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, _L_SPD)
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, _R_SPD)
    if (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
        _L_SPD = 0
    } else {
        _L_SPD = 34
    }
})
