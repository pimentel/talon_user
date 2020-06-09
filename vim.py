from talon.voice import Word, Context, Key, Rep, Str, press
from time import sleep

ctx = Context('vim', bundle = 'org.vim.MacVim')


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
    'last file': [Key('escape'), Key('ctrl-^')],

    # insert mode
    # assumes you have AutoPair installed
    'insert code': ['```', Key('return')],

    # normal mode
    'vip': 'vip',
    'pain left': [Key('ctrl-w'), Key('h')],
    'pain right': [Key('ctrl-w'), Key('l')],
    'pain down': [Key('ctrl-w'), Key('j')],
    'pain up': [Key('ctrl-w'), Key('k')],
    'vertical split': [Key('escape'), ':vsplit\n'],
    'horizontal split': [Key('escape'), ':split\n'],
    'resize window': Key('ctrl-w ='),
    'left indent': '<<',
    'right indent': '>>',

    # vim-slime
    'send slime': [Key('ctrl-c'), Key('ctrl-c')],
    # normal mode
    'send function': ':call b:SlimeBlocksFunction()\n',
    'send markdown': ':call b:SlimeBlocksFenced()\n',
    'send line': ':SlimeSend\n',
    'configure slime': Key('ctrl-c v'),

    # fzf.vim
    'buffers': ':Buffers\n',
    'LS': ':Files\n',

    'crew <dgndictation>': search_forward,
    'trail <dgndictation>': search_reverse,

    'run (search | silver)': [':Ack! -S \'\'', Key('left')],
    'kill buffer': ':BD\n',

    # phrases that get misrecognized commonly
    'champ obsess': 'Obsess',
})
