#!/usr/bin/env python3.8
from setuptools import setup, find_packages
setup(name='yezh',
      author='Julien Baley',
      url='https://github.com/julienbaley/yezh',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
      ],
      entry_points={
          'console_scripts': ['yezh = yezh.main:main',
                              ]
      },
      )
