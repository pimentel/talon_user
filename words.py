from talon.voice import Context, Key

ctx = Context('words')

keymap = {
    'word queue': 'queue',
    'word eye': 'eye',
    'word bson': 'bson',
    'word iter': 'iter',

    'word no': 'null',
    'yeller no': 'NULL',

    'word dup': 'dup',
    'word streak': ['streq()', Key('left')],
    'word printf': 'printf',
    'word (dickt | dictionary)': 'dict',
    'word shell': 'shell',
    'word get': 'git',
    'word get hub': 'github',
    'word them': 'vim',
    'word vim': 'vim',

    'word stood in': 'stdin',
    'word stood out': 'stdout',
    'word stood err': 'stderr',
    'word write': 'write',
    'word linux': 'linux',

    'shrink command': 'cmd',
    'shrink control': 'ctrl',
    'shrink parameter': 'param',
    'shrink parameters': 'params',

    'title shake file': 'Snakefile',
    'word shake make': 'snakemake',
    'word latex make': 'latexmk',
    'word seek T K': 'seqtk',
    'word numpy': 'numpy',

    'word adam': 'atom',
    'title adam': 'Atom',

    # names
    'word wife': 'puente',
    'title wife': 'Puente',
    'word son': 'avi',
    'title son': 'Avi',
    'word kyle': 'lior',
    'word bays': 'bayes',
    'title bays': 'Bayes',

    # bio words
    'word snip': 'snp',
    'title snip': 'SNP',
    'word QTL': 'qtl',
    'title QTL': 'QTL',
    'word transcript import': 'tximport',
    'word seek': 'seq',
    'title seek': 'Seq',
    'word attack': 'atac',
    'title attack': 'ATAC',
    'word geo': 'geuvadis',
    'title geo': 'GEUVADIS',

    'shrink ensemble': 'ensembl',

    # R
    'word plier': 'dplyr',

    # 'word lunixbochs': 'lunixbochs',
    'word talon': 'talon',
    # 'word Point2d': 'Point2d',
    # 'word Point3d': 'Point3d',
    'title Point': 'Point',
    'word angle': 'angle',

    # unix style words
    'shrink server': 'srv',
    'shrink user': 'usr',
    'shrink parameter': 'param',

    # weird tech words
    'word trello': 'trello',
}

keymap.update({
    'insert code': ['```\n\n```', Key('up')],
    '(insert (our | are))': ['```{r}\n\n```', Key('up')],
})

keymap.update({
    'math towel': 'tao',
    'math chai': 'chi',
    'math row': 'rho',
    'math sigh': 'psi',
    'math some': 'sum',
    'math root': 'sqrt',
    'math empirical': 'ecdf',
    'math poison': 'poisson',
    'math pie': 'pi',
})

ctx.keymap(keymap)
