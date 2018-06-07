from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from talon import ctrl
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string

alpha_alt = 'air bat cap die each fail gone harm ice jury crash look mad near odd pit quest red sun trap urge vest whale box yes zip'.split()
alnum = list(zip(alpha_alt, string.ascii_lowercase)) + [(str(i), str(i)) for i in range(0, 10)]

alpha = {}
alpha.update(dict(alnum))

extra_modifier_key_targets = {'left':'left','right':'right','up':'up','down':'down','minus':'-','plus':'+','(return|enter)':'enter','slash':'/','delete':'backspace','space':'space','index right':']','index left':'[','escape':'esc'}
for (k, v) in extra_modifier_key_targets.items():
    alnum.append((k, v))

alpha.update({'sky %s' % word: letter for word, letter in zip(alpha_alt, string.ascii_uppercase)})

alpha.update({'troll %s' % k: Key('ctrl-%s' % v) for k, v in alnum})
alpha.update({'coof %s' % k: Key('cmd-%s' % v) for k, v in alnum})
alpha.update({'shoff %s' % k: Key('cmd-shift-%s' % v) for k, v in alnum})
alpha.update({'alt %s' % k: Key('alt-%s' % v) for k, v in alnum})

alpha.update({'troll shift %s' % k: Key('ctrl-shift-%s' % v) for k, v in alnum})
alpha.update({'troll option %s' % k: Key('ctrl-alt-%s' % v) for k, v in alnum})
alpha.update({'command control %s' % k: Key('cmd-ctrl-%s' % v) for k, v in alnum})
alpha.update({'command option %s' % k: Key('cmd-alt-%s' % v) for k, v in alnum})
alpha.update({'option %s' % k: Key('alt-%s' % v) for k, v in alnum})
alpha.update({'option shift %s' % k: Key('alt-shift-%s' % v) for k, v in alnum})

mapping = {
    'semicolon': ';',
    'new-line': '\n',
    'new-paragraph': '\n\n',
}
punctuation = set('.,–!?')

token_replace = {
    'et cetera': 'etc',
    'e-mail': 'email',
    'I\\pronoun': 'I',
    'I\'m': 'I\'m',
    'I\'ve': 'I\'ve',
    'I\'d': 'I\'d',

    'Callisto': 'kallisto',
    'meta-\\\\meta': 'meta',
    'multi-\\\\multi': 'multi',

    'jean': 'gene',
    'jeans': 'genes',
}

prefix_mapping = set([
    'intron'
])

def parse_word(word):
    word = str(word)
    print('"', word, '"')
    if word in token_replace:
        word = token_replace.get(word)
    else:
        word = word.lower()
    word = word.lstrip('\\').split('\\', 1)[0]
    word = mapping.get(word, word)
    return word

def join_words(words, sep=' '):
    out = ''
    for i, word in enumerate(words):
        if (i > 0 and word not in punctuation) and word not in "'s":
            out += sep
        if word in "'s" and words[i - 1] in prefix_mapping:
            word = 's'
        out += word
    return out

def parse_words(m):
    return list(map(parse_word, m.dgndictation[0]._words))

def insert(s):
    Str(s)(None)

def text(m):
    insert(join_words(parse_words(m)))

def sentence_text(m):
    insert(join_words(capitalize(parse_words(m))))

def capitalize(words):
    return [words[0].capitalize()] + words[1:]

def word(m):
    text = join_words(list(map(parse_word, m.dgnwords[0]._words)))
    insert(text.lower())

def surround(by):
    def func(i, word, last):
        if i == 0: word = by + word
        if last: word += by
        return word
    return func

def rot13(i, word, _):
    out = ''
    for c in word.lower():
        if c in string.ascii_lowercase:
            c = chr((((ord(c) - ord('a')) + 13) % 26) + ord('a'))
        out += c
    return out

formatters = {
    'dunder': (True,  lambda i, word, _: '__%s__' % word if i == 0 else word),
    'cram':  (True,  lambda i, word, _: word if i == 0 else word.capitalize()),
    'snake':  (True,  lambda i, word, _: word if i == 0 else '_'+word),
    'smash':  (True,  lambda i, word, _: word),
    # spinal or kebab?
    'spine':  (True,  lambda i, word, _: word if i == 0 else '-'+word),
    'title':  (False, lambda i, word, _: word.capitalize()),
    # 'allcaps': (False, lambda i, word, _: word.upper()),
    'dubstring': (False, surround('"')),
    'string': (False, surround("'")),
    'padded': (False, surround(" ")),
    'rot thirteen':  (False, rot13),

    'pathway':  (True, lambda i, word, _: word if i == 0 else '/'+word),
    'dotsway':  (True, lambda i, word, _: word if i == 0 else '.'+word),
    'yellsnik':  (True, lambda i, word, _: word.capitalize() if i == 0 else '_'+word.capitalize()),
    # 'champ': (True, lambda i, word, _: word.capitalize() if i == 0 else " "+word),
    'criff': (True, lambda i, word, _: word.capitalize()),
    'yeller': (False, lambda i, word, _: word.upper()),
    'thrack': (False, lambda i, word, _: word[0:3]),
    'quattro': (False, lambda i, word, _: word[0:4]),
}

