from talon.voice import Word, Key, Context, Str
import string

ctx = Context('fetch', bundle = 'com.fetchsoftworks.Fetch')

ctx.keymap({
    'cd': Key('cmd-shift-g'),
    'cd up': Key('cmd-up'),
    'back': Key('cmd-['),
    'forward': Key('cmd-]'),
    'edit file': Key('cmd-j'),
    'open': Key('cmd-o'),
    })
