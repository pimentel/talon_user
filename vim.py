from talon.voice import Word, Context, Key, Rep, Str, press

ctx = Context('vim', bundle='org.vim.MacVim')

def search_forward(m):
    press('/')
    w = str(m.dgndictation[0]._words[0])
    Str(w)(None)
    press('return')

def search_reverse(m):
    press('?')
    w = str(m.dgndictation[0]._words[0])
    Str(w)(None)
    press('enter')

ctx.keymap({
    'trough': Key('ctrl-w'),

    # insert mode
    'insert code': ['```', Key('return')],

    # normal mode
    'vip': 'vip',
    'pain left': [Key('ctrl-w'), Key('h')],
    'pain right': [Key('ctrl-w'), Key('l')],
    'pain down': [Key('ctrl-w'), Key('j')],
    'pain up': [Key('ctrl-w'), Key('k')],
    'pain vertical': [Key('escape'), ':vsplit\n'],
    'pain horizontal': [Key('escape'), ':split\n'],
    'send pair': [Key('ctrl-c'), Key('ctrl-c')],

    # fzf.vim
    'list buffers': ':Buffers\n',
    'list files': ':Files\n',

    'crew <dgndictation>': search_forward,
    'trail <dgndictation>': search_reverse,

    'run (back | ack)': [':Ack! -i \'\'', Key('left')],
    'fuzzy find': ':FZF\n',
    'kill buffer': ':BD',
    # 'lead': ',',

    # phrases that get misrecognized commonly
    'champ obsess': 'Obsess',
})
