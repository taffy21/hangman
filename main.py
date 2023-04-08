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


def word_hider(word):
    count = len(word)
    return "_" * count


class MyLabel(Label):
    word = StringProperty
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.word = self.begin_game()
        self.text = word_hider(self.word)

    def begin_game(self):
        self.word = choice(["AEROPLANE"])
        return self.word

    def combineListLetters(self, arg):   #not sure how this is meant to work @ ALL
        word = ""
        for i in arg:
            word += i
        return word

    def wordPlayer(self, instance):
        letter = instance.text
        self.trial = list(self.text)
        if letter in self.word:
            indexes = [i.start() for i in re.finditer(letter, self.word)]
            print(letter)
            for index in indexes:
                self.trial[index] = letter
            self.text = self.combineListLetters(self.trial)
        else:
            pass



class MyBox(BoxLayout):
    pass

class TrialGameApp(App):
    pass

if __name__ == "__main__":
    TrialGameApp().run()
