from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Box(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.label = Label()
        grid = GridLayout(cols=2)

        btn1 = Button(text="A")
        btn2 = Button(text="B")
        btn1.bind(on_press=self.callback)
        btn2.bind(on_press=self.callback2)

        self.add_widget(self.label)
        grid.add_widget(btn1)
        grid.add_widget(btn2)
        self.add_widget(grid)

    def callback(self, instance):
        print("king")

    def callback2(self, instance):
        self.label.text = ""

class TutorialApp(App):
    pass


if __name__ == "__main__":
    TutorialApp().run()
