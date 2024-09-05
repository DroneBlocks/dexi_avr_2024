This repo requires the DEXI core ROS2 components. Clone this into the ~/dexi_ws/src folder:

git clone --recurse-submodules https://github.com/DroneBlocks/dexi_avr_2024

Install dependencies:

rosdep update
sudo apt update
rosdep install --from-paths src -y --ignore-src

and build:

cd /home/dexi/dexi_ws
colcon build --packages-select apriltag_msgs
colcon build --packages-select apriltag_ros
colcon build --packages-select dexi_avr_2024

## Dev notes
From /Users/db/_dev/dexi/dexi_avr_2024_ws/src/dexi_avr_2024
docker run -p 6080:80 -p 9090:9090 --name=dexi-avr-dev --security-opt seccomp=unconfined -v ${PWD}:/dexi_avr_2024_ws/src/ --shm-size=512m droneblocks/dexi-px4-sitl:latest

## Calling the mock led service
