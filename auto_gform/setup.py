from setuptools import find_packages, setup

setup(
    name='auto_gform',
    packages=find_packages(include=['auto_gform']),
    version='0.1.0',
    description='Selenium wrapper for Google Forms',
    author='github.com/rys730',
    install_requires=['selenium>=4.6']
)