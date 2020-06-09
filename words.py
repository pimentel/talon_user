from talon.voice import Context, Key

ctx = Context('words')

keymap = {
    'word width': 'width',
    'word queue': 'queue',
    'word eye': 'eye',
    'word bson': 'bson',
    'word iter': 'iter',
    'word index': 'index',

    'word jupiter': 'jupyter',

    'word args': 'args',
    'word paste': 'paste',
    'word point': 'point',
    'word head': 'head',
    'word pain': 'pane',
    'word pains': 'panes',
    'word sink': 'sync',
    'word in it': 'init',
    'word lint': 'lint',
    'title lint': 'Lint',
    'word linter': 'linter',
    'title linter': 'Linter',

    'word noel': 'null',
    'title noel': 'Null',
    'yeller noel': 'NULL',

    'word gutentags': 'gutentags',
    'title Gutentags': 'Gutentags',

    'word (dickt | dictionary)': 'dict',
    'word dup': 'dup',
    'word get hub': 'github',
    'title get hub': 'GitHub',
    'word get': 'git',
    'word macvim': 'macvim',
    'word printf': 'printf',
    'word shell': 'shell',
    'word streak': ['streq()', Key('left')],
    'word mux': 'tmux',
    'yeller mux': 'TMUX',
    'word (them | vim)': 'vim',
    'word neo': 'neovim',

    'word stood in': 'stdin',
    'word stood out': 'stdout',
    'word stood err': 'stderr',
    'word write': 'write',
    'word linux': 'linux',

    'shrink command': 'cmd',
    'shrink control': 'ctrl',
    'shrink parameter': 'param',
    'shrink parameters': 'params',

    'word snake file': 'snakefile',
    'title snake file': 'Snakefile',
    'word snake make': 'snakemake',
    'word latex make': 'latexmk',
    'word seek T K': 'seqtk',
    'word numpy': 'numpy',

    'word adam': 'atom',
    'title adam': 'Atom',

    # names
    'word puenteh': 'puente',
    'title puenteh': 'Puente',
    'word avi': 'avi',
    'title avi': 'Avi',
    'title aviell': 'Aviel',
    'word lior': 'lior',
    'title lior': 'Lior',
    'word palkter': 'pachter',
    'title palkter': 'Pachter',
    'word paul': 'pall',
    'title paul': 'Pall',
    'word bays': 'bayes',
    'title bays': 'Bayes',

    # bio words
    'word mod': 'maude',
    'title mod': 'MAUDE',
    'word magic': 'mageck',
    'title magic': 'MAGeCK',

    'word biomart': 'biomaRt',
    'word crisper': 'crispr',
    'title crisper': 'CRISPR',
    'word chrome': 'chrom',
    'word entrée': 'entrez',
    'title racks': 'RAxML',
    'word contig': 'contig',
    'word snip': 'snp',
    'word snips': 'snps',
    'title snips': 'SNPs',
    'word QTL': 'qtl',
    'title QTL': 'QTL',
    'word EQTL': 'eqtl',
    'title EQTL': 'eQTL',
    'word IRQTL': 'irqtl',
    'title IRQTL': 'irQTL',
    'word seek': 'seq',
    'title seek': 'Seq',
    'yeller seek': 'SEQ',
    'word attack': 'atac',
    'title attack': 'ATAC',
    'word geo': 'geuvadis',
    'title geo': 'GEUVADIS',
    'word fast Q': 'fastq',
    'word fasta': 'fasta',

    'shrink ensemble': 'ensembl',

    # R
    'word plier': 'dplyr',
    'word quantile': 'quantile',

    'word talon': 'talon',
    'title Point': 'Point',
    'word angle': 'angle',

    # unix style words
    'shrink server': 'srv',
    'shrink user': 'usr',
    'shrink parameter': 'param',

    # weird tech words
    'word pandoc': 'pandoc',
    'word SQ light': 'sqlite',
    'word trello': 'trello',
    'word presto': 'prezto',
    'word slurm': 'slurm',
}

keymap.update({
    'insert code': ['```\n\n```', Key('up')],
    'insert (our | are)': ['```{r}\n\n```', Key('up')],
})

ctx.keymap(keymap)
