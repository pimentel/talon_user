from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
import string

alpha_alt = 'air bat cap die each fail gone harm sit jury crash look mad '\
    'near odd per quest red soon trap urge vest whale box yes zip'.split()
alnum = list(zip(alpha_alt, string.ascii_lowercase)) + \
    [(str(i), str(i)) for i in range(0, 10)]
alpha = {}

alpha.update(dict(alnum))

# these help in vim
alpha_up = {
    'gate': 'G',
    'viz.': 'V',
}

case_state = False


def insert_character(m):
    c = alpha.get(str(m._words[0]))
    if case_state:
        press(c.upper())
    else:
        press(c)


def case_upper(discard):
    global case_state
    case_state = True


def case_down(discard):
    global case_state
    case_state = False


context = Context('case')

keymap = {
    'upstate': case_upper,
    'downstate': case_down,
}

keymap.update({'%s' % k: insert_character for k in alpha})
keymap.update({'%s' % k: '%s' % v for k, v in alpha_up.items()})

context.keymap(keymap)
