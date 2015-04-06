# encoding: utf-8
import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='python-freemail',
    version='0.0.1',
    packages=find_packages(exclude=('test',)),
    include_package_data=True,
    license='BSD License',
    description='A database of free and disposable email domains and a handy python module for querying it.',
    long_description=README,
    url='https://github.com/idonethis/freemail/',
    author='Björn Andersson',
    author_email='ba@sanitarium.se',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
