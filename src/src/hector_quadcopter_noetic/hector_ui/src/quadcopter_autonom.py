#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math

class MoveToGoal:
    def __init__(self):
        rospy.init_node('move_to_goal', anonymous=True)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber('/ground_truth/state', Odometry, self.odometry_callback)

        self.current_position = (0, 0, 0)
        self.goal = (0, 0, 1)  # Hedef konum (x, y, z)
        self.rate = rospy.Rate(10)  # Hz

    def odometry_callback(self, msg):
        self.current_position = (msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z)

    def takeoff(self):
        takeoff_cmd = Twist()
        takeoff_cmd.linear.z = 1.0  # Yukarı doğru hareket
        for _ in range(5):  # 5 döngü boyunca yukarı hareket
            self.pub.publish(takeoff_cmd)
            self.rate.sleep()

    def move_to_goal(self):
        while not rospy.is_shutdown():
            twist = Twist()
            distance = math.sqrt((self.goal[0] - self.current_position[0])**2 +
                                 (self.goal[1] - self.current_position[1])**2 +
                                 (self.goal[2] - self.current_position[2])**2)

            if distance > 0.1:  # 10 cm'lik bir tolerans
                angle_to_goal = math.atan2(self.goal[1] - self.current_position[1], self.goal[0] - self.current_position[0])
                twist.linear.x = 0.5  # İleri hareket hızı
                twist.angular.z = angle_to_goal  # Hedefe yönelmek için açı
            else:
                twist.linear.x = 0
                twist.angular.z = 0
                rospy.loginfo("Hedefe ulaşıldı!")

            self.pub.publish(twist)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        mover = MoveToGoal()
        mover.takeoff()  # Kalkış
        mover.move_to_goal()  # Hedefe hareket
    except rospy.ROSInterruptException:
        pass
