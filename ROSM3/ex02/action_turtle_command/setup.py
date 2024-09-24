from setuptools import find_packages, setup

package_name = 'action_turtle_command'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='arina',
    maintainer_email='a.glushchenko2@g.nsu.ru',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'action_turtle_server = action_turtle_command.action_server:main',
            'action_turtle_client = action_turtle_command.action_client:main',
        ],
    },
)
