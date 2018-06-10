from talon.voice import Word, Context, Key, Rep, Str, press

ctx = Context('vim', bundle='org.vim.MacVim')

ctx.keymap({
    'pain left': [Key('ctrl-w'), Key('h')],
    'pain right': [Key('ctrl-w'), Key('l')],
    'pain down': [Key('ctrl-w'), Key('j')],
    'pain up': [Key('ctrl-w'), Key('k')],

    'pain vertical': [Key('escape'), ':vsplit\n'],
    'pain horizontal': [Key('escape'), ':split\n'],

    'run ack': ['Ack! \'\'', Key('left')],
    # 'lead': ',',
})
