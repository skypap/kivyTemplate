from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from Screen.MainScreen.main_screen import *
from Screen.SecondScreen.second_screen import *
from Screen.DemoWidgetScreen.demo_widget_screen import *
class WindowManager(ScreenManager):


    pass

class MyMainApp(App):
    def build(self):
        Builder.load_file("Screen/SecondScreen/second_screen.kv")
        Builder.load_file("Screen/MainScreen/main_screen.kv")
        Builder.load_file("Screen/DemoWidgetScreen/demo_widget_screen.kv")
        sm = ScreenManager()
        sm.add_widget(MainWindow())
        sm.add_widget(SecondWindow())
        sm.add_widget(DemoWidgetScreen())
        return sm


if __name__ == "__main__":
    MyMainApp().run()