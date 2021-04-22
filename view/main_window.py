from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class MainScreen(Screen):
    pass

class AddScreen(Screen):
    pass

class DeleteScreen(Screen):
    pass

class ExportScreen(Screen):
    pass

class LearnScreen(Screen):
    pass

class InfoScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MainApp(App):
    def on_start(self):
        self.title = 'Save a word'
    def build(self):
        return Builder.load_file("main.kv")


if __name__ == '__main__':
    MainApp().run()
