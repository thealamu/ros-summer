import os
from glob import glob
from setuptools import setup

package_name = "ros_summer"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share", package_name), glob("launch/*.xml")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Faithfulness Alamu",
    maintainer_email="vaguemail369@gmail.com",
    description="ROS Summer",
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "counter = ros_summer.counter:main",
            "summer = ros_summer.summer:main",
        ],
    },
)
