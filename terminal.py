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

    'cd talon home': 'cd ~/.talon; ls\n',
    'cd talon user': 'cd ~/.talon/user; ls\n',

    'armin': ' -',
    'longarmin': ' --',

    'mux new': 'tmux new -s ',
    'mux attach': 'tmux attach -t ',
    'mux list': 'tmux ls\n',
    'mux horizontal': [Key('ctrl-b'), '\"'],
    'mux vertical': [Key('ctrl-b'), '%'],
    'mux leave': [Key('ctrl-b'), Key('d')],
    'mux scroll': [Key('ctrl-b'), Key('[')],

    'run cat': 'cat ',
    'run less': 'less ',
    'run list': 'ls\n',
    'run list all': 'ls -lah ',
    'run list long': 'ls -lh ',
    'run get voice': ['git commit -am \' #talon\'', Key('alt-left'), Key('left')],
    'run bib': 'bibtex ',
    'run socks': 'ssh -D localhost:2020 ',
    'run grep': 'grep ',
    'run (back | ack)': 'ack ',
    'run hawk': 'awk ',
    'run copy': 'cp -rf ',
    'run sink': 'rsync -ravh',
    'run make': 'mkdir -p ',
    'run see make': 'cmake ..',
    'run pseudo-': 'sudo ',
    'run said': 'sed ',
    'run move': 'mv ',
    'run touch': 'touch ',
    'run remove': 'rm ',
    'run remove force': 'rm -rf ',
    'run top': 'htop\n',

    'run get': 'git ',
    'run get (R M | remove)': 'git rm ',
    'run get add': 'git add ',
    'run get bisect': 'git bisect ',
    'run get branch': 'git branch ',
    'run get checkout': 'git checkout ',
    'run get clone': 'git clone ',
    'run get commit': 'git commit ',
    'run get diff': 'git diff ',
    'run get fetch': 'git fetch ',
    'run get grep': 'git grep ',
    'run get in it': 'git init .',
    'run get log': 'git log ',
    'run get merge': 'git merge ',
    'run get move': 'git mv ',
    'run get pull': 'git pull ',
    'run get push': 'git push ',
    'run get rebase': 'git rebase ',
    'run get reset': 'git reset ',
    'run get show': 'git show ',
    'run get status': 'git status\n',
    'run get tag': 'git tag ',
    'run (them | vim)': 'vim ',

    'run brew': 'brew ',
    'run brew tap': 'brew tap ',
    'run brew search': 'brew search ',
    'run brew upgrade': 'brew upgrade ',
    'run brew update': 'brew update ',
    'run brew install': 'brew install ',
    'run cask install': 'brew cask install ',
    'run cask search': 'brew cask search ',

    'run stow': 'stow ',

    'run interactive': ['sdev -p pritch -t 2:00:00 -m 16GB', Key('left'), Key('left')],
    'run SQ': 'squeue -u $USER\n',

    # snakemake
    'shake dry': 'snakemake -p --dryrun\n',

    # assumes in tmux
    'pain left': [Key('ctrl-b'), Key('left')],
    'pain right': [Key('ctrl-b'), Key('right')],
    'pain up': [Key('ctrl-b'), Key('up')],
    'pain down': [Key('ctrl-b'), Key('down')],

    'snipple': [Key('ctrl-a'), Key('ctrl-k')],
    'kite': [Key('esc'), Key('d')],
    'trough': [Key('ctrl-w')],
    'tools oedipus': [Key('ctrl-x'), Key('ctrl-e')],

    # 'tools full-screen': Key('cmd-enter'),
    # 'tools exit': [Key('ctrl-c'), 'exit\n'],
    'window clear': Key('cmd-k'),

    'find here': ['find . -name \'\'', Key('left')],
    'open here': 'open .\n',
    'adam here': 'atom .\n',
    'run sq': 'squeue -u $USER\n',
    'run df': 'df -h\n',
    'run secure': 'ssh ',
}

ctx.keymap(keymap)
