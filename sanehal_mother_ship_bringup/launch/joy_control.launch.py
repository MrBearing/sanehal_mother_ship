from launch import LaunchDescription

from launch.actions import DeclareLaunchArgument

from launch.substitutions import (
    LaunchConfiguration,
    TextSubstitution,
)
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    launch_args = [
        DeclareLaunchArgument(
            'hw_type',
            default_value=TextSubstitution(text='DualSense')
        )
    ]
    joy_container = [
        ComposableNodeContainer(
            name='joy_container',
            package='rclcpp_components',
            executable='component_container',
            namespace='',
            composable_node_descriptions=[
                ComposableNode(
                    package='joy',
                    plugin='joy::Joy',
                    name='joy',
                    namespace='',
                ),
                ComposableNode(
                    package='p9n_node',
                    plugin='p9n_node::TeleopTwistJoyNode',
                    name='teleop_twist_joy_node',
                    namespace='',
                    remappings=[('/cmd_vel', '/diffbot_base_controller/cmd_vel_unstamped')],
                    parameters=[{
                        'hw_type': LaunchConfiguration('hw_type')
                    }],
                )
            ],
        ),
    ]
    ld = LaunchDescription(launch_args+joy_container)

    return ld