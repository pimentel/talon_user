from talon.voice import Word, Key, Context, Str, press
from talon import ui
from time import sleep
import string

ctx = Context('Shortcat')

def run_shortcat(m):
    press('cmd-shift-space')
    sleep(0.1)
    if len(m._words) > 1:
        words = list(map(str, m.dgndictation[0]._words))
        words = ' '.join(words)
        print(words)
        Str(words)(None)
    else:
        press('.')

ctx.keymap({
    'shorty [<dgndictation>]': run_shortcat,
    })

