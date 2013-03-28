#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['geodesy'],
    package_dir={'': 'src'},
    install_requires=['pyproj', 'rospy', 'unique_id'],
    )

setup(**d)