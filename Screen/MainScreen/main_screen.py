from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class MainWindow(Screen):

    def go_second_screen(self):
        self.manager.current = "secondScreen"
    def go_demo_widget_screen(self):
        self.manager.current = "demoWidgetScreen"


