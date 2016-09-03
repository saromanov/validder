#!/usr/bin/env python

from setuptools import setup, find_packages
import sys

DESCRIPTION = ("Validation of items")
VERSION = __import__('validder').__version__

setup(
    name='Validder',
    version=VERSION,
    description=DESCRIPTION,
    author='Sergey Romanov',
    author_email='xxsmotur@gmail.com',
    url='https://github.com/saromanov/validder',
    license='MIT',
    platforms=["any"],
    packages=find_packages(),
    include_package_data=True,
    tests_require=['unittest'] if sys.version_info < (2, 7) else [],
    test_suite="validder.tests",
    install_requires=[],
    keywords=['validation', 'schema'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)