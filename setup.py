# coding: utf-8

from setuptools import setup, find_packages


__version__ = '0.1.1'
__author__ = 'hbc'
__email__ = 'bcxxxxxx@gmail.com'


README = 'Guangzhou bus routine realtime tracking.'


setup(
    name='gzbus',
    version=__version__,

    author=__author__,
    author_email=__email__,
    url='https://github.com/bcho/gzbus',

    description='Guangzhou bus routine realtime tracking.',
    long_description='Guangzhou bus routine realtime tracking',
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
