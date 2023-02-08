#!/usr/bin/env python3

from setuptools import setup

VERSION = '0.7.3'

packages = ['defillama2_fork']
requires = ['requests>=2.28.1', 'pandas>=1.4.4', 'numpy>=1.22.4']

with open('README.md', mode='r') as f:
    readme = f.read()

setup(
    name="defillama2_fork", 
    version=VERSION,
    description='Python client for DefiLlama API',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/songchul/defillama2_fork',
    author="Coin Data School",
    author_email="<coindataschool@gmail.com>",
    packages=packages,
    install_requires=requires, # dependencies    
    keywords=['python 3', 'defillama', 'api'],
    classifiers= [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
