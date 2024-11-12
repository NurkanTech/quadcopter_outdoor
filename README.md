# Quadcopter Control to Noetic & Gazebo

-Cloning process
```
git clone  https://github.com/NurkanTech/quadcopter_outdoor.git
```

If you have installed ros, the next steps:

```
cd ~/<yoursworkspace>
roscore
roslaunch hector_quadrotor_gazebo quadrotor_empty_world.launch
```
```
roslaunch hector_quadrotor_demo outdoor_flight_gazebo.launch
```
```
roslaunch hector_quadrotor_demo outdoor_flight_gazebo_no_rviz.launch
