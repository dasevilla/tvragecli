#!/usr/bin/env python

PROJECT = 'tvragecli'

# Change docs/sphinx/conf.py too!
VERSION = '0.1'

# Bootstrap installation of Distribute
import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

from distutils.util import convert_path
from fnmatch import fnmatchcase
import os
import sys

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='Command line client for TV Rage',
    long_description=long_description,

    author='Devin Sevilla',
    author_email='dasevilla@gmail.com',

    url='https://github.com/dasevilla/tvragecli',
    download_url='https://github.com/dasevilla/tvragecli/tarball/master',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['distribute', 'cliff'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'tvrage = tvragecli.main:main'
            ],
        'tvrage.cli': [
            'epinfo = tvragecli.show:EpisodeInfo',
            'showinfo = tvragecli.show:ShowInfo',
            'eplist = tvragecli.list:EpisodeList',
            'search = tvragecli.list:ShowSearchList',
            ],
        },

    zip_safe=False,
    )
