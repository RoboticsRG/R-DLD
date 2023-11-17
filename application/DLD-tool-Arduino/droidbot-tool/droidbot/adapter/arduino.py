import serial
import time
import io

# dmesg | grep tty
# dmesg | tail
# chmod a+rw /dev/ttyUSB0
#


class Arduino:

    """
    Class for application communication with the Arduino robot
    """
    def __init__(self, port="/dev/ttyS0"):
        self.com  = serial.Serial('/dev/ttyUSB0', 9600)
        # self.com = serial.Serial(port=port, baudrate=9600, timeout=.1)
        self.sio = io.TextIOWrapper(io.BufferedRWPair(self.com, self.com))

    def read(self):
        time.sleep(2)
        output = self.com.readline().decode("utf-8")
        while len(output) > 0:
            print(output.strip('\n').strip('\r'))
            output = self.com.readline().decode("utf-8")

    def write(self, x):
        self.com.write(bytes(x).encode("utf-8"))
        time.sleep(0.05)


if __name__ == '__main__':
    ard = Arduino()
    cont = 0
    # ard.write("0")
    time.sleep(2)
    ard.write("1")
    time.sleep(2)
    ard.write("0")
    time.sleep(1)

    # while cont < 10:
    #
    #     cont +=1
    #     time.sleep(2)
    #     if cont % 2 != 0:
    #         print(0)
    #         ard.write("0")
    #     else:
    #         ard.write("1")
    #         print(1)
    #
    # time.sleep(2)
    # ard.write("2")
    # time.sleep(3)
