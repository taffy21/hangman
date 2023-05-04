from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from random import choice
from kivy.graphics import Line, Color
import re

def word_hider(word):
    count = len(word)
    return "_" * count


class MyManager(ScreenManager):
    pass


class FirstScreen(Screen):
    pass


class GameOver(Screen):
    pass


class GameScreen(Screen):
    pass


class MyLabel(Label):
    word = StringProperty
    count = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.word = self.begin_game()
        self.text = word_hider(self.word)

    def begin_game(self):
        self.word = choice(["AEROPLANE", "DEVELOPMENT", "CHUCK", "EXTENSIVE", "MINISTRY", "XYLOPHONE"])
        return self.word

    def combineListLetters(self, arg):  # not sure how this is meant to work @ ALL
        word = ""
        for i in arg:
            word += i
        return word

    def wordPlayer(self, instance):

        letter = instance.text
        self.trial = list(self.text)
        if letter in self.word:
            indexes = [i.start() for i in re.finditer(letter, self.word)]
            for index in indexes:
                self.trial[index] = letter
            self.text = self.combineListLetters(self.trial)
        else:
            self.drawer()
            if self.count == 10:
                self.parent.parent.parent.parent.current = "third"  #moves to the Game Over screen

    def drawer(self):
        self.count += 1
        width = 4
        if self.count == 1:
            self.canvas.add(Color(1, 0, 0))
            self.canvas.add(Line(points=[100, 200, 100, 500], width=width))
        elif self.count == 2:
            self.canvas.add(Line(points=[100, 200, 100, 500, 300, 500], width=width))
        elif self.count == 3:
            self.canvas.add(Line(points=[100, 200, 100, 500, 300, 500, 300, 450], width=width))
        elif self.count == 4:
            self.canvas.add(Line(circle=(300, 430, 20), width=width))
        elif self.count == 5:
            self.canvas.add(Line(points=[300, 410, 300, 400], width=width))
        elif self.count == 6:
            self.canvas.add(Line(points=[300, 400, 280, 380], width=width))
        elif self.count == 7:
            self.canvas.add(Line(points=[300, 400, 320, 380], width=width))
        elif self.count == 8:
            self.canvas.add(Line(points=[300, 400, 300, 350], width=width))
        elif self.count == 9:
            self.canvas.add(Line(points=[300, 350, 280, 330], width=width))
        elif self.count == 10:
            self.canvas.add(Line(points=[300, 350, 320, 330], width=width))

class TrialGameApp(App):
    pass


if __name__ == "__main__":
    TrialGameApp().run()
