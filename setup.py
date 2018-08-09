#!/usr/bin/env python

from setuptools import setup, find_packages


PACKAGE = 'torified_pip'

setup(
    name=PACKAGE,
    description='Always run pip via torify.',
    version='0.1',
    author='Nathan Wilcox',
    author_email='nejucomo+dev@gmail.com',
    license='GPLv3',
    url='https://github.com/nejucomo/{}'.format(PACKAGE),
    install_requires=[
        'pip >= 18.0',
    ],

    packages=find_packages(),
    entry_points={
        'console_scripts': [
            '{} = {}.main:main'.format(
                PACKAGE.replace('_', '-'),
                PACKAGE,
            )
        ],
    }
)
