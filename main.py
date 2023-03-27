from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from random import choice
import re

class MyLabel(Label):
    word = StringProperty
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.word = self.word_hider()
        self.text = self.word

    def begin_game(self):
        self.word = choice(["CHUCK", "AEROPLANE", "DEVELOPMENT"])
        return self.word

    def word_hider(self):
        count = len(self.begin_game())
        return "_" * count

    def combineListLetters(self, arg):   #not sure how this is meant to work @ ALL
        word = ""
        for i in arg:
            word += i
        return word

    def wordPlayer(self):
        playing = True
        wrong_count = 0
        complete = self.word_hider()
        selected_word = self.begin_game()
        while playing:
            letter = self.ids.buttonA.text
            if letter in selected_word:
                indexes = [i.start() for i in re.finditer(letter, selected_word)]
                for index in indexes:
                    complete[index] = letter
            else:
                wrong_count += 1
            if selected_word == self.combineListLetters(complete) or wrong_count == 10:
                playing = False


class MyBox(BoxLayout):
    pass

class TrialGameApp(App):
    pass

if __name__ == "__main__":
    TrialGameApp().run()
