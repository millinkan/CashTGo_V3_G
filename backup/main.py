# main.py
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from screen.startSc import StartScreen  # Importiere die StartScreen-Klasse
from screen.loginSc import LoginScreen
from screen.homeASc import HomeScreen
from screen.registerSc import RegisterScreen
from core.config import window_width, window_height
from kivy.lang import Builder

# Lade die Styles aus dem Unterordner
Builder.load_file('/core/styles.kv')

class MainApp(App):
    def build(self):
        Window.clearcolor = (0.98, 0.95, 0.89, 1)  # Beige Hintergrundfarbe setzen
        Window.size = (window_width, window_height)
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(HomeScreen(name='home'))
        return sm

if __name__ == '__main__':
    MainApp().run()
