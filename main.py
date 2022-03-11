def on_button_pressed_a():
    global 我出拳
    我出拳 = 1
    basic.show_icon(IconNames.SCISSORS)
input.on_button_pressed(Button.A, on_button_pressed_a)

def 設定初值():
    global 我出拳, 對手出拳
    basic.show_arrow(ArrowNames.NORTH)
    我出拳 = 0
    對手出拳 = randint(1, 3)
def 比輸贏():
    if 我出拳 == 對手出拳:
        basic.show_icon(IconNames.DUCK)
    elif 我出拳 == 1 and 對手出拳 == 3:
        basic.show_icon(IconNames.HAPPY)
    elif 我出拳 == 2 and 對手出拳 == 1:
        basic.show_icon(IconNames.HAPPY)
    elif 我出拳 == 3 and 對手出拳 == 2:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.SAD)

def on_button_pressed_ab():
    global 我出拳
    我出拳 = 3
    basic.show_icon(IconNames.SQUARE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global 我出拳
    我出拳 = 2
    basic.show_icon(IconNames.SMALL_DIAMOND)
input.on_button_pressed(Button.B, on_button_pressed_b)

對手出拳 = 0
我出拳 = 0
設定初值()

def on_forever():
    serial.write_number(對手出拳)
    while 我出拳 != 0:
        比輸贏()
        basic.pause(3000)
        設定初值()
basic.forever(on_forever)
