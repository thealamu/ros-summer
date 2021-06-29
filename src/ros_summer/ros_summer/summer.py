import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64


class SummerNode(Node):
    def __init__(self):
        super().__init__("summer_node")
        self._logger = self.get_logger()
        self._sum = 0
        self.create_subscription(Int64, "count", self.summer_callback, 10)

    def summer_callback(self, msg):
        self._sum += msg.data
        self._logger.info(f"Total: {self._sum}")


def main():
    rclpy.init()
    rclpy.spin(SummerNode())
    rclpy.shutdown()


if __name__ == "__main__":
    main()
