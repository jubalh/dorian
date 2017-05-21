from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from gesture_box import GestureBox

# Declare both screens
class DisplayScreen(GestureBox):
    pass

class SettingsScreen(GestureBox):
    pass

# Dorian
class DorianApp(App):

    imgsource = StringProperty()
    sm = ScreenManager()

    def build(self):
        display_screen = DisplayScreen(name='displayscreen')
        display_screen.set_screenmanager(self.sm)
        settings_screen = SettingsScreen(name='settingsscreen')
        settings_screen.set_screenmanager(self.sm)

        self.sm.add_widget(display_screen)
        self.sm.add_widget(settings_screen)

        return self.sm

if __name__ == '__main__':
    DorianApp().run()
