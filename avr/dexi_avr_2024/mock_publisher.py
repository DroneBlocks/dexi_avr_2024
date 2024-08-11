import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from std_msgs.msg import String
from apriltag_msgs.msg import AprilTagDetection
from apriltag_msgs.msg import AprilTagDetectionArray
import random

class MockPublisher(Node):
    def __init__(self):
        super().__init__("mock_publisher")
        self.get_logger().info("Mock Publisher Node is running")

        self.infrared_beam_publisher = self.create_publisher(String, "infrared_beam", 10)
        timer_period = 0.5  # seconds
        self.infrared_beam_timer = self.create_timer(timer_period, self.infrared_beam_callback)
        self.i = 0

        self.april_tag_publisher = self.create_publisher(AprilTagDetectionArray, "detections", 10)
        self.april_tag_timer = self.create_timer(timer_period, self.april_tag_callback)
        self.i = 0

    def infrared_beam_callback(self):
        msg = String()
        msg.data = "Beam detected: %d" % self.i
        self.infrared_beam_publisher.publish(msg)
        self.i += 1

    def april_tag_callback(self):
        tag = AprilTagDetection()
        tag.family = "36h11"
        tag.id = random.randint(0, 10)
        tag.hamming = 0
        tag.goodness = 0.0
        tag.decision_margin = 30.0

        msg = AprilTagDetectionArray()
        msg.detections = [tag]
        
        self.april_tag_publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    try:
        mock_publisher_node = MockPublisher()
        rclpy.spin(mock_publisher_node)
    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        mock_publisher_node.destroy_node()
        rclpy.shutdown()
        sys.exit(1)

if __name__ == '__main__':
    main()
