import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'dexi_avr_2024'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='DroneBlocks',
    maintainer_email='db@droneblocks.io',
    description='ROS2 for AVR 2024 Drone Competition',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'infrastructure_recovery = dexi_avr_2024.infrastructure_recovery:main',
            'mock_publisher = dexi_avr_2024.mock_publisher:main',
            'mock_subscriber = dexi_avr_2024.mock_subscriber:main',
            'led_service = dexi_avr_2024.mock_led_service:main',
            'gpio_reader = dexi_avr_2024.mock_gpio_reader:main',
            'gpio_writer_service = dexi_avr_2024.mock_gpio_writer:main'
        ],
    },
)
