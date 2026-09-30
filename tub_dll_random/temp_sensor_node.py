import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Temperature
import random

class TempSensorNode(Node):
    def __init__(self):
        super().__init__('temp_sensor_node')
        self.publisher_ = self.create_publisher(Temperature, '/sensor/temperature', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.current_temp = 35.0
        self.heating = True
        self.get_logger().info('Temperature Sensor Node elindult.')

    def timer_callback(self):
        if self.heating:
            self.current_temp += 3.0 + random.uniform(-0.5, 0.5)
            if self.current_temp >= 75.0:
                self.heating = False
        else:
            self.current_temp -= 3.5 + random.uniform(-0.5, 0.5)
            if self.current_temp <= 38.0:
                self.heating = True

        msg = Temperature()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'temp_sensor_frame'
        msg.temperature = float(self.current_temp)
        msg.variance = 0.05

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publikalt homerseklet: {self.current_temp:.2f} °C')

def main(args=None):
    rclpy.init(args=args)
    node = TempSensorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