def FormatText(m):
    fmt = []
    for w in m._words:
        if isinstance(w, Word):
            fmt.append(w.word)
    words = parse_words(m)

    tmp = []
    spaces = True
    for i, word in enumerate(words):
        word = parse_word(word)
        for name in reversed(fmt):
            smash, func = formatters[name]
            word = func(i, word, i == len(words)-1)
            spaces = spaces and not smash
        tmp.append(word)
    words = tmp

    sep = ' '
    if not spaces:
        sep = ''
    Str(sep.join(words))(None)

def format_text(words, i, last_function, spaces):
    if (len(words) == 1):
        word = words[0]
        smash, func = formatters[name]
        word = func(i, word, False)
        spaces = spaces and not smash
        return word
    else:
        if words[0] in formatters:
            name = words[0]
            print('in the formatters', name)
            smash, func = formatters[name]
            spaces = spaces and not smash
            return func(format_text(words[1:len(words)], i + 1, func, spaces))
        else:
            result = last_function(words[0], i, False)
            sep = ' '
            if not spaces:
                sep = ''
            return sep.join([result, format_text(words[1:len(words)], i + 1, last_function, spaces)])


def FormatTextRecursive(m):
    # fmt = []
    # for w in m._words:
    #     if isinstance(w, Word):
    #         fmt.append(w.word)
    print(m.dgndictation[0]._words)
    # words = parse_words(m)
    # print(words)

    # format_text(words[1:len(words)], 0, )
    # Str(sep.join(words))(None)

ctx = Context('input')

