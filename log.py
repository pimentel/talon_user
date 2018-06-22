import time
import datetime
import threading

from talon import app, ui
from talon.engine import engine
from talon.voice import Word, Context, Rep, Str, press
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER

phrase_lock = threading.Lock()

context = Context('log')

class Logger:
    def __init__(self):
        self.lock = threading.Lock()
        ts = time.time()
        self.timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S')
        self.file_name = '%s/%s.log' % (TALON_HOME, self.timestamp)

    def on_phrase(self, m):
        # if m['cmd'] in ('p.begin', 'p.end') and m['grammar'] == 'talon':
        if m['cmd'] in ('p.end') and m['grammar'] == 'talon':
            with self.lock:
                with open(self.file_name, 'a') as log_file:
                    log_file.write('%s\n' % ' '.join(m['phrase']))


logger = Logger()
engine.register('phrase', logger.on_phrase)

