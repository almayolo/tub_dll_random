from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tub_dll_random',
            executable='temp_sensor_node',
            name='temp_sensor_node',
            output='screen'
        ),
        Node(
            package='tub_dll_random',
            executable='cooling_controller_node',
            name='cooling_controller_node',
            output='screen'
        ),
    ])
