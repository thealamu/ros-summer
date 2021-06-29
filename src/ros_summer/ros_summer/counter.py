import rclpy
from rclpy.node import Node


class CountingNode(Node):
    def __init__(self):
        super().__init__("counting_node")
        self._logger = self.get_logger()
        self._count = 0
        self.create_timer(1.0, self.count_callback)

    def count_callback(self):
        self._logger.info(str(self._count))
        self._count += 1


def main():
    rclpy.init()
    rclpy.spin(CountingNode())
    rclpy.shutdown()


if __name__ == "__main__":
    main()
