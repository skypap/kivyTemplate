from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget


class CustomWidget(Widget):
    pass
class DemoWidgetScreen(Screen):
    def go_main_screen(self):
        self.manager.current = "mainScreen"
    # def go_second_screen(self):
    #     self.manager.current = "secondScreen"
    # def go_demo_widget_screen(self):
    #     pass

# class CustomDropDown(BoxLayout):
#     pass