
from datetime import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class ClockApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.time_label = Label(font_size="56sp", color=(0, 1, 0.8, 1))
        self.date_label = Label(font_size="22sp", color=(1, 1, 1, 1), size_hint_y=0.3)

        layout.add_widget(self.time_label)
        layout.add_widget(self.date_label)

        Clock.schedule_interval(self.update, 1)
        self.update(0)
        return layout

    def update(self, dt):
        now = datetime.now()
        self.time_label.text = now.strftime("%H:%M:%S")
        self.date_label.text = now.strftime("%d/%m/%Y")


if __name__ == "__main__":
    ClockApp().run()
