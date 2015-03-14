#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of backstage-store.
# https://github.com/globoi/backstage-store

from setuptools import setup, find_packages

tests_require = [
    'ipdb',
]

setup(
    name='django-workdays',
    version='0.0.1',
    description='workdays is a django-app for manage workdays and goals quarter',
    keywords='workdays django goals',
    author='Rafael Floriano da Silva',
    author_email='rflorianobr@gmail.com',
    url='https://github.com/rfloriano/workdays',
    license='Proprietary',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Proprietary License',
        'Natural Language :: English',
        'Operating System :: Unix',
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: PyPy",
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django',
        'workdays',
    ],
    extras_require={
        'tests': tests_require,
    },
)
