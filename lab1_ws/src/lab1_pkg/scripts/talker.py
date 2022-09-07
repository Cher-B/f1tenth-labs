#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped

class Publisherz(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'drive', 10)
        self.timer_ = self.create_timer(2.0, self.findans)
    

    def findans(self):
        v=0.0
        d=0.0
        
        ack_msg = AckermannDriveStamped()
        ack_msg.drive.steering_angle = d
        ack_msg.drive.speed = v
        self.publisher_.publish(ack_msg)


def main(args=None):
    rclpy.init(args=args)
    talker = Publisherz()
    rclpy.spin(talker)
    talker.destroy_node()
    rclpy.shutdown()
    




if __name__ == '__main__':
    main()

