#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-artificer',
    version='0.1.0',
    author='Vishal Singh Kushwaha',
    author_email='vishal.02jan@gmail.com',
    maintainer='Vishal Singh Kushwaha',
    maintainer_email='vishal.02jan@gmail.com',
    license='MIT',
    url='https://github.com/vishal-kushwaha/pytest-artificer',
    description='A pytest plugin for API testing using OpenAPI Specification',
    long_description=read('README.rst'),
    py_modules=['pytest_artificer'],
    python_requires='>=3.7',
    install_requires=['pytest>=5.4.3'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'artificer = pytest_artificer',
        ],
    },
)
