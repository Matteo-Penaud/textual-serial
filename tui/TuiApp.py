from textual.app import App
from textual.widgets import Footer

from .TuiSerialView import TuiSerialView


class TuiApp(App):
    CSS_PATH = "./style.tcss"
    serial = None

    def compose(self):
        yield Footer()

        yield self.serial_view

    def assign_serial(self, data_queue):
        self.serial_view = TuiSerialView(data_queue)
