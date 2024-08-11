import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from std_msgs.msg import String
from apriltag_msgs.msg import AprilTagDetectionArray

class MockSubscriber(Node):
    
    def __init__(self):
        super().__init__("mock_subscriber")

        self.ir_beam_subscriber = self.create_subscription(String, "infrared_beam", self.infrared_beam_callback, 10)
        self.april_tag_subscriber = self.create_subscription(AprilTagDetectionArray, "detections", self.april_tag_callback, 10)

    def infrared_beam_callback(self, msg):
        self.get_logger().info("got beam message: {:s}".format(msg.data))

    def april_tag_callback(self, msg):
        self.get_logger().info("First tag id is: {:d}".format(msg.detections[0].id))

def main(args=None):
    rclpy.init(args=args)
    try:
        mock_subscriber_node = MockSubscriber()
        rclpy.spin(mock_subscriber_node)
    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        mock_subscriber_node.destroy_node()
        rclpy.shutdown()
        sys.exit(1)

if __name__ == '__main__':
    main()