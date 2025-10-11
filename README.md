# Lab - Closed loop control of mobile robots

## Introduction 

By the end of this lab, participants will be able to:
- Use the position data in a controller;
- Control a mobile robot using a tunable PID controller.
- Implement pure pursuit controller


#### The summary of what you should learn is as following:

1. You will learn how to properly read and log position sensors using ROS2.
2. You will write a PID controller class that can properly calculate derivate, and integral of your position sensor.
3. You use the PID controller to perform two trajectories with the mobile robot while logging the error. Then, a report should be prepared comparing the P and PID controllers in 
    * **agility** (how quickly a control system responds to changes in the desired setpoint), 
    * **accuracy** (the ability of the control system to reach and maintain the desired setpoint without steady-state error), and
    * **overshoot** (the amount by which a system overshoots the desired setpoint in its initial response).

## Submission - Lab Report
Please prepare a written report in pdf format containing personal details in the front page:
- Names (Family Name, First Name)
- UID

report the following:
- Your updated codes with explanations (i.e., how the parameters change the performance accordingly?)
- A brief discussion to show your understanding of the closed loop control. Hint: you may leverage on the course material and the online documentation of PID control to better interpret your elaborations.
## There are no minimum page limit or format requirements, but a more professional report could contribute to a higher mark for this lab exercise.
## Deadline: check the announcements in HKU Moodle.


