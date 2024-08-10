from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.gridlayout import GridLayout

class WhiteBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(WhiteBoxLayout, self).__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Белый цвет (RGBA)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class Kaspi(App):
    
    def build(self):
        layout = WhiteBoxLayout(orientation='horizontal', padding=10, spacing=10)
    
        btn3 = Button(text="Предъявить документ ",size_hint=(0.5, 0.05),font_size=18)
        btn4 = Button(text="Отправить документ",size_hint=(0.5, 0.05),font_size=18)
       
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        

        return layout

if __name__ == "__main__":
    Kaspi().run()
