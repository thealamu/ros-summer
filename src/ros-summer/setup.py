from setuptools import setup

package_name = "ros-summer"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Faithfulness Alamu",
    maintainer_email="vaguemail369@gmail.com",
    description="ROS Summer",
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": ["counter = ros-summer.counter:main"],
    },
)
