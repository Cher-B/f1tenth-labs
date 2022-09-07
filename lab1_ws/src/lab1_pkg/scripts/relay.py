#!/usr/bin/python3


import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped


class Subscriberz(Node):
    def __init__(self):
        super().__init__('relay')
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'drive_relay', 10)
        #self.timer_ = self.create_timer(2.0, self)
        self.subscription = self.create_subscription(AckermannDriveStamped, 'drive', self.lcallback, 10)
        self.subscription
        

        
    def lcallback(self,msg):
        msg.drive.speed=msg.drive.speed*3.0
        msg.drive.steering_angle=msg.drive.steering_angle*3.0
                   
        self.publisher_.publish(msg)

            
    
def main(args=None):
    rclpy.init(args=args)
    relay = Subscriberz()
    rclpy.spin(relay)
    relay.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    