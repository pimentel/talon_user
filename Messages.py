from talon.voice import Word, Key, Context, Str
import string

ctx = Context('messages', bundle = 'com.apple.iChat')

ctx.keymap({
  'tab next': Key('cmd-shift-]'),
  'tab last': Key('cmd-shift-['),
})
