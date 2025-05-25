from multiprocessing import Process, Queue

from serial import Serial

from tui.TuiApp import TuiApp


def serial_handler(serial: Serial, queue: Queue) -> None:
    while True:
        line = serial.read()
        queue.put(line.decode("utf-8"))

    serial.close()
    queue.close()


def create_serial():
    port_name = "/dev/ttyUSB1"
    baudrate = 115_200
    serial = Serial(port=port_name, baudrate=baudrate)
    serial_queue = Queue()

    return Process(target=serial_handler, args=(serial, serial_queue)), serial_queue


if __name__ == "__main__":
    serial_process, serial_queue = create_serial()
    serial_process.start()

    app = TuiApp()
    app.assign_serial(serial_queue)
    app.run()
