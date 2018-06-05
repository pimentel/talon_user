from talon.voice import Word, Context, Key, Rep, Str, press
from talon import ui

apps = {}

def switch_app(m):
    name = str(m._words[1])
    full = apps.get(name)
    if not full: return
    for app in ui.apps():
        if app.name == full:
            app.focus()
            break

def short_application(m, app):
    m._words = [0, app]
    switch_app(m)

ctx = Context('switcher')
keymap = {
    'focus {switcher.apps}': switch_app,

    'madame': lambda x: short_application(x, 'Atom'),
    'termite': lambda x: short_application(x, 'iTerm2'),
    'masseuse': lambda x: short_application(x, 'Messages'),
    'chromie': lambda x: short_application(x, 'Google Chrome'),
    'roman': lambda x: short_application(x, 'R'),
    # 'slacker': lambda x: short_application(x, 'Slack')
}

ctx.keymap(keymap)

def update_lists():
    global apps
    new = {}
    for app in ui.apps():
        # if not app.windows():
        #     continue
        words = app.name.split(' ')
        for word in words:
            if word and not word in new:
                new[word] = app.name
        new[app.name] = app.name
    if set(new.keys()) == set(apps.keys()):
        return
    ctx.set_list('apps', new.keys())
    apps = new

def ui_event(event, arg):
    if event in ('app_activate', 'app_launch', 'app_close', 'win_open', 'win_close'):
        update_lists()

ui.register('', ui_event)
update_lists()
