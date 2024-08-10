#! /usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Hello ROS2")
        self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info("Hello " + str(self.counter_))

def main(args=None):
    rclpy.init(args=args)
    node = MyNode() # name for the node
    rclpy.spin(node) # pause the program and keep the programe running
    rclpy.shutdown()

if __name__ == "__main__":
    main()




# minimum code
# import rclpy
# from rclpy.node import Node

# def main(args=None):
#     rclpy.init(args=args)
#     node = Node("py_text") # name for the node
#     node.get_logger().info("Hello ROS2")
#     rclpy.spin(node) # pause the program and keep the programe running
#     rclpy.shutdown()

# if __name__ == "__main__":
#     main()


# #!/usr/bin/env python3
# import rclpy
# from rclpy.node import Node
 
 
# class MyCustomNode(Node): # MODIFY NAME
#     def __init__(self):
#         super().__init__("node_name") # MODIFY NAME
 
 
# def main(args=None):
#     rclpy.init(args=args)
#     node = MyCustomNode() # MODIFY NAME
#     rclpy.spin(node)
#     rclpy.shutdown()
 
 
# if __name__ == "__main__":
#     main()

