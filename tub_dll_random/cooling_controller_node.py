import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Temperature
from std_msgs.msg import Bool

class CoolingControllerNode(Node):
    def __init__(self):
        super().__init__('cooling_controller_node')
        
        self.subscription = self.create_subscription(
            Temperature,
            '/sensor/temperature',
            self.temp_callback,
            10
        )
        
        self.publisher_ = self.create_publisher(Bool, '/cooling/fan_state', 10)
        self.fan_on = False
        self.upper_threshold = 60.0
        self.lower_threshold = 45.0
        
        self.get_logger().info('Cooling Controller Node elindult (Be: 60 °C, Ki: 45 °C).')

    def temp_callback(self, msg: Temperature):
        temp = msg.temperature

        if not self.fan_on and temp >= self.upper_threshold:
            self.fan_on = True
            self.get_logger().warn(f'Kuszobertek tullepes ({temp:.2f} °C)! Ventilator BEKAPCSOLVA.')
        elif self.fan_on and temp <= self.lower_threshold:
            self.fan_on = False
            self.get_logger().info(f'Homerseklet normalizaldott ({temp:.2f} °C). Ventilator KIKAPCSOLVA.')

        status_msg = Bool()
        status_msg.data = self.fan_on
        self.publisher_.publish(status_msg)

def main(args=None):
    rclpy.init(args=args)
    node = CoolingControllerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
