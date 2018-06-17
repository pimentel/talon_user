from talon import app, ui, clip
from talon.api import lib, ffi
from talon.audio import record, noise
from talon.engine import engine
from talon.voice import Word, Key, Context, Str, press

context = Context('homophones')

homophones = [
    ['1', 'one', 'won'],
    ['2', 'two', 'too', 'to'],
    ['3', 'three'],
    ['4', 'for', 'four', 'fore'],
    ['5', 'five'],
    ['6', 'six'],
    ['7', 'seven'],
    ['8', 'eight'],
    ['9', 'nine'],
    ["I'll", 'aisle', 'isle'],
    ['awful', 'offal'],
    ['ad', 'add'],
    ['ads', 'adds'],
    ['bald', 'balled', 'bawled'],
    ['ball', 'bawl'],
    ['band', 'banned'],
    ['base', 'bass'],
    ['basil', 'basal'],
    ['bear', 'bare'],
    ['break', 'brake'],
    ['breaks', 'brakes'],
    ['bread', 'bred'],
    ['but', 'butt'],
    ['by', 'buy', 'bye'],
    ['cash', 'cache'],
    ['cashed', 'cached'],
    ['Jean', 'gene'],
    ['jeans', 'genes'],
    ['meet', 'meat'],
    ['pool', 'pull'],
    ["there", "they're", "their"],
    ['where', 'wear'],
]

all_homophones = {}
for l in homophones:
    for word in l:
        all_homophones[word] = l

font = None
active_word_list = None

def run_homophones(vg, w, h):
    global font

    if active_word_list is None:
        return

    if font is None:
        font = lib.nvgCreateFont(vg, 'courier'.encode('utf8'), '/Library/Fonts/Courier New Bold.ttf'.encode('utf8'));

    x = w / 3
    y = h / 3
    lib.nvgBeginPath(vg)

    wt = w / 3
    ht = h / 3

    lib.nvgRect(vg, x, y, wt, ht)
    lib.nvgStrokeWidth(vg, 2)
    lib.nvgFillColor(vg, lib.nvgRGBA(0, 0, 0, 255))
    lib.nvgFill(vg)

    h = active_word_list
    h_string = ['%d . %s' % (i + 1, h[i]) for i in range(len(h))]
    h_string = '\n'.join(h_string)
    h_string = h_string.encode('utf8')

    lib.nvgFontFaceId(vg, font)
    lib.nvgFontSize(vg, 22)
    lib.nvgFillColor(vg, lib.nvgRGBA(255, 255, 255, 255))
    lib.nvgTextBox(vg, x + 20, y + 20, 400, h_string, ffi.NULL)

    lib.nvgStrokeWidth(vg, 3)

pick_context = Context('pick')

def close_homophones():
    pick_context.unload()
    app.unregister('overlay', run_homophones)

def make_selection(m):
    d = int(str(m._words[0]))
    w = active_word_list[d - 1]
    Str(w)(None)
    close_homophones()

def get_selection():
    with clip.capture() as s:
        press('cmd-c', wait=0)
    return s.get()

def raise_homophones(m):
    global pick_context
    global active_word_list


    # if hasattr(m, 'dgndictation') and len(m.dgndictation[0]._words) > 0:
    if len(m._words) > 1:
        if hasattr(m, 'dgndictation'):
            word = str(m.dgndictation[0]._words[0])
        else:
            # deal with the 1, 2, ... case
            word = str(m._words[1])
    else:
        word = get_selection()

    if word not in all_homophones:
        app.notify('homophones.py', '"%s" not in homophones list' % word)
        return

    active_word_list = all_homophones[word]

    app.register('overlay', run_homophones)
    valid_indices = range(len(active_word_list))

    keymap = {
        '0': lambda x: close_homophones(),
    }
    keymap.update({'%s' % (i + 1): make_selection for i in valid_indices})
    pick_context.keymap(keymap)
    pick_context.load()

keymap = {
    # Usage:
    # 'homophones word' to look up those homophones.
    # when the list pops up, say appropriate number or zero (leave and do nothing).
    # can also call 'homophones' without any arguments.
    # it will look at the selected text and look that up.
    'homophones [<dgndictation>]': raise_homophones,
    }
keymap.update({'homophones %d' % i : raise_homophones for i in range(10)})

context.keymap(keymap)

