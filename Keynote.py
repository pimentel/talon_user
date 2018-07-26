from talon.voice import Word, Context, Key, Rep, Str, press
from talon import applescript

context = Context('global_keynote')

DIRECTORY = '/Users/hjp/.talon/user'
UNLOAD_CONTEXT = ['case.py', 'editing.py', 'navigation.py', 'std.py',
                  'switcher.py', 'words.py']
IGNORE = '#IGNORE '


def load_context(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        lines = []
        for line in f:
            line = line.replace(IGNORE, '')
            lines.append(line)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(''.join(lines))


def unload_context(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        lines = []
        for line in f:
            line = IGNORE + line
            lines.append(line)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(''.join(lines))


def unload_all(discard):
    files = [DIRECTORY + '/' + f for f in UNLOAD_CONTEXT]
    print(files)
    for fname in files:
        unload_context(fname)


def load_all(discard):
    files = [DIRECTORY + '/' + f for f in UNLOAD_CONTEXT]
    for fname in files:
        load_context(fname)


mapping = {
    'semicolon': ';',
    'new-line': '\n',
    'new-paragraph': '\n\n',
}
punctuation = set('.,-!?')


def parse_word(word):
    word = str(word).lstrip('\\').split('\\', 1)[0]
    word = mapping.get(word, word)
    return word


def jump_slide(m):
    words = m.dgndictation[0]._words
    numbers = list(map(parse_word, words))
    numbers_map = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'for': '4',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    numbers = [numbers_map[n] for n in numbers]
    number = ''.join(numbers)
    applescript.run(r'''
tell application "Keynote"
	set target to item %s of (get slides of the front document)
	set current slide of the front document to target
end tell''' % number)


def last_slide(m):
    applescript.run(r'''
tell application "Keynote"
	set target to last item of (get slides of the front document)
	set current slide of the front document to target
end tell
''')


keymap = {
    'presentation mode on': unload_all,
    'presentation mode off': load_all,
}


context.keymap(keymap)

local_context = Context('local_keynote', bundle='com.apple.iWork.Keynote')

local_key_map = {
    'next': Key('right'),
    'last': Key('left'),
    'toggle presentation': Key('cmd-alt-p'),
    'slide <dgndictation> go': jump_slide,
    'slide last [go]': last_slide,
}

local_context.keymap(local_key_map)
