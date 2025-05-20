from textual.app import App
from textual.widgets import Footer

from .TuiSerialView import TuiSerialView


class TuiApp(App):
    CSS_PATH = "./style.tcss"

    def compose(self):
        yield Footer()

        self.serial_view = TuiSerialView()
        yield self.serial_view

    def on_mount(self):
        self.serial_view.border_title = "Serial_name"
        self.serial_view.border_subtitle = "On /dev/tty/USBx"
