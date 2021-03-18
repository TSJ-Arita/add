input.onButtonPressed(Button.A, function () {
    Start = 1
    basic.showString("R")
})
input.onButtonPressed(Button.B, function () {
    Start = 2
    basic.showString("L")
})
let Start = 0
let 方向 = 0
Start = 0
basic.forever(function () {
    basic.showString("" + (Start))
    if (Start == 1) {
    	
    } else {
    	
    }
})
control.inBackground(function () {
	
})
