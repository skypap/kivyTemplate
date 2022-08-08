from kivy.uix.screenmanager import Screen
class SecondWindow(Screen):
    def go_main_screen(self):
        self.manager.current = "mainScreen"
    pass