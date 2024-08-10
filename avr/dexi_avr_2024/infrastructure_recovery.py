
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException

class InfrastructureRecovery(Node):
    def __init__(self):
        self.get_logger().info("InfrastructureRecovery Node is running")

def main(args=None):
    rclpy.init(args=args)
    try:
        node = InfrastructureRecovery()
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        node.destroy_node()
        rclpy.shutdown()
        sys.exit(1)

if __name__ == '__main__':
    main()
