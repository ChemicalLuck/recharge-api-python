
import codecs
import os
import re
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))


setup(
    name='recharge',
    version='1.0.0',
    author='Tobin Brown',
    author_email='tobin@bulugroup.com',
    packages=['recharge'],
    include_package_data=True,
    url='http://github.com/BuluBox/recharge-api',
    license='MIT',
    description='Python API Wrapper for Recharge',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],
    keywords='api recharge',
    long_description=open('README.rst', 'r').read(),
    install_requires=['requests'],
    zip_safe=False,
)