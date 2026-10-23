from glob import glob
from setuptools import find_packages, setup

package_name = "front_camera_info"

setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        ("share/" + package_name + "/urdf", glob("urdf/*.urdf")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Dimitris",
    maintainer_email="dimitris@example.com",
    description="Template package for front camera information with the supplied sensor URDF.",
    license="Apache-2.0",
)
