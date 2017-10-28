# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='easyds',
    version='0.1.0',
    description='Easy way for data science',
    long_description=readme,
    author='Yusuke Takeuchi',
    author_email='take.yusuke@gmail.com',
    install_requires=['numpy', 'pandas', 'cv2', 'matplotlib'],
    url='https://github.com/yusuke/easy-ds',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)

