import smbus
import time
bus = smbus.SMBus(1)
address = 0x23


def write(value):
        bus.write_byte_data(address, value, 0)
        return -1

def range():
        range1 = bus.read_word_data(address, 0x10)
        range2 = range1 & 0xff00
        range3 = (range2 << 8)
        range4 = range2 | range1
        return range4

while True:
        time.sleep(0.7)
        rng = range()
        print rng

