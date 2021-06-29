import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64


class CountingNode(Node):
    def __init__(self):
        super().__init__("counting_node")
        self._logger = self.get_logger()
        self._count = 0
        self._publisher = self.create_publisher(Int64, "count", 10)
        self.create_timer(1.0, self.count_callback)

    def count_callback(self):
        self._logger.info(f"Counter: {self._count}")

        dt = Int64()
        dt.data = self._count
        self._publisher.publish(dt)

        self._count += 1


def main():
    rclpy.init()
    rclpy.spin(CountingNode())
    rclpy.shutdown()


if __name__ == "__main__":
    main()
