#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import numpy as np

i = 0

class Circle_moving(Node):
    def __init__(self):
        super().__init__('circle_moving')
        self.publisher_ = self.create_publisher(Twist, '/robot/cmd_vel', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        twist_msg = Twist()
        twist_msg.linear.x = 0.5  # линейная скорость вперед
        twist_msg.angular.z = 0.5  # угловая скорость для движения по кругу
        self.publisher_.publish(twist_msg)

class Eight_moving(Node):
    def __init__(self):
        super().__init__('eight_moving')
        self.publisher_ = self.create_publisher(Twist, '/robot/cmd_vel', 10)
        self.timer_period = 0.1
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

        # Параметры для движения по восьмерке
        self.angular_speed = 0.5  # Угловая скорость
        self.linear_speed = 0.5  # Линейная скорость
        self.direction = 1  # Направление поворота (1 - влево, -1 - вправо)
        self.time_elapsed = 0.0  # Время, прошедшее с начала движения
        self.half_period = 13.0  # Время, за которое робот проходит половину восьмерки

    def timer_callback(self):
        twist_msg = Twist()
        twist_msg.linear.x = self.linear_speed
        twist_msg.angular.z = self.angular_speed * self.direction

        # Обновляем время
        self.time_elapsed += self.timer_period

        # Меняем направление движения каждые half_period секунд
        if self.time_elapsed >= self.half_period:
            self.direction *= -1
            self.time_elapsed = 0.0  # Сбрасываем таймер

        self.publisher_.publish(twist_msg)


def main(args=None):
    rclpy.init(args=args)
    #node = Circle_moving()
    node = Eight_moving()
    rclpy.spin(node)  
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
