# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='python-radix',
version='0.1.0',
description='A tool for conversion numbers from one base to another',
long_description=long_description,
url='https://github.com/valbub/python-radix',
author='valbub, yury-khrustalev',
license='MIT',
classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
],
keywords='radix numbers',
packages=['anyradix'],
install_requires=[],
platforms=['Any'])