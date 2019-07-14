import browser
from browser import document, window

moving = document["rot15"]
x = 0
dx = 3
run = None


def change(event):
    if event.keyCode == 39:
        global run
        if run is None:
            # start animation
            animloop(1)
        else:
            # stop animation
            window.cancelAnimationFrame(run)
            run = None


document.bind("keydown", change)


def render():
    global x, dx
    moving.style.transform = "translate({}px,0)".format(x)
    x += dx
    if x > document["zone15"].offsetWidth - moving.offsetWidth:
        dx = -dx
        moving.html = "&#9668;"  # left triangle
    elif x <= 0:
        dx = -dx
        moving.html = "&#9658;"  # right triangle


def animloop(t):
    global run
    run = window.requestAnimationFrame(animloop)
    render()