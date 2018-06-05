from talon.voice import Word, Key, Context, Str
import string

terminals = ('com.apple.Terminal', 'com.googlecode.iterm2')
ctx = Context('terminal', func=lambda app, win: any(
    t in app.bundle for t in terminals))

keymap = {
    'cd': ['cd ; ls', Key('left'), Key('left'), Key('left'), Key('left')],
    'cd back': 'cd -; ls2\n',
    'cd develop': 'cd ~/dev; ls\n',
    'cd home': 'cd ~; ls\n',
    'cd up': 'cd ..; ls\n',

    'mux new': 'tmux new -s ',
    'mux attach': 'tmux attach -t ',
    'mux list': 'tmux ls\n',
    'mux horizontal': [Key('ctrl-b'), '\"'],
    'mux vertical': [Key('ctrl-b'), '%'],
    'mux leave': [Key('ctrl-b'), Key('d')],
    'mux scroll': [Key('ctrl-b'), Key('[')],

    'run list all': 'ls -lah\n',
    'run list long': 'ls -lh\n',
    'run get voice': ['git commit -m \' #talon\'', Key('alt-left'), Key('left')],
    'run bib': 'bibtex ',
    'run socks': 'ssh -D localhost:2020 ',
    'run grep': 'grep ',
    'run hawk': 'awk ',
    'run copy': 'cp -rf ',
    'run sink': 'rsync -ravh',
    'run see make': 'cmake ..',
    'run pseudo-': 'sudo ',
    'run said': 'sed ',
    'run remove': 'rm ',
    'run remove force': 'rm -rf ',
    'run top': 'htop\n',

    'run interactive': 'sdev -p pritch -t 2:00:00 -m 16GB',
    'run SQ': 'squeue -u $USER\n',

    # snakemake
    'shake dry': 'snakemake -p --dryrun\n',

    'pain left': [Key('ctrl-b'), Key('left')],
    'pain right': [Key('ctrl-b'), Key('right')],
    'pain up': [Key('ctrl-b'), Key('up')],
    'pain down': [Key('ctrl-b'), Key('down')],

    'snipple': [Key('ctrl-a'), Key('ctrl-k')],
    'kite': [Key('esc'), Key('d')],
    'trough': [Key('ctrl-w')],
    'tools oedipus': [Key('ctrl-x'), Key('ctrl-e')],

    'tools full-screen': Key('cmd-enter'),
    'tools exit': [Key('ctrl-c'), 'exit\n'],
    'window clear': Key('cmd-k'),

    'find here': ['find . -name \'\'', Key('left')],
    'open here': 'open .\n',
    'adam here': 'atom .\n',
    'run sq': 'squeue -u $USER\n',
    'run df': 'df -h\n',
    'run secure': 'ssh ',
}

ctx.keymap(keymap)
