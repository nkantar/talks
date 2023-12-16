from adafruit_circuitplayground.express import cpx


COLORS = (
    (0, 255, 0),  # green
    (255, 0, 0),  # red
)


cpx.pixels.brightness = 0.01


while True:
    with open("state") as state_file:
        state = int(state_file.readline())
        color = COLORS[state]
        cpx.pixels.fill(color)
