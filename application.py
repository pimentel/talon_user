from talon.voice import Context, Key

ctx = Context('application')

keymap = {
    'preffies': Key('cmd-,'),
    'marco': Key('cmd-f'),
}

ctx.keymap(keymap)
