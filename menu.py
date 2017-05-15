from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from gesture_box import GestureBox

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    Image:
        source: str(app.imgsource)

<SettingsScreen>:
    BoxLayout:
        BoxLayout:
            orientation: 'vertical'
            BoxLayout:
                size_hint_y: None
                height: '50dp'
                orientation: 'horizontal'
                Label:
                    text: 'Folder:'
                TextInput:
                    text: '/home/michael/Pictures/netbsd.png'
                    multiline: False
                    id: textinput_path
            BoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                height: '50dp'
                Label:
                    text: 'Display duration:'
                BoxLayout:
                    orientation: 'vertical'
                    Label:
                        text: "%2d" % slider_time.value
                    Slider:
                        id: slider_time
                        range: (5, 60)
                        value: 10
                        step: 1
            Widget:
            BoxLayout:
                size_hint_y: None
                height: '50dp'
                orientation: 'horizontal'
                Button:
                    text: 'Ok'
                    on_press:
                        root.manager.current = 'menu'
                        app.imgsource = textinput_path.text
                Button:
                    text: 'Cancel'
                    on_press: root.manager.current = 'menu'
""")

# Declare both screens
class MenuScreen(GestureBox):
    pass

class SettingsScreen(GestureBox):
    pass


class TestApp(App):

    imgsource = StringProperty()
    sm = ScreenManager()

    def build(self):
        menu_screen = MenuScreen(name='menu')
        menu_screen.set_screenmanager(self.sm)
        settings_screen = SettingsScreen(name='settings')
        settings_screen.set_screenmanager(self.sm)

        self.sm.add_widget(menu_screen)
        self.sm.add_widget(settings_screen)

        return self.sm

if __name__ == '__main__':
    TestApp().run()
