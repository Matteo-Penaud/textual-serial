from textual import work
from textual.widgets import TextArea


class TuiSerialView(TextArea):
    read_only = True

    def on_mount(self) -> None:
        self.update_timer = self.set_interval(1 / 100, self.update_serial)

    @work(exclusive=True)
    async def update_serial(self) -> None:
        self.insert("Test")
