from talon.voice import Context, Key

ctx = Context('slack', bundle='com.tinyspeck.slackmacgap')

keymap = {
    'channel': Key('cmd-k'),
    'channel up': Key('alt-up'),
    'channel down': Key('alt-down'),
    'insert command': ['``', Key('left')],
    'insert code': ['``````', Key('left left left'),
                    Key('shift-return'), Key('shift-return'), Key('up')],
}

ctx.keymap(keymap)
