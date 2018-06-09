import time
from talon import ctrl, tap
from talon.voice import Context

ctx = Context('mouse')

x, y = ctrl.mouse_pos()
mouse_history = [(x, y, time.time())]
force_move = None

def click_pos(m):
    word = m._words[0]
    start = (word.start + min((word.end - word.start) / 2, 0.100)) / 1000.0
    diff, pos = min([(abs(start - pos[2]), pos) for pos in mouse_history])
    return pos[:2]

def mouse_drag(m):
    x, y = click_pos(m)
    ctrl.mouse_click(x, y, down=True)

def mouse_release(m):
    x, y = click_pos(m)
    ctrl.mouse_click(x, y, up=True)

def command_click(m):
    ctrl.key_press('cmd', down = True)
    ctrl.mouse_click(button = 0)
    ctrl.key_press('cmd', up = True)

keymap = {
    'righty': lambda x: ctrl.mouse_click(button = 1),
    'click': lambda x: ctrl.mouse_click(button = 0),
    'command click': command_click,
    'dubclick': lambda x: ctrl.mouse_click(button = 0, times = 2, wait = 16000),
    'tripclick': lambda x: ctrl.mouse_click(button = 0, times = 3, wait = 16000),
    'drag': mouse_drag,
    'release': mouse_release,
}
ctx.keymap(keymap)
