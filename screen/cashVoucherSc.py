import os
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from Project_5.CashTGo.core.widgets import CustomRoundedCard
from Project_5.CashTGo.core.widgets2 import CustomRddCard
from Project_5.CashTGo.core.widgets import ShadowRoundedButton
from Project_5.CashTGo.core.color import cTx  # Import color
from kivy.clock import Clock

#Starting the Cash Voucher Screen

class CashVoucherScreen ( Screen ):
    def __init__(self , **kwargs):
        super ().__init__ ( **kwargs )

        # Background Image
        self.bg_image = Image ( source = 'assets/images/I1.png' , allow_stretch = True , keep_ratio = False )
        self.add_widget ( self.bg_image )

        # Layout
        layout = FloatLayout ()

        # Title Label
        title_label = Label (
            text = "Welcome to Zurich!\n Find services below" ,
            font_size = "28sp" ,
            # ...Other properties
            pos_hint = {"center_x": 0.5 , "top": 0.95} ,
        )
       # layout.add_widget ( title_label )

        # Back to Home Button
        back_home_card = ShadowRoundedButton (
            text = "Back" , font_size = "18sp" ,
            pos_hint = {"center_x": 0.5 , "center_y": 0.15} ,
        )
        back_home_card.bind ( on_press = self.go_to_home )
        layout.add_widget ( back_home_card )

        # Creating a card instance (ensure image_path passed properly)
        card_instance = CustomRddCard ( image_path = 'assets/images/Zurich.png' )

        # Add the card to display
        self.add_widget ( card_instance )

        # Add layout to the screen
        self.add_widget ( layout )

    def go_to_home(self , *args):
        # Navigation or home logic
        self.manager.current = 'homeA'