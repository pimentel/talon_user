from talon.voice import Context, Rep, talon
from talon.audio import noise
from talon import cron

context = Context('repeat_sound')


class Repeater:
    def __init__(self, initial_delay = '500ms', repeat_delay = '100ms'):
        self.initial_delay = initial_delay
        self.repeat_delay = repeat_delay
        noise.register('noise', self.on_noise)
        self.job = None


    def disable(self):
        noise.unregister('noise', self.on_noise)
        if self.job:
            cron.cancel(self.job)


    def enable(self):
        noise.register('noise', self.on_noise)


    def on_noise(self, noise):
        if noise == 'hiss_start' and talon.enabled:
            if self.job is None:
                self.job = cron.after(self.initial_delay, self.repeat)
                print('HISS START')
        elif noise == 'hiss_end' and self.job:
            print('HISS STOP')
            cron.cancel(self.job)
            self.job = None


    def repeat(self):
        repeater = Rep(1)
        repeater.ctx = talon
        repeater(None)
        if self.job:
            self.job = cron.after(self.repeat_delay, self.repeat)
            print('REPEAT')

repeater = Repeater()

keymap = {
    'enable repeat': lambda m: repeater.enable(),
    'disable repeat': lambda m: repeater.disable(),
}


context.keymap(keymap)
