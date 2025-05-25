from multiprocessing import Event, Process, SimpleQueue

from serial import Serial

from tui.TuiApp import TuiApp


class SerialHandler(Process):
    queue = SimpleQueue()
    _stop_event = Event()

    def open_serial(self, port: str, baudrate: int):
        self.serial: Serial = Serial(port=port, baudrate=baudrate)

    def stop(self) -> None:
        self.serial.cancel_read()
        self.serial.close()
        self.queue.close()
        self._stop_event.set()

    def run(self) -> None:
        while not self._stop_event.is_set():
            line = self.serial.read(1)
            self.queue.put(line.decode("ascii"))


if __name__ == "__main__":
    serial_process = SerialHandler()
    serial_process.open_serial("/dev/ttyUSB1", 115_200)
    serial_process.start()

    app = TuiApp()
    app.assign_serial(serial_process.queue)
    app.run()
    serial_process.stop()
