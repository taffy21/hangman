from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import string
from kivy.properties import StringProperty
import hangman


class MyBox(BoxLayout):
    pass



class MyLetterGrid(GridLayout):
    alphabet = list(string.ascii_uppercase)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 5
        self.buttons = []
        for i in self.alphabet:
            self.btn = Button(text=f'{i}')
            self.btn.bind(on_press=self.pressed)
            self.add_widget(self.btn)
            self.buttons.append(self.btn)

    def pressed(self, instance):
        MyBox.ids.game_word.text = instance.text #this is where the code is dying


class TrialGameApp(App):
    def build(self):
        return MyBox()


if __name__ == "__main__":
    TrialGameApp().run()
