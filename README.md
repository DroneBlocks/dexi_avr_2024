This repo requires the DEXI core ROS2 components. Clone this into the ~/dexi_ws/src folder:

git clone --recurse-submodules https://github.com/DroneBlocks/dexi_avr_2024

and build:

cd /home/dexi/dexi_ws
colcon build --packages-select apriltag_msgs
colcon build --packages-select apriltag_ros
colcon build --packages-select dexi_avr_2024