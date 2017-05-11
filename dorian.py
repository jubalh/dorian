import os
import random
import kivy

from kivy.clock import Clock
from kivy.config import Config
from kivy.app import App
from kivy.uix.image import Image

from os.path import expanduser

kivy.require('1.0.6') # replace with your current kivy version !


class MyApp(App):

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.images = []
        Config.set('graphics', 'fullscreen', 'auto')

    def buildPictureList(self, path):
        for dirpath, subdirs, files in os.walk(path):
            for f in files:
                if f.endswith(".png") or f.endswith(".jpg") or f.endswith(".jpeg"):
                    fullpath = os.path.join(dirpath, f)
                    self.images.append(fullpath)

    def display_new_picture(self, *args):
        randomsource = random.choice(self.images)
        print "Using image: %s" % randomsource
        self.root.source = randomsource

    def build(self):
        self.buildPictureList(expanduser('~/Pictures'))

        randomsource = random.choice(self.images)
        print "Using image: %s" % randomsource

        Clock.schedule_interval(self.display_new_picture, 5)

        return Image(source=randomsource)

if __name__ == '__main__':
    MyApp().run()
