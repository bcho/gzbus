# coding: utf-8

from setuptools import setup, find_packages

import gzbus


README = open('README.md').read()
CHANGES = open('CHANGES.md').read()


setup(
    name='gzbus',
    version=gzbus.__version__,

    author=gzbus.__author__,
    author_email=gzbus.__email__,
    url='https://github.com/bcho/gzbus',

    description='Guangzhou bus routine realtime tracking.',
    long_description='\n'.join((README, CHANGES)),
    license='MIT',

    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=[
        'lxml',
        'pyquery',
        'requests'
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ]
)
