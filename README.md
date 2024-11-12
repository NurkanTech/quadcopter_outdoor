# Quadcopter Control to Noetic & Gazebo

-Cloning process
```
git clone  https://github.com/NurkanTech/quadcopter_outdoor.git
```

If you have installed ros, the next steps:
1
```
cd ~/<yoursworkspace>
roscore
```
2.
```
roslaunch hector_quadrotor_gazebo quadrotor_empty_world.launch
```
3.
```
roslaunch hector_quadrotor_demo outdoor_flight_gazebo.launch
```
4.
```
roslaunch hector_quadrotor_demo outdoor_flight_gazebo_no_rviz.launch
```
5.
```
rosrun  hector_ui quadcopter_autonom.py
```

## Overview


https://github.com/user-attachments/assets/f11804fa-a317-49cc-a561-732099dfd99a

