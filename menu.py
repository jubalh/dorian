from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.properties import StringProperty

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Image:
            source: str(app.imgsource)
        Button:
            text: 'to settings'
            on_press: root.manager.current = 'settings'

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
                        text: str(slider_time.value)
                    Slider:
                        id: slider_time
                        range: (5, 60)
                        value: '10'
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
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass


class TestApp(App):

    imgsource = StringProperty()

    def build(self):

        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm

if __name__ == '__main__':
    TestApp().run()
