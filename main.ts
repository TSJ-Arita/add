maqueen.ltEvent(maqueen.Patrol1.PatrolRight, maqueen.Voltage.Low, function () {
    _R_SPD = 255
})
maqueen.ltEvent(maqueen.Patrol1.PatrolRight, maqueen.Voltage.High, function () {
    _R_SPD = 127
})
input.onButtonPressed(Button.A, function () {
    Start = 1
    basic.showString("R")
})
maqueen.ltEvent(maqueen.Patrol1.PatrolLeft, maqueen.Voltage.High, function () {
    _L_SPD = 127
})
input.onButtonPressed(Button.B, function () {
    Start = 2
    basic.showString("L")
})
maqueen.ltEvent(maqueen.Patrol1.PatrolLeft, maqueen.Voltage.Low, function () {
    _L_SPD = 255
})
let _L_SPD = 0
let _R_SPD = 0
let Start = 0
Start = 0
_R_SPD = 255
_L_SPD = 255
let strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.Red))
basic.pause(2000)
basic.forever(function () {
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, _R_SPD)
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, _L_SPD)
    basic.showString("" + Start)
    if (Start == 1) {
    	
    } else {
    	
    }
})
control.inBackground(function () {
	
})
