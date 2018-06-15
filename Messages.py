from talon.voice import Word, Key, Context, Str
import string

ctx = Context('messages', bundle = 'com.apple.iChat')

ctx.keymap({
  'next tab': Key('cmd-shift-]'),
  'last tab': Key('cmd-shift-['),
})
