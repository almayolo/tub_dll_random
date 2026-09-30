import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'tub_dll_random'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Tuba Benedek',
    maintainer_email='tuba.benedek@example.com',
    description='ROS 2 kis beadando - Homerseklet felugyelet es hutesvezerles',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'temp_sensor_node = tub_dll_random.temp_sensor_node:main',
            'cooling_controller_node = tub_dll_random.cooling_controller_node:main',
        ],
    },
)
