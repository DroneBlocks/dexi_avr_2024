import sys
import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
# import RPi.GPIO as GPIO
from std_msgs.msg import Bool

DEXI_GPIO_PINS = (
    16,
    17,
    20,
    21,
    22,
    23,
    24
)

class MockGPIOReader(Node):

    def __init__(self):
        super().__init__('gpio_reader')
        self.declare_parameter('pin', rclpy.Parameter.Type.INTEGER)
        self.gpio_pin = self.get_parameter('pin').value
        self.publisher = self.create_publisher(Bool, "gpio_input_{0}".format(str(self.gpio_pin)), 10)
        self.timer = self.create_timer(1, self.timer_callback)

        self.pin_state = False

        # Configure with BCM pin numbering
        # GPIO.setmode(GPIO.BCM)

        # Disable warnings
        # GPIO.setwarnings(False)

        # Setup the pin as input with pull up resistor
        # TODO: make pull up/down configurable
        # GPIO.setup(self.gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def timer_callback(self):
        # pin_state = bool(GPIO.input(self.gpio_pin))
        self.pin_state = not self.pin_state
        msg = Bool()
        msg.data = self.pin_state # Toggle the gpio value
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    try:
        gpio_reader = MockGPIOReader()
        rclpy.spin(gpio_reader)
    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        # GPIO.cleanup()
        gpio_reader.destroy_node()
        rclpy.shutdown()
        sys.exit(1)

if __name__ == '__main__':
    main()