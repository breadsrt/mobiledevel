from kivy.app import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen


class FirstScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        btn = Button(text="screen 1")
        btn.on_press = self.go_to_second
        self.add_widget(btn)
    def go_to_second(self):
        self.manager.current = "second"

class SecondScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        btn = Button(text="screen 2")
        btn.on_press = self.go_to_third
        self.add_widget(btn)

    def go_to_third(self):
        self.manager.current = "third"


class ThirdScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        line = BoxLayout()
        btn = Button(text="screen 3")

        btn.on_press = self.go_to_first


        self.add_widget(btn)




    def go_to_first(self):
        self.manager.current = "first"



class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name="first"))
        sm.add_widget(SecondScreen(name="second"))
        sm.add_widget(ThirdScreen(name="third"))
        return sm

MyApp().run()