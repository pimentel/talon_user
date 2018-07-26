from os import system
from talon.voice import Context, Key
from talon import applescript, ui

from user.std import parse_words

ctx = Context('navigation')

menu_items = {}


def select_menu_bar_item(m):
    name = str(m._words[1])
    full = menu_items.get(name)
    if not full:
        return
    applescript.run(r'''
tell application "System Events"
  tell (first process whose frontmost is true)
    click menu bar item "%s" of menu bar 1
  end tell
end tell
    ''' % full)


def update_lists():
    global menu_items
    print('IN HERE')
    items = applescript.run(r'''
on menubar_items()
	tell application "System Events"
		tell (first process whose frontmost is true)
			tell menu bar 1
				set test to name of every menu bar item
				return test
			end tell
		end tell
	end tell
end menubar_items

set theList to menubar_items()
set {text item delimiters, TID} to {",", text item delimiters}
set {text item delimiters, theListAsString} to {TID, theList as text}
return theListAsString
''')
    items = items.split(',')
    new = {}
    for item in items:
        words = item.split(' ')
        for word in words:
            if word and not word in new:
                new[word] = item
        new[item] = item
    if set(new.keys()) == set(menu_items.keys()):
        return
    ctx.set_list('menu_items', new.keys())
    menu_items = new


def ui_event(event, arg):
    # if event in ('app_activate', 'app_launch', 'app_close', 'win_open',
    #              'win_close'):
    if event in ('app_activate', 'win_open', 'win_close'):
        update_lists()


ui.register('', ui_event)
update_lists()

keymap = {
    # Application navigation
    'launcher': Key('cmd-space'),
    'swick': Key('cmd-tab'),

    # 'menu <dgndictation>': select_menu_bar_item,
    'menu {navigation.menu_items}': select_menu_bar_item,

    'close tab': Key('cmd-w'),
    'close window': Key('cmd-shift-w'),

    'mission': lambda m: system('open -a \'Mission Control\''),
    'show windows': Key('ctrl-down'),
    'curtail': Key('cmd-m'),

    '(next window | gibby)': Key('cmd-`'),
    '(last window | shibby)': Key('cmd-shift-`'),
    'window space right': Key('cmd-alt-ctrl-right'),
    'window space left': Key('cmd-alt-ctrl-left'),

    'new window': Key('cmd-n'),

    # 'next app': Key('cmd-tab'),
    # 'last app': Key('cmd-shift-tab'),

    'next space': Key('cmd-alt-ctrl-right'),
    'last space': Key('cmd-alt-ctrl-left'),

    # Following three commands should be application specific
    'last tab': Key('cmd-shift-['),
    'next tab': Key('cmd-shift-]'),
    'new tab': Key('cmd-t'),
    'reload': Key('cmd-r'),

    # 'scroll down': [Key('down')] * 30,
    'page up': [Key('pageup')],
    # 'scroll up': [Key('up')] * 30,
    'page down': [Key('pagedown')],
    # 'scroll top': [Key('cmd-up')],
    # 'scroll bottom': [Key('cmd-down')],

    # deleting
    'junk': Key('backspace'),
    'scrap': Key('delete'),
    'kite': Key('alt-delete'),
    'snip left': Key('cmd-shift-left delete'),
    'snip right': Key('cmd-shift-right delete'),
    'slurp': Key('backspace delete'),
    'trough': Key('alt-backspace'),

    # moving
    # '(tab | tarp)': Key('tab'),
    'tarp': Key('tab'),
    'tarsh': Key('shift-tab'),
    'slap': [Key('cmd-right enter')],
    'peg': Key('alt-left'),
    'fran': Key('alt-right'),
    'ricky': Key('cmd-right'),
    'derek': Key('cmd-right space'),
    'lefty': Key('cmd-left'),
    'jeep': Key('up'),
    'lloyd':  Key('left'),
    'chris': Key('right'),
    'doom':  Key('down'),
    'doom way': Key('cmd-down'),
    'jeep way': Key('cmd-up'),

    # zooming
    'zoom in': Key('cmd-='),
    'zoom out': Key('cmd--'),
    'zoom normal': Key('cmd-0'),

    # selecting
    'select all': Key('cmd-a'),
    'snatch': Key('cmd-x'),
    'shackle': [Key('cmd-left'), Key('shift-cmd-right')],
    'stoosh': Key('cmd-c'),
    'spark': Key('cmd-v'),
    'shreepway': Key('cmd-shift-up'),
    'shroomway': Key('cmd-shift-down'),
    'shreep': Key('shift-up'),
    'shroom': Key('shift-down'),
    'lecksy': Key('cmd-shift-left'),
    'ricksy': Key('cmd-shift-right'),
    'shlocky': Key('alt-shift-left'),
    'shrocky': Key('alt-shift-right'),
    'shlicky': Key('shift-left'),
    'shricky': Key('shift-right'),
}

ctx.keymap(keymap)
