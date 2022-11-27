def on_forever():
    pass
basic.forever(on_forever)
led.unplot(1, 30)
led.plot(10, 0)
radio.send_number(1)