input.onButtonPressed(Button.A, function () {
    Start = 1
    basic.showString("R")
})
input.onButtonPressed(Button.B, function () {
    Start = 2
    basic.showString("L")
})
let Start = 0
Start = 0
let strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.White))
basic.forever(function () {
    maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 255)
    basic.showString("" + (Start))
    if (Start == 1) {
    	
    } else {
    	
    }
})
control.inBackground(function () {
	
})
