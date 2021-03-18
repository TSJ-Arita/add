input.onButtonPressed(Button.A, function () {
    basic.showString("R")
})
input.onButtonPressed(Button.B, function () {
    basic.showString("L")
})
basic.forever(function () {
    basic.showIcon(IconNames.Heart)
})
control.inBackground(function () {
	
})
