from kivy.app import App
from kivy.uix.widget import Widget


class MainLayout(Widget):
    def foo(self):
        pass

class MainApp(App):
    def on_start(self):
        self.title = 'Save a word'
    def build(self):
        return MainLayout()


if __name__ == '__main__':
    MainApp().run()
