from talon.voice import Context, Key, press, Str
from user.utils import parse_words_as_integer

# It is recommended to use this script in tandem with Vimium, a Google Chrome plugin for controlling the browser via keyboard
# https://vimium.github.io/

context = Context('GoogleChrome', bundle='com.google.Chrome')

keymaps = {
  'back': Key('cmd-['),
  'forward': Key('cmd-]'),
}

context.keymap(keymaps)
