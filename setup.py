
import codecs
import os
import re
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='recharge-api',
    version='1.1.0',
    author='ChemicalLuck',
    author_email='chemicalluck@outlook.com',
    packages=['recharge'],
    include_package_data=True,
    url='http://github.com/ChemicalLuck/recharge-api',
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
    long_description=long_description,
    install_requires=['requests'],
    zip_safe=False,
    python_requires=">=3.6"
)