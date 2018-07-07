from talon.voice import Context, Rep, RepPhrase, talon
from user.utils import parse_words_as_integer
from talon.audio import noise

from threading import Timer, Lock

context = Context('repeat_sound')


class Repeater:
    def __init__(self, initial_delay = 0.5, repeat_delay = 0.1):
        self.initial_delay = initial_delay
        self.repeat_delay = repeat_delay
        noise.register('noise', self.on_noise)
        self.lock = Lock()
        self.running = False
        self.timer = None


    def disable(self):
        noise.unregister('noise', self.on_noise)


    def enable(self):
        noise.register('noise', self.on_noise)


    def on_noise(self, noise):
        if noise == 'hiss_start':
            with self.lock:
                if self.running:
                    return
                print('HISS START')
                self.running = True
                self.timer = Timer(self.initial_delay, self.repeat)
            if self.timer is not None:
                self.timer.start()
        elif noise == 'hiss_end':
            with self.lock:
                if not self.running:
                    return
                self.timer.cancel()
                self.timer = None
                self.running = False
            print('HISS STOP')


    def repeat(self):
        repeater = Rep(1)
        repeater.ctx = talon
        repeater(None)
        with self.lock:
            if not self.running:
                return
            print('REPEAT')
            self.timer = Timer(self.repeat_delay, self.repeat)
        if self.timer is not None:
            self.timer.start()

repeater = Repeater()

keymap = {
    'enable repeat': lambda m: repeater.enable(),
    'disable repeat': lambda m: repeater.disable(),
}


context.keymap(keymap)
