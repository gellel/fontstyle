#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from codecs import open
import os

name = 'fontstyle'

author = email = source = version = license = description = None

with open('README.rst', encoding = 'utf-8') as f:
    readme = f.read().strip()

with open(os.path.join(name, '__init__.py'), encoding = 'utf-8') as f:
	for i in f:
		if i.strip().startswith('__version__'):
			version = i.split('=')[1].strip().replace('"', '').replace("'", '')
		elif i.strip().startswith('__author__'):
			author = i.split('=')[1].strip().replace('"', '').replace("'", '')
		elif i.strip().startswith('__email__'):
			email = i.split('=')[1].strip().replace('"', '').replace("'", '')
		elif i.strip().startswith('__source__'):
			source = i.split('=')[1].strip().replace('"', '').replace("'", '')
		elif i.strip().startswith('__license__'):
			license = i.split('=')[1].strip().replace('"', '').replace("'", '')
		elif i.strip().startswith('__description__'):
			description = i.split('=')[1].strip().replace('"', '').replace("'", '')
		elif None not in (version, author, email, source, description):
			break

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
		'logging', 'terminal', 'terminal colour', 'print', 
		'font', 'strings', 'fontstyle', 'style', 'styling',
		'gellel', 'text', 'output'
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