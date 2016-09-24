import smbus
import ctypes


class I2CBus(object):

    def __init__(self, bus_number, slaveAdr):
        self.bus = smbus.SMBus(bus_number)
        self.adr = slaveAdr

    def read_bit_data(self, adr, bit):
        byte = self.bus.read_byte_data(self.adr, adr)
        return (byte >> bit) & 1

    def read_byte_data(self, adr):
        return self.bus.read_byte_data(self.adr, adr)

    def read_word_data(self, adr):
        high_byte = self.bus.read_byte_data(self.adr, adr)
        low_byte = self.bus.read_word_data(self.adr, adr + 1)
        return (high_byte << 8) + low_byte

    def write_byte_data(self, adr, val):
        val = val & 0xff
        self.bus.write_byte_data(self.adr, adr, val)

    def write_bit_data(self, adr, bit, val):
        val &= 1
        byte = self.bus.read_byte_data(self.adr, adr)
        self.bus.write_byte_data(self.adr, adr, byte | (val << bit))


class MPU60X0(object):
    PWR_MGMT_1 = 0x6b
    TEMP_OUT = 0x41
    GYRO_XOUT = 0x43
    GYRO_YOUT = 0x45
    GYRO_ZOUT = 0x47
    ACCEL_XOUT = 0x3b
    ACCEL_YOUT = 0x3d
    ACCEL_ZOUT = 0x3f

    def __init__(self, bus_number, address):
        self.bus = I2CBus(bus_number, address)
        self.bus.write_byte_data(MPU60X0.PWR_MGMT_1, 0)
        self.accel_scale = 16384.0
        self.gyro_scale = 131.0
        self.temp_scale = 340.0
        self.temp_offset = 36.53

    def getGyroX(self):
        return self.bus.read_word_data(MPU60X0.GYRO_XOUT)/self.gyro_scale

    def getGyroY(self):
        return self.bus.read_word_data(MPU60X0.GYRO_YOUT)/self.gyro_scale

    def getGyroZ(self):
        return self.bus.read_word_data(MPU60X0.GYRO_ZOUT)/self.gyro_scale

    def getTemp(self):
        data = ctypes.c_int16(self.bus.read_word_data(MPU60X0.TEMP_OUT)).value
        return data / self.temp_scale + self.temp_offset

    def getAccelX(self):
        data = ctypes.c_int16(
            self.bus.read_word_data(MPU60X0.ACCEL_XOUT)).value
        return data / self.accel_scale

    def getAccelY(self):
        data = ctypes.c_int16(
            self.bus.read_word_data(MPU60X0.ACCEL_YOUT)).value
        return data / self.accel_scale

    def getAccelZ(self):
        data = ctypes.c_int16(
            self.bus.read_word_data(MPU60X0.ACCEL_ZOUT)).value
        return data / self.accel_scale

if __name__ == '__main__':
    sensor = MPU60X0(1, 0x68)

    print(sensor.getTemp())
    print(sensor.getGyroX())
    print(sensor.getGyroY())
    print(sensor.getGyroZ())
    print(sensor.getAccelX())
    print(sensor.getAccelY())
    print(sensor.getAccelZ())
