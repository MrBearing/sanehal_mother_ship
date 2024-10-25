# Copyright 2020 ros2_control Development Team
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution,LaunchConfiguration
from launch.actions import DeclareLaunchArgument

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    rviz_config_file = PathJoinSubstitution(
        [FindPackageShare('sanehal_mother_ship_bringup'), 'config', 'diffbot.rviz']
    )

    # for debug
    # logger = LaunchConfiguration('log_level')
    launch_arg = DeclareLaunchArgument(
            'log_level',
            default_value=['debug'],
            description='Logging level',
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='log',
        arguments=[
            '-d', rviz_config_file,
            # '--ros-args', '--log-level', logger
        ],
    )

    nodes = [
        launch_arg,
        rviz_node
    ]

    ld  = LaunchDescription(nodes)
    return ld