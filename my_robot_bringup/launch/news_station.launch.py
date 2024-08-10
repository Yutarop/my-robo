from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    robot_station_node_1 = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="robot_news_station_giskard", # change node name
    )

    robot_station_node_2 = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="robot_news_station_bb8", # change node name
    )

    robot_station_node_3 = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="robot_news_station_daneel", # change node name
    )

    robot_station_node_4 = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="robot_news_station_jander", # change node name
    )

    robot_station_node_5 = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="robot_news_station_c3po", # change node name
    )

    smartphone_node = Node(
        package="my_py_pkg",
        executable="smartphone",
        name="smartphone",
    )

    ld.add_action(robot_station_node_1)
    ld.add_action(robot_station_node_2)
    ld.add_action(robot_station_node_3)
    ld.add_action(robot_station_node_4)
    ld.add_action(robot_station_node_5)
    ld.add_action(smartphone_node)


    return ld