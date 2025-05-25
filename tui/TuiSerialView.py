from multiprocessing import SimpleQueue

from textual import work
from textual.widgets import TextArea


class TuiSerialView(TextArea):
    read_only = True

    def __init__(self, data_queue: SimpleQueue = SimpleQueue()):
        self.data_queue = data_queue

        super().__init__()

    def on_mount(self) -> None:
        self.border_title = "Serial"
        self.update_timer = self.set_interval(1 / 100, self.update_serial)

    @work(exclusive=True)
    async def update_serial(self) -> None:
        if not self.data_queue.empty():
            self.insert(self.data_queue.get())
