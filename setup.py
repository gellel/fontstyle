#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from codecs import open
import os

name = 'fontstyle'
author = email = source = version = description = None

with open(os.path.join(name, '__init__.py'), encoding = 'utf-8') as f:
	for line in f:
		if line.strip().startswith('__version__'):
			version = line.split('=')[1].strip().replace('"', '').replace("'", '')
		elif line.strip().startswith('__author__'):
			author = line.split('=')[1].strip().replace('"', '').replace("'", '')
		elif line.strip().startswith('__email__'):
			email = line.split('=')[1].strip().replace('"', '').replace("'", '')
		elif line.strip().startswith('__source__'):
			source = line.split('=')[1].strip().replace('"', '').replace("'", '')
		elif line.strip().startswith('__description__'):
			description = line.split('=')[1].strip().replace('"', '').replace("'", '')
		elif None not in (version, author, email, source, description):
			break

with open('README.rst', encoding = 'utf-8') as f:
    readme = f.read().strip()

with open('LICENSE', encoding = 'utf-8') as f:
	license = f.read().strip()

setup(
	name = name,
	version = version,
	license = license,
	description = description,
    long_description = readme,
	author = author,
	author_email = email,
	url = source,
	include_package_data = True,
	packages = [name],
	install_requires = ['setuptools'],
	keywords = [
		'ansi', 'color', 'colour', 'console', 'formatting', 
		'logging', 'terminal', 'terminal colour', 
		'font', 'strings', 'fontstyle', 'style'
	],
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Intended Audience :: Information Technology',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Text Processing',
		'Topic :: Text Processing :: Filters',
		'Topic :: Text Processing :: Fonts',
		'Topic :: Text Processing :: General',
		'Topic :: Text Processing :: Markup'
    ]
)