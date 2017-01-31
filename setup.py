#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
import os

name = 'fontstyle'
author = email = source = version = None

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
        elif None not in (version, author, email, source):
            break

setup(
	name = name,
	version = str(version),
	license = str(license),
	description = 'Formats strings for output in terminal.',
	author = str(author),
	author_email = str(email),
	url = str(source),
	keywords = ['ansi', 'color', 'colour', 'console', 'formatting', 
		'logging', 'terminal', 'terminal colour', 'font', 'strings', 'fontstyle', 'style'],
	packages = [name],
	install_requires = ['setuptools'],
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