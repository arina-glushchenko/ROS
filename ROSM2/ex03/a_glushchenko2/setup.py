from setuptools import find_packages, setup

package_name = 'a_glushchenko2'

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
    maintainer_email='a.glushchenko2@g,nsu,ru',
    description='Beginner client libraries tutorials practice package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = a_glushchenko2.my_node:main'
        ],
    },
)
