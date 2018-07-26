from talon.voice import Context, Rep, RepPhrase, talon
from user.utils import parse_words_as_integer

from time import sleep

ctx = Context('repeater')


# TODO: This could be made more intelligent:
#         * Apply a timeout after which the command will not repeat previous actions
#         * Prevent stacking of repetitions upon previous repetitions
def repeat(m):
    repeat_count = parse_words_as_integer(m._words[1:])
    print(talon.last)

    if repeat_count is not None and repeat_count >= 2:
        repeater = Rep(repeat_count - 1)
        repeater.ctx = talon
        return repeater(None)


def repeat_delay(n, delay=0.09):
    for i in range(n):
        sleep(delay)
        repeater = Rep(i - 1)
        repeater.ctx = talon
        repeater(None)


ctx.keymap({
    'wink': Rep(1),
    'creek': RepPhrase(1),
    'soup': Rep(1),
    'trace': Rep(2),
    'quarr': Rep(3),
    # 'fypes': lambda m: repeat_delay(4),
    'fypes': Rep(4),
    'repeat (0 | oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)+': repeat,
})
