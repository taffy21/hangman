import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class VelhaGame(GridLayout, Screen):
    def __init__(self, **kwargs):
        super(VelhaGame, self).__init__(**kwargs)
        self.cols = 3
        self.rows = 3
        self.font_size = 100

        self.buttons = []

        for i in range(1, 10):
            button = Button(text='', font_size=self.font_size)
            button.bind(on_press=self.player_turn)
            self.add_widget(button)
            self.buttons.append(button)

        self.player1 = True

    def player_turn(self, instance, *args):
        if self.player1:
            self.player1 = False
            instance.text = 'X'
        elif not self.player1:
            self.player1 = True
            instance.text = '0'

class VelhaGameApp(App):
    def build(self):
        game = Screen()
        table_screen = VelhaGame()
        game.add_widget(table_screen)
        return game

if __name__ == '__main__':
    VelhaGameApp().run()