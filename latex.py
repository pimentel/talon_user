from talon.voice import Context, Key, Str, press

context = Context('latex')

# if true, insert a \ prefix by default
insert_prefix = True

def latex_on():
    global insert_prefix
    insert_prefix = True

def latex_off():
    global insert_prefix
    insert_prefix = False

keymap = {
    'latex on': lambda m: latex_on(),
    'latex off': lambda m: latex_off(),
}

greek_alphabet = {
    'alpha': 'alpha',
    'beta': 'beta',
    'epsilon': 'epsilon',
    'upsilon': 'upsilon',
    'lambda': 'lambda',
    'theta': 'theta',
    'sigma': 'sigma',
    'omega': 'omega',
    'gamma': 'gamma',
    'zeta': 'zeta',
    'new': 'nu',
    'tao': 'tao',
    'chai': 'chi',
    'row': 'rho',
    'sigh': 'psi',
    'fee': 'phi',
    'mew': 'mu',
    'pie': 'pi',
    'see': 'xi',
}

latex_symbols = {
    'backslash': 'backslash',
    'and': 'cap',
    'or': 'cup',
    'frak': 'frac',
    'int': 'int',
    'infinity': 'infty',
    'nabla': 'nabla',
    'prod': 'prod',
    'root': 'sqrt',
    '(simulate | simulates)': 'sim',
    'some': 'sum',
}

math_words = {
    'bays': 'bayes',
    # 'bayesian': 'bayesian',
    'dash': 'dash',
    'dot': 'dot',
    'dots': 'dots',
    'dureeshlay': 'dirichlet',
    'empirical': 'ecdf',
    'pusson': 'poisson',
    'some': 'sum',
}

def insert_normal(w, prefix):
    def internal(w):
        if insert_prefix and prefix:
            w = '\\%s' % w
        return Str(w)(None)
    return lambda m: internal(w)

def insert_capital(w, prefix):
    def internal(w):
        w = '%s%s' % (w[0].upper(), w[1:])
        if insert_prefix and prefix:
            w = '\\%s' % w
        return Str(w)(None)
    return lambda m: internal(w)


# upper and lower case versions of the greek alphabet
keymap.update({'math %s' % k: insert_normal(v, True) for k, v in greek_alphabet.items()})
keymap.update({'math cap %s' % k: insert_capital(v, True) for k, v in greek_alphabet.items()})

keymap.update({'math %s' % k: insert_normal(v, True) for k, v in latex_symbols.items()})
keymap.update({'word %s' % k: insert_normal(v, False) for k, v in math_words.items()})
keymap.update({'title %s' % k: insert_capital(v, False) for k, v in math_words.items()})
keymap.update({
    # a slash that is laying backwards
    'slay': '\\',
})

context.keymap(keymap)
