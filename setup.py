# -- coding: utf-8 --
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='xenith.org',
    version='0.0.1',
    author='',
    author_email='xenith@xenith.org',
    packages=[
        'xenith',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['xenith/manage.py'],
)
