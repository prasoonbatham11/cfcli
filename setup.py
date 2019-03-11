from setuptools import setup, find_packages
import sys
from codecs import open
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='cfs',
    include_package_data=True,
    packages=find_packages(),
    entry_points={'console_scripts': ['cfs = cf.__main__:main']},
    install_requires=['requests','prettytable','bs4','colorama','numpy','mdv','html2text','gnuplotlib','termgraph','yaspin'],
    python_requires='>=3.6',
    requires=['requests','prettytable','bs4','colorama','numpy','mdv','html2text','gnuplotlib','termgraph','yaspin'],
    version='1.0.1',
    url='https://github.com/prasoonbatham11/cfcli',
    license='MIT',
    author='Prasoon Batham',
    author_email='prasoonbatham@gmail.com',
    description='Codeforces cli for lazy nerds who don\'t want to leave their cozy terminals.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['Codeforces','cli', 'command line', 'terminal'],
)
