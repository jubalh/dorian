from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.storage.jsonstore import JsonStore
from kivy.clock import Clock

from gesture_box import GestureBox

import os.path
import random

# Declare both screens
class DisplayScreen(GestureBox):
    pass

class SettingsScreen(GestureBox):
    images_base_path = ObjectProperty()
    display_duration = ObjectProperty()

# Dorian
class DorianApp(App):

    current_image_path = StringProperty()
    sm = ScreenManager()
    settings_store = JsonStore('dorian.json')
    images = []
    updater = None

    def build(self):
        display_screen = DisplayScreen(name='displayscreen')
        display_screen.set_screenmanager(self.sm)
        settings_screen = SettingsScreen(name='settingsscreen')
        settings_screen.set_screenmanager(self.sm)

        self.sm.add_widget(display_screen)
        self.sm.add_widget(settings_screen)

        # load values
        if os.path.isfile('dorian.json'):
            settings_screen.images_base_path.text = self.settings_store.get('dorian')['path']
            settings_screen.display_duration.value = self.settings_store.get('dorian')['duration']

        self.new_base_start_slideshow()

        return self.sm

    def on_settings_ok_pressed(self):
        settings_screen = self.sm.get_screen('settingsscreen')

        # save values in store
        self.settings_store.put('dorian',
                path = settings_screen.images_base_path.text,
                duration = settings_screen.display_duration.value)
        # stop old cycle
        Clock.unschedule(self.updater)
        # start new cycle
        self.new_base_start_slideshow()

    # needs args to work with scheduler
    def choose_new_random_picture(self, *args):
        # choose random image
        random_image = random.choice(self.images)
        # display image
        self.current_image_path = random_image

    def build_images_list(self, path):
        for dirpath, subdirs, files in os.walk(path):
            for f in files:
                if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                    fullpath = os.path.join(dirpath, f)
                    self.images.append(fullpath)

    def new_base_start_slideshow(self):
        settings_screen = self.sm.get_screen('settingsscreen')
        # build new image list
        self.build_images_list(settings_screen.images_base_path.text)
        # set new pic
        self.choose_new_random_picture()
        # start scheduler
        self.updater = Clock.schedule_interval(self.choose_new_random_picture,
                settings_screen.display_duration.value)

if __name__ == '__main__':
    DorianApp().run()
