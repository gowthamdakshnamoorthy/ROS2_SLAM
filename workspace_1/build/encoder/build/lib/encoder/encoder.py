#!/usr/bin/python3
import rclpy
import RPi.GPIO as GPIO
from example_interfaces.msg import Int16

#Defining the pins from RaspberryPi
a = 16
b = 18

#Setting Board mode and warnings
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Pin_Setup
GPIO.setup(a, GPIO.IN)
GPIO.setup(b, GPIO.IN)

pulse_a = GPIO.input(a)
pulse_b = GPIO.input(b)

rclpy.init()
node = rclpy.create_node('encoder_data_1_A')
node.get_logger().info("Right_Motor_Encoder_A_Publisher: Started")
pub = node.create_publisher(Int16, "RightMotorEncoderA", 10)
msg = Int16()
msg.data = pulse_a
while True:
	pub.publish(msg)

rclpy.spin(node)
rclpy.shutdown()
