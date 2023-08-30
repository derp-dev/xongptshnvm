from setuptools import setup
from setuptools import extension

setup(
  name='cloader',
  version='0.1',
  ext_modules=[extension('cloader', ['cloader.c'])],