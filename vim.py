from talon.voice import Word, Context, Key, Rep, Str, press

ctx = Context('vim', bundle='org.vim.MacVim')

ctx.keymap({
    'trough': Key('ctrl-w'),

    # assumes you are in insert mode
    'insert code': ['```', Key('return')],

    # assumes you are in normal mode
    'vip': 'vip',
    'pain left': [Key('ctrl-w'), Key('h')],
    'pain right': [Key('ctrl-w'), Key('l')],
    'pain down': [Key('ctrl-w'), Key('j')],
    'pain up': [Key('ctrl-w'), Key('k')],

    'pain vertical': [Key('escape'), ':vsplit\n'],
    'pain horizontal': [Key('escape'), ':split\n'],

    'run (back | ack)': [':Ack! -i \'\'', Key('left')],
    'fuzzy find': ':FZF\n',
    'kill buffer': ':BD',
    # 'lead': ',',
})
