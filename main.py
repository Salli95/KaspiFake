from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

class WhiteBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(WhiteBoxLayout, self).__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Белый цвет (RGBA)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        # Обновляем размеры и позицию фона при изменении размера или положения виджета
        self.rect.pos = self.pos
        self.rect.size = self.size

class WhiteBackgroundApp(App):
    def build(self):
        # Создаем основной вертикальный макет, который будет содержать верхнюю и нижнюю части
        main_layout = WhiteBoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Создаем верхнюю часть макета для кнопок "Документы" и "Реквизиты"
        # Используем BoxLayout с горизонтальной ориентацией
        top_layout = BoxLayout(orientation='horizontal', size_hint_y=0.003, padding=10, spacing=10)
        
        # Создаем кнопки для верхней части
        btn1 = Button(
            text="Документы", 
            size_hint=(0.5, 0.05), 
            font_size=18, 
            background_color=(0, 0, 1, 1)
            )
        btn2 = Button(text="Реквизиты",
                      size_hint=(0.5, 0.05), 
                      font_size=18, 
                      background_color=(0.662, 0.662, 0.662, 0.5)
                      
                      ) 
        # Добавляем кнопки в верхний макет
        top_layout.add_widget(btn1)
        top_layout.add_widget(btn2)
        
        # Создаем нижнюю часть макета для кнопок "Предъявить документ" и "Отправить документ"
        # Используем BoxLayout с горизонтальной ориентацией
        bottom_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1, padding=10, spacing=10)
        
        # Создаем кнопки для нижней части
        btn3 = Button(text="Предъявить документ", size_hint=(0.5, 0.05), font_size=18)
        btn4 = Button(text="Отправить документ", size_hint=(0.5, 0.05), font_size=18)
        
        # Добавляем кнопки в нижний макет
        bottom_layout.add_widget(btn3)
        bottom_layout.add_widget(btn4)
        
        # Добавляем верхний и нижний макеты в основной макет
        main_layout.add_widget(top_layout)
        main_layout.add_widget(bottom_layout)
        
        return main_layout

if __name__ == "__main__":
    WhiteBackgroundApp().run()
