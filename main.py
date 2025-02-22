from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen , ScreenManager
from kivymd.app import MDApp
from Project_5.CashTGo.core.scanner import Scanner

from screen.startSc import StartScreen  # Import the start screen

# Load the stylesheet
Builder.load_file ( 'core/styles.kv' )

# Set a standard window size for mobile applications
Window.size = (360 , 640)  # Mobile-friendly resolution

# Optional: Attempt to import each additional screen. Provide fallbacks where necessary.
# Each try-except block ensures that missing screens don’t halt the app.
try:
    from screen.loginSc import LoginScreen
except ImportError:
    class LoginScreen ( Screen ):
        def __init__(self , **kwargs):
            super ().__init__ ( **kwargs )
            self.name = "login"  # Default screen name fallback

try:
    from screen.registerSc import RegisterScreen
except ImportError:
    class RegisterScreen ( Screen ):
        def __init__(self , **kwargs):
            super ().__init__ ( **kwargs )
            self.name = "register"  # Default screen name fallback

try:
    from screen.homeASc import HomeAScreen
except ImportError:
    class HomeAScreen ( Screen ):
        def __init__(self , **kwargs):
            super ().__init__ ( **kwargs )
            self.name = "homeA"  # Default screen name fallback

try:
    from screen.homeBSc import HomeBScreen
except ImportError:
    class HomeBScreen ( Screen ):
        def __init__(self , **kwargs):
            super ().__init__ ( **kwargs )
            self.name = "homeB"  # Default screen name fallback

try:
    from screen.scanSc import ScanScreen
except ImportError:
    class ScanScreen ( Screen ):
        def __init__(self , **kwargs):
            super ().__init__ ( **kwargs )
            self.name = "scan"  # Default screen name fallback

try:
    from screen.cashJourneySc import CashJourneyScreen
except ImportError:
    class CashJourneyScreen ( Screen ):
        def __init__(self , **kwargs):
            super ().__init__ ( **kwargs )
            self.name = "cashJourney"  # Default screen name fallback

try:
    from screen.cashLottoSc import CashLottoScreen
except ImportError:
    class CashLottoScreen ( Screen ):
        def __init__(self , **kwargs):
            super ().__init__ ( **kwargs )
            self.name = "cashLotto"  # Default screen name fallback

try:
    from screen.cash4GoodSc import Cash4GoodScreen
except ImportError:
    class Cash4GoodScreen ( Screen ):
        def __init__(self , **kwargs):
            super ().__init__ ( **kwargs )
            self.name = "cash4Good"  # Default screen name fallback

try:
    from screen.cashQuizSc import CashQuizScreen
except ImportError:
    class CashQuizScreen ( Screen ):
        def __init__(self , **kwargs):
            super ().__init__ ( **kwargs )
            self.name = "cashQuiz"  # Default screen name fallback

try:
    from screen.cashGameSc import CashGameScreen
except ImportError:
    class CashGameScreen ( Screen ):
        def __init__(self , **kwargs):
            super ().__init__ ( **kwargs )
            self.name = "cashGame"  # Default screen name fallback

try:
    from screen.cashBackSc import CashBackScreen
except ImportError:
    class CashBackScreen ( Screen ):
        def __init__(self , **kwargs):
            super ().__init__ ( **kwargs )
            self.name = "cashBack"  # Default screen name fallback

try:
    from screen.cashVoucherSc import CashVoucherScreen
except ImportError:
    class CashVoucherScreen ( Screen ):
        def __init__(self , **kwargs):
            super ().__init__ ( **kwargs )
            self.name = "cashVoucher"  # Default screen name fallback
try:
    from screen.cashGameSc import CashVoucherScreen
except ImportError:
    class CashGameScreenen ( Screen ):
        def __init__(self , **kwargs):
            super ().__init__ ( **kwargs )
            self.name = "cashGames"  # Default screen name fallback


# Define the main application class
class CashTGoApp ( MDApp ):
    def build(self):
        # Initialize the screen manager
        screen_manager = ScreenManager ()

        # Add all the available screens to the screen manager
        screen_manager.add_widget ( StartScreen ( name = 'start' ) )
        screen_manager.add_widget ( LoginScreen ( name = 'login' ) )
        screen_manager.add_widget ( RegisterScreen ( name = 'register' ) )
        screen_manager.add_widget ( HomeAScreen ( name = 'homeA' ) )
        screen_manager.add_widget ( HomeBScreen ( name = 'homeB' ) )
        screen_manager.add_widget ( ScanScreen ( name = 'scan' ) )
        screen_manager.add_widget ( CashJourneyScreen ( name = 'cashJourney' ) )
        screen_manager.add_widget ( CashLottoScreen ( name = 'cashLotto' ) )
        screen_manager.add_widget ( Cash4GoodScreen ( name = 'cash4Good' ) )
        screen_manager.add_widget ( CashQuizScreen ( name = 'cashQuiz' ) )
        screen_manager.add_widget ( CashGameScreen ( name = 'cashGame' ) )
        screen_manager.add_widget ( CashBackScreen ( name = 'cashBack' ) )
        screen_manager.add_widget ( CashVoucherScreen ( name = 'cashVoucher' ) )
        screen_manager.add_widget ( CashGameScreen ( name = 'cashGames' ) )

        # Adding Scanner as a special screen
        screen_manager.add_widget ( Scanner ( name = 'scanbus' ) )

        # Return the screen manager as the app's root widget
        return screen_manager


# Entry point of the application
if __name__ == '__main__':
    CashTGoApp ().run ()