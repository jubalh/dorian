from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.storage.jsonstore import JsonStore
from gesture_box import GestureBox

import os.path

# Declare both screens
class DisplayScreen(GestureBox):
    pass

class SettingsScreen(GestureBox):
    images_base_path = ObjectProperty()
    display_duration = ObjectProperty()

# Dorian
class DorianApp(App):

    imgsource = StringProperty()
    sm = ScreenManager()
    settings_store = JsonStore('dorian.json')

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

        return self.sm

    def save_values(self):
        settings_screen = self.sm.get_screen('settingsscreen')
        self.settings_store.put('dorian',
                path = settings_screen.images_base_path.text,
                duration = settings_screen.display_duration.value)

if __name__ == '__main__':
    DorianApp().run()
