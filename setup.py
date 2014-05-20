#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='pyweather',
    version='0.1.0',
    description='The pyweather project is a Python based wrapper for the Weather.com, Yahoo! weather, and NOAA weather services.',
    long_description=readme + '\n\n' + history,
    author='Jonathan Whitaker',
    author_email='jon.b.whitaker@gmail.com',
    url='https://github.com/jon-whit/pyweather',
    packages=[
        'pyweather',
    ],
    package_dir={'pyweather':
                 'pyweather'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='pyweather',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)
