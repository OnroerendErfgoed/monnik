#!/usr/bin/env python

import os
import sys

import monnik

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    'monnik',
]

requires = [
    'rfc3987',
    'requests',
]

setup(
    name='monnik',
    version='0.1.0-alpha.1',
    description='Library for easy querying of Flanders Heritage REST services.',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    author='Koen Van Daele',
    author_email='koen.vandaele@vlaanderen.be',
    url='http://github.com/onroerenderfgoed/monnik',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'monnik': 'monnik'},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)
