from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivymd.app import MDApp

from CashTGo.screen.scanSc import ScanScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from CashTGo.core.scanner import Scanner
#from CashTGo.core.color import colors
from CashTGo.screen.cashJourneySc import CashJourneyScreen

from core.color import *  # Importiere alle Farbdefinitionen
from screen.startSc import StartScreen  # Importiere StartScreen

# Stylesheet laden
Builder.load_file('core/styles.kv')

# Fenstergröße dynamisch anpassen oder auf eine mobile Standardgröße setzen
Window.size = (360, 640)  # Standardgröße für kleine Smartphones
# Oder für automatische Anpassung an den Bildschirm
# Window.fullscreen = 'auto'

# Import available screen modules (replace missing ones with placeholders)
try:
    from screen.loginSc import LoginScreen
except ImportError:
    class LoginScreen(Screen):
        pass

try:
    from screen.registerSc import RegisterScreen
except ImportError:
    class RegisterScreen(Screen):
        pass

try:
    from screen.homeASc import HomeAScreen
except ImportError:
    class HomeAScreen(Screen):
        pass

try:
    from screen.homeBSc import HomeBScreen
except ImportError:
    class HomeBScreen(Screen):
        pass

try:
    from screen.scanSc import ScanScreen
except ImportError:
    class ScanScreen(Screen):
        pass
try:
    from screen.cashJourneySc import CashJourneyScreen
except ImportError:
    class CashJourneyScreen(Screen):
        pass

try:
    from screen.cashLottoSc import CashLottoScreen
except ImportError:
    class CashLottoScreen(Screen):
        pass

try:
    from screen.cash4GoodSc import Cash4GoodScreen
except ImportError:
    class Cash4GoodScreen(Screen):
        pass

try:
    from screen.cashQuizSc import CashQuizScreen
except ImportError:
    class CashQuizScreen(Screen):
        pass

try:
    from screen.cashGameSc import CashGameScreen
except ImportError:
    class CashGameScreen(Screen):
        pass

try:
    from screen.cashBackSc import CashBackScreen
except ImportError:
    class CashBackScreen(Screen):
        pass

try:
    from screen.cashVoucherSc import CashVoucherScreen
except ImportError:
    class CashVoucherScreen(Screen):
        pass

# Main App Class
class CashTGoApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(HomeAScreen(name='homeA'))
        sm.add_widget(HomeBScreen(name='homeB'))
        sm.add_widget(ScanScreen(name='scan'))
        sm.add_widget(CashJourneyScreen(name='cashJourney'))
        sm.add_widget(CashLottoScreen(name='cashLotto'))
        sm.add_widget(Cash4GoodScreen(name='cash4Good'))
        sm.add_widget(CashQuizScreen(name='cashQuiz'))
        sm.add_widget(CashGameScreen(name='cashGame'))
        sm.add_widget(CashBackScreen(name='cashBack'))
        sm.add_widget(CashVoucherScreen(name='cashVoucher'))
        sm.add_widget(Scanner(name='scanbus'))
        #sm.add_widget(CashJourney(name='cashJourneybus'))
        return sm


if __name__ != '__main__':
    pass
# Entry point
else:
    CashTGoApp().run()
