import copy

from time import time

from talon.voice import Context, Rep, talon
from talon.audio import noise
from talon import cron

context = Context('repeat_sound')
repeat_context = Context('repeat_enabled')

# " "jskljlksjlksjlksdjlksdjlksdjsdlkjsdlksdjlksdjskldjsdkljsdlkjsdlkjskljsdlksjlksjlksjslkjslksjlkjslkjslkjskljsklsjklsjlksjklskjsjlksjklsjslkjslksjlksjlk

class Repeater:
    def __init__(self, initial_delay = '500ms', repeat_delay = '100ms'):
        self.initial_delay = initial_delay
        self.repeat_delay = repeat_delay
        # noise.register('noise', self.on_noise)
        self.job = None
        self.action = None
        self.rule = None


    def disable(self):
        # noise.unregister('noise', self.on_noise)
        if self.job:
            cron.cancel(self.job)


    def enable(self):
        # noise.register('noise', self.on_noise)
        pass


    def start(self):
        print(talon.last)
        if self.job is None:
            self.action, self.rule = talon.last_action[0]
            print('START')
            repeat_context.keymap({
                'stop': lambda m: self.stop(),
            })
            repeat_context.load()
            self.job = cron.after(self.initial_delay, self.repeat)


    def stop(self):
        if self.job:
            print('STOP')
            cron.cancel(self.job)
            repeat_context.unload()
            self.job = None


    # def on_noise(self, noise):
        # pass
    def on_noise(self, noise):
        pass
        now = time()
        # print(noise)
        if noise == 'pop':
            print('POP')
            if self.job:
                cron.cancel(self.job)
                self.job = None
                print('STOP')
            elif now - self.last_pop < 0.5 and self.job is not None:
                self.job = cron.after(self.initial_delay, self.repeat)
                print('START')
            self.last_pop = now

            # if self.job is None:
                # self.job = cron.after(self.initial_delay, self.repeat)
                # print('HISS START')
        # elif noise == 'hiss_end' and self.job:
            # print('HISS STOP')
            # cron.cancel(self.job)
            # self.job = None


    def repeat(self):
        print("IN REPEATER")
        self.action(self.rule)
        if self.job:
            self.job = cron.after(self.repeat_delay, self.repeat)
            print('REPEAT')

repeater = Repeater()
# repeater.disable()

keymap = {
    'enable repeat': lambda m: repeater.enable(),
    'disable repeat': lambda m: repeater.disable(),
    'start repeat': lambda m: repeater.start(),
}


context.keymap(keymap)