keymap = {}
keymap.update(alpha)
keymap.update({
    # 'phrase <dgndictation> [over]': text,
    'go <dgndictation> [over]': text,
    'word <dgnwords>': word,

    'sentence <dgndictation> [over]': sentence_text,
    'sent <dgndictation> [over]': sentence_text,
    'champ <dgndictation> [over]': sentence_text,

    'comma <dgndictation> [over]': [', ', text],
    'period <dgndictation> [over]': ['. ', sentence_text],
    'more <dgndictation> [over]': [' ', text],

    '(%s)+ <dgndictation>' % (' | '.join(formatters)): FormatText,

    # 'delete': Key('backspace'),

    'slap': [Key('cmd-right enter')],
    # 'enter': Key('enter'),
    'shock': Key('enter'),
    # 'escape': Key('esc'),
    'risk': Key('esc'),
    'question [mark]': '?',
    'tilde': '~',
    '(bang | exclamation point)': '!',
    'dollar [sign]': '$',
    '(downscore | crunder)': '_',
    '(semi | semicolon)': ';',
    'colon': ':',
    'coalgap': ': ',
    'coal twice': '::',
    'ellipsis': '...',
    '(square | left square [bracket])': '[', '(rsquare | are square | right square [bracket])': ']',
    '(paren | left paren)': '(', '(rparen | are paren | right paren)': ')',
    '(brace | left brace)': '{', '(rbrace | are brace | right brace)': '}',
    '(curly)': '{', '(rcurly)': '}',
    '(angle | left angle | less than)': '<', '(rangle | are angle | right angle | greater than)': '>',

    '(star | asterisk)': '*',
    '(pound | hash [sign] | octo | thorpe | number sign)': '#',
    'percent [sign]': '%',
    'caret': '^',
    'at sign': '@',
    '(and sign | ampersand | amper)': '&',
    'pipe': '|',

    '(dubquote | double quote)': '"',
    'quote': "'",
    'triple quote': "'''",
    '(dot | period)': '.',
    'comma': ',',
    'swipe': ', ',
    'space': ' ',
    '[forward] slash': '/',
    'backslash': '\\',

    '(dot dot | dotdot)': '..',
    # 'cd': 'cd ',
    'cd talon home': 'cd {}'.format(TALON_HOME),
    'cd talon user': 'cd {}'.format(TALON_USER),
    'cd talon plugins': 'cd {}'.format(TALON_PLUGINS),

    'run make (durr | dear)': 'mkdir ',
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

    'run list': 'ls\n',
    'dot pie': '.py',
    # 'run make': 'make\n',
    'run jobs': 'jobs\n',

    'const': 'const ',
    'static': 'static ',
    'tip pent': 'int ',
    'tip bull': 'bool ',
    'tip char': 'char ',
    'tip byte': 'byte ',
    'tip pent 64': 'int64_t ',
    'tip you went 64': 'uint64_t ',
    'tip pent 32': 'int32_t ',
    'tip you went 32': 'uint32_t ',
    'tip pent 16': 'int16_t ',
    'tip you went 16': 'uint16_t ',
    'tip pent 8': 'int8_t ',
    'tip you went 8': 'uint8_t ',
    'tip size': 'size_t',
    'tip float': 'float ',
    'tip double': 'double ',

    'args': ['()', Key('left')],
    'index': ['[]', Key('left')],
    'block': ['{}', Key('left enter enter up tab')],
    'empty array': '[]',
    'empty dict': '{}',

    'state (def | deaf | deft)': 'def ',
    'state else if': 'elif ',
    'state if': 'if ',
    'state else if': [' else if ()', Key('left')],
    'state while': ['while ()', Key('left')],
    'state for': ['for ()', Key('left')],
    'state for': 'for ',
    'state switch': ['switch ()', Key('left')],
    'state case': ['case \nbreak;', Key('up')],
    # 'state goto': 'goto ',
    'state import': 'import ',
    'state class': 'class ',

    'state include': '#include ',
    'state include system': ['#include <>', Key('left')],
    'state include local': ['#include ""', Key('left')],
    'state type deaf': 'typedef ',
    'state type deaf struct': ['typedef struct {\n\n};', Key('up'), '\t'],

    'comment see': '// ',
    'comment py': '# ',



    'dunder in it': '__init__',
    'self taught': 'self.',
    'dickt in it': ['{}', Key('left')],
    'list in it': ['[]', Key('left')],
    'string utf8': "'utf8'",
    'state past': 'pass',

    'equals': '=',
    '(minus | dash)': '-',
    'long minus': '--',
    'plus': '+',
    'arrow': '->',
    'tinker': '`',

    # R specific
    'rambo': ' <- ',
    'our pipe': ' %>% ',

    'call': '()',
    'indirect': '&',
    'dereference': '*',
    '(op equals | assign)': ' = ',
    'op (minus | subtract)': ' - ',
    'op (plus | add)': ' + ',
    'op (times | multiply)': ' * ',
    'op divide': ' / ',
    'op mod': ' % ',
    '[op] (minus | subtract) equals': ' -= ',
    '[op] (plus | add) equals': ' += ',
    '[op] (times | multiply) equals': ' *= ',
    '[op] divide equals': ' /= ',
    '[op] mod equals': ' %= ',

    '(op | is) greater [than]': ' > ',
    '(op | is) less [than]': ' < ',
    '(op | is) equal': ' == ',
    '(op | is) not equal': ' != ',
    '(op | is) greater [than] or equal': ' >= ',
    '(op | is) less [than] or equal': ' <= ',
    '(op (power | exponent) | to the power [of])': ' ** ',
    'op and': ' && ',
    'op or': ' || ',
    '[op] (logical | bitwise) and': ' & ',
    '[op] (logical | bitwise) or': ' | ',
    '(op | logical | bitwise) (ex | exclusive) or': ' ^ ',
    '[(op | logical | bitwise)] (left shift | shift left)': ' << ',
    '[(op | logical | bitwise)] (right shift | shift right)': ' >> ',
    '(op | logical | bitwise) and equals': ' &= ',
    '(op | logical | bitwise) or equals': ' |= ',
    '(op | logical | bitwise) (ex | exclusive) or equals': ' ^= ',
    '[(op | logical | bitwise)] (left shift | shift left) equals': ' <<= ',
    '[(op | logical | bitwise)] (right shift | shift right) equals': ' >>= ',

    'shebang bash': '#!/bin/bash -u\n',

    'new window': Key('cmd-n'),
    'next window': Key('cmd-`'),
    'last window': Key('cmd-shift-`'),
    'next app': Key('cmd-tab'),
    'last app': Key('cmd-shift-tab'),
    'next tab': Key('ctrl-tab'),
    'new tab': Key('cmd-t'),
    'last tab': Key('ctrl-shift-tab'),

    'next space': Key('cmd-alt-ctrl-right'),
    'last space': Key('cmd-alt-ctrl-left'),

    # 'scroll down': [Key('down')] * 30,
    'page up': [Key('pageup')],
    # 'scroll up': [Key('up')] * 30,
    'page down': [Key('pagedown')],
    # 'scroll top': [Key('cmd-up')],
    # 'scroll bottom': [Key('cmd-down')],
})
ctx.keymap(keymap)
