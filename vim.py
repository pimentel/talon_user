from talon.voice import Word, Context, Key, Rep, Str, press
from time import sleep

ctx = Context('vim', bundle='org.vim.MacVim')


def search_forward(m):
    press('/')
    w = str(m.dgndictation[0]._words[0])
    w = w.lower()
    Str(w)(None)
    press('return')


def search_reverse(m):
    press('?')
    w = str(m.dgndictation[0]._words[0])
    w = w.lower()
    Str(w)(None)
    press('enter')


def change_tab(m):
    window = str(m._words[1])
    press(window)
    press('g')
    press('t')


ctx.keymap({
    'trough': Key('ctrl-w'),
    'win (%s)+' % (' | '.join(map(str, range(10)))): change_tab,

    # insert mode
    # assumes you have AutoPair installed
    'insert code': ['```', Key('return')],

    # normal mode
    'vip': 'vip',
    'pain left': [Key('ctrl-w'), Key('h')],
    'pain right': [Key('ctrl-w'), Key('l')],
    'pain down': [Key('ctrl-w'), Key('j')],
    'pain up': [Key('ctrl-w'), Key('k')],
    'pain vertical': [Key('escape'), ':vsplit\n'],
    'pain horizontal': [Key('escape'), ':split\n'],
    'resize window': Key('ctrl-w ='),

    # vim-slime
    'send slime': [Key('ctrl-c'), Key('ctrl-c')],
    # normal mode
    'send function': ':call RSendFunctionSlime()\n',
    'send line': ':call RSendLineSlime()\n',
    'reset slime': Key('ctrl-c v'),

    # fzf.vim
    'list buffers': ':Buffers\n',
    'list files': ':Files\n',

    'crew <dgndictation>': search_forward,
    'trail <dgndictation>': search_reverse,

    'run (search | silver)': [':Ack! -S \'\'', Key('left')],
    'kill buffer': ':BD\n',
    # 'lead': ',',

    # phrases that get misrecognized commonly
    'champ obsess': 'Obsess',
})
