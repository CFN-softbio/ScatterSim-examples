#!/usr/bin/env python
# to install:
# python setup.py install

import setuptools
from distutils.core import setup, Extension
#from setupext import ext_modules
#import versioneer
import numpy as np
import os

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
#def read(fname):
    #return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='ScatterSim_examples',
    #version=versioneer.get_version(),
    #cmdclass=versioneer.get_cmdclass(),
    author='Kevin Yager',
    description="Examples of how to run ScatterSim",
    packages=setuptools.find_packages(exclude=['doc']),
    include_dirs=[np.get_include()],
    install_requires=['six', 'numpy'],  # essential deps only
#    ext_modules=ext_modules,
    keywords='Xray Analysis Meso Cluster Powder Diffraction SAXS',
    license='BSD',
    )

