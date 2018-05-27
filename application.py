from talon.voice import Context, Key

ctx = Context('application')

keymap = {
    'preffies': Key('cmd-,'),
    'marco': Key('cmd-f'),
    # 'marco super': Key('cmd-shift-f'),
    # 'run stacks': Key('ctrl-alt-d'),
}

ctx.keymap(keymap)
