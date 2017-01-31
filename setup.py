#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from codecs import open
import os

name = 'fontstyle'
author = email = source = version = description = None

def read (*args):
	return open(os.path.join(*[os.path.dirname(__file__)] + list(args)), encoding = 'utf-8').read().strip()

for i in read(name, '__init__.py').splitlines():
	if i.strip().startswith('__version__'):
		version = i.split('=')[1].strip().replace('"', '').replace("'", '')
	elif i.strip().startswith('__author__'):
		author = i.split('=')[1].strip().replace('"', '').replace("'", '')
	elif i.strip().startswith('__email__'):
		email = i.split('=')[1].strip().replace('"', '').replace("'", '')
	elif i.strip().startswith('__source__'):
		source = i.split('=')[1].strip().replace('"', '').replace("'", '')
	elif i.strip().startswith('__description__'):
		description = i.split('=')[1].strip().replace('"', '').replace("'", '')
	elif None not in (version, author, email, source, description):
		break

setup(
	name = name,
	version = version,
	license = read('LICENSE'),
	description = description,
    long_description = read('README.rst'),
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
		'gellel', 'text'
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