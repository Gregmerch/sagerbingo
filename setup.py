from setuptools import setup
from setuptools import find_packages
import os

with open('requirements.txt') as f:
	install_requires = f.read().splitlines()

kw = dict(
	name='sagerbingo',
	version='0.1',
	description='A python module for playing Bingo during Sagers class',
	author='Greg Merchant',
	author_email='greg.merchant@gmail.com',
	install_requires = install_requires,
	packages=find_packages(),
	url=''
	)

setup(**kw)