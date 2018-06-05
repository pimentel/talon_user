from talon.voice import Context, Key

ctx = Context('words')

keymap = {
    'word queue': 'queue',
    'word eye': 'eye',
    'word bson': 'bson',
    'word iter': 'iter',
    'word no': 'null',
    'title no': 'NULL',
    'word cmd': 'cmd',
    'word control': 'ctrl',
    'word dup': 'dup',
    'word streak': ['streq()', Key('left')],
    'word printf': 'printf',
    'word (dickt | dictionary)': 'dict',
    'word shell': 'shell',
    'word get': 'git',

    'shrink parameters': 'params',
    'shrink parameter': 'param',

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
    'word kyle': 'lior',
    'word bays': 'bayes',
    'title bays': 'Bayes',

    # bio words
    'word snip': 'snp',
    'title snip': 'SNP',
    'word Q T L': 'qtl',
    'title Q T L': 'QTL',
    'word transcript import': 'tximport',
    'word seek': 'seq',
    'title seek': 'Seq',
    'word attack': 'atac',
    'title attack': 'ATAC',

    'shrink ensemble': 'ensembl',


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
    # 'mark block': ['```\n\n```', Key('up'), Key('up')],
    'insert code': ['```\n\n```', Key('up')],
    'insert our': ['```{r}\n\n```', Key('up')],
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
})

ctx.keymap(keymap)
