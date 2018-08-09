#!/usr/bin/env python

from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess


PACKAGE = 'torified_pip'
EXECUTABLE = PACKAGE.replace('_', '-')


class PostInstallCommand (install):
    def run(self):
        install.run(self)
        subprocess.check_call([EXECUTABLE])


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
            '{} = {}.main:main'.format(EXECUTABLE, PACKAGE),
        ],
    },

    cmdclass={
        'install': PostInstallCommand,
    },
)
