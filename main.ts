input.onButtonPressed(Button.A, function () {
    Start = 1
    basic.showString("R")
})
maqueen.ltEvent(maqueen.Patrol1.PatrolLeft, maqueen.Voltage.High, function () {
	
})
input.onButtonPressed(Button.B, function () {
    Start = 2
    basic.showString("L")
})
let Start = 0
Start = 0
let strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.White))
basic.pause(2000)
let READERBUFFER_SIZE = 4
let WRITERBUFFER_SIZE = 4
let empty_list = [READERBUFFER_SIZE]
basic.forever(function () {
    maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 255)
    basic.showString("" + Start)
    if (Start == 1) {
    	
    } else {
    	
    }
})
control.inBackground(function () {
	
})
