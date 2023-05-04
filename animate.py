from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Canvas, Line, Ellipse, Color, Rectangle
class HangBox(BoxLayout):
    pass

class MyWidget(Widget):
    count = NumericProperty()

    def draw(self):
        self.count+=1
        if self.count == 1:
            self.canvas.add(Color(1, 0, 0))
            self.canvas.add(Line(points=[100, 100, 100, 300], width=5))
        elif self.count == 2:
            #self.canvas.add(Color(1, 0, 0))
            self.canvas.add(Line(points=[100, 100, 100, 300, 300, 300], width=5))
        elif self.count == 3:
            self.canvas.add(Line(points=[100, 100, 100, 300, 300, 300, 300, 250], width=5))
        elif self.count == 4:
            self.canvas.add(Line(circle=(300, 230, 20), width=5))
        elif self.count == 5:
            self.canvas.add(Line(points=[300, 210, 300, 200], width=5))
        elif self.count == 6:
            self.canvas.add(Line(points=[300, 200, 280, 180], width=5))
        elif self.count == 7:
            self.canvas.add(Line(points=[300, 200, 320, 180], width=5))
        elif self.count == 8:
            self.canvas.add(Line(points=[300, 200, 300, 150], width=5))
        elif self.count == 9:
            self.canvas.add(Line(points=[300, 150, 280, 130], width=5))
        elif self.count == 10:
            self.canvas.add(Line(points=[300, 150, 320, 130], width=5))



    def drawer(self):
        pass

class AnimateApp(App):
    pass


if __name__ == "__main__":
    AnimateApp().run()

