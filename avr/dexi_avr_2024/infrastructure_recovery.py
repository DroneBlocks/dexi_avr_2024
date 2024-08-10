import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException

# /avr/fire_laser
# /avr/detect_beam

    # Listen for tag detections to determine where failures are and light up LED white
    # Look for IR signal to determine which color connex AVR drone should pick up
    # Light up LED based on tag id
    # Listen for IR signal
    # Light up LED based on IR signal
    # Fire laser

class InfrastructureRecovery(Node):
    def __init__(self):
        super().__init__('avr_node')
        self.get_logger().info("InfrastructureRecovery Node is running")

    
    
def main(args=None):
    rclpy.init(args=args)
    try:
        avr_node = InfrastructureRecovery()
        rclpy.spin(avr_node)
    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        avr_node.destroy_node()
        rclpy.shutdown()
        sys.exit(1)

if __name__ == '__main__':
    main()
