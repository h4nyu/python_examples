import RPi.GPIO as GPIO
import time


class TA7291(object):

    def __init__(self, Vref, IN1, IN2):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Vref, GPIO.OUT)
        GPIO.setup(IN1, GPIO.OUT)
        GPIO.setup(IN2, GPIO.OUT)
        self.pwm = GPIO.PWM(Vref, 500)
        self.in1 = IN1
        self.in2 = IN2

    def run(self, speed):
        if speed > 0:
            self._cw(speed)
        elif speed < 0:
            self._ccw(speed)
        else:
            self.stop()

    def _cw(self, speed):
        GPIO.output(self.in1, 1)
        GPIO.output(self.in2, 0)
        self.pwm.start(abs(speed))

    def _ccw(self, speed):
        GPIO.output(self.in1, 0)
        GPIO.output(self.in2, 1)
        self.pwm.start(abs(speed))

    def brake(self):
        GPIO.output(self.in1, 1)
        GPIO.output(self.in2, 1)
        self.pwm.start(0)

    def stop(self):
        GPIO.output(self.in1, 1)
        GPIO.output(self.in2, 1)
        self.pwm.stop()

    def cleanup(self):
        self.pwm.stop()
        
        GPIO.cleanup()


if __name__ == '__main__':
    right_motor = TA7291(Vref=21, IN1=20, IN2=16)
    left_motor = TA7291(Vref=26, IN1=19, IN2=13)
    right_motor.run(100)
    left_motor.run(100)
    time.sleep(10)
    right_motor.cleanup()
    left_motor.cleanup()
