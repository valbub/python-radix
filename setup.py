# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='python-radix',
version='0.1.0',
description=' ... что-то там ...',
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
],
keywords='radix numbers',
packages=['radix'],
install_requires=[],
platforms=['Any'])