#! /usr/bin/env python

from __future__ import absolute_import, print_function, division
try:
    from setuptools import setup, find_packages
except ImportError:
    raise RuntimeError('No suitable version of setuptools detected.')
import re
import os
import codecs
import sys
import struct

try:
    import pip
except ImportError:
    pip = None

HERE = os.path.abspath(os.path.dirname(__file__))
# sys.path.insert(0, os.path.join(HERE, 'gkit'))

DEPENDENCY_LINKS = []

PYVER = sys.version_info
PYPLAT = sys.platform
PY2_MIN = (2, 7)
PY2_MAX = (2, 7)
PY3_MIN = (3, 4)
PY3_MAX = (3, 6)

###############################################################################


def is_python_64bit():
    return struct.calcsize("P") == 8


def read(*parts):
    with codecs.open(os.path.join(HERE, *parts), 'rb', 'utf-8') as f:
        return f.read()

META_FILE = read(*['gkit', '__about__.py'])


def find_meta(meta):
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),
        META_FILE, re.M
    )

    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))

setup(
    name='gkit_utils',
    version=find_meta('version'),
    url=find_meta('uri'),
    license=find_meta('license'),
    author=find_meta('author'),
    author_email=find_meta('email'),
    description=find_meta('summary'),
    maintainer=find_meta('author'),
    maintainer_email=find_meta('email'),
    keywords=['Tkinter', 'widgets'],
    long_description=read('README.rst'),
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    zip_safe=False,
    classifiers=[
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    include_package_data=True,
    test_suite='tests',
)
