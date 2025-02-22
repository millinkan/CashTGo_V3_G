from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from Training_1.Project_5.CashTGo.core.color import cTx

class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Background image
        self.bg_image = Image(source='assets/images/I1.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.bg_image)

        # Title label (example)
        self.title_label = Label(
            text="Screen Title",
            font_size="28sp",
            color=cTx,
            halign="center",
            valign="middle",
            pos_hint={"center_x": 0.5, "top": 0.95}
        )
        self.add_widget(self.title_label)