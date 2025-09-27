# Lab - Sensor data processing for mobile robots

### Participants will be able to:
- Interact with sensors.
- Understand the pipeline of ros2 or any middleware.
- Read and Process robot's data; sensors and actuators.


### Participants will learn:

1. How to connect to your mobile robot and make it move around. 
2. How to properly read and log sensors through ros interfaces and OOP programming. 


## Part 1 - Setting up your code

In this lab, you will complete the provided code ```motions.py``` to move the robot and collect data. 
For robot movement, you will be sending motion commands as velocities (twists). This means you will need to publish velocities over the ```/cmd_vel``` topic. 
For data collection from the IMU, the Lidar (laser scan), and the wheel encoders (odometry), you will be subscribing to ```/imu```, ```/scan```, and ```/odom```, respectively. 

- Find ```utilities.py``` and ```motions.py``` in the current branch (labOne), and download them.
- Open each script, and follow the TODO comments to implement the requirements corresponding to Parts 3 - 5 in this manual. You should replace each ```...``` in the script before you attempt running it.

To setup your code:
- Import the right types of messages needed (see ```motions.py```); to do so, you will need to check for message type and message components given the topic names and using ros2 commands ```ros2 topic info /topic_name``` and ```ros2 interface show message_type```, respectively, as covered in the tutorials. For online documentation of the messages (you need to select the ROS2 distro you are using)
  - https://index.ros.org/p/geometry_msgs/
  - https://index.ros.org/p/sensor_msgs/
  - https://index.ros.org/p/nav_msgs 
- Set up the publisher for the robot's motions;
- Create the QoS profile.
  
**Define the QoS profile variable based on whether you are using the simulation (Turtlebot 3 Burger) or the real robot (Turtlebot 4).**

**Use "ros2 topic info /odom --verbose" as explained in Tutorial 3.**

## Part 2 - Implement the motions

In this part, you need to implement 3 different motions for the robot:
- Circle;
- Spiral;
- Straight line.

Follow the comments in ```motions.py``` to implement these motions for the robot, there is one function for each of these motions. 


## Part 3 - Implement the data reading and logging
To read from the sensors (IMU, Lidar, wheel encoders), you need to:
- Subscribe to the topics these sensors are publishing data on;
- Create callback functions to log the data.

Follow the comments in the ```motions.py``` and ```utilities.py``` to complete the above functionalities. The loggers that save the data on csv files are already implemented for you.

## Part 4 - Execute on the robot and log the data
If all of the above is completed, you should now be ready to execute the code on the robot. Run each case one by one (circle, spiral, line) to log the data.
Log sufficient data for post processing and analysis. Make sure that the data is actually logged and saved.

First drive the robot to a sufficiently large space, then start your motion sequences. You can use undock and the teleop as you did in *Part 2*. Remember to dock your robot at the end of your tests.

To run your modifed ```motions.py``` script:
- Make sure you can still see your robot's topics before attempting to run your script. The critical topics are ```/scan``` and ```/odom```, make sure they are available by running ```ros2 topic echo /topic_name```  If not, re-visit *Part 1*.
- Open a terminal, go to your modified ```motions.py``` directory and run: ```python3 motion.py --motion line```

Test all motion sequences.


## Submission - Lab Report
Please prepare a written report in pdf format containing in the front page:
- Names (Family Name, First Name)
- UID

report the following:
- Screenshots of your ROS setup, program testing in Gazebo and Rviz, etc (follow the steps in this lab sheet).
- Screenshots of running the TurtleBot in house environment and the map you obtained (freely run your robot in the house)
- Your filled-in python codes (motion.py and utilities.py) with explanations.
- A brief discussion to show your understanding of the sensor information. Hint: you may leverage on the course material and the online documentation of the messages to better interpret your data.
## There are no minimum page limit or format requirements, but a more professional report could contribute to a higher mark for this lab exercise.
## Deadline: check the announcements in HKU Moodle.


