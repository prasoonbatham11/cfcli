from setuptools import setup, find_packages

setup(
    name='cf',
    include_package_data=True,
    packages=find_packages(),
    entry_points={'console_scripts': ['cf = cf.__main__:main']},
    install_requires=['requests','prettytable','bs4','colorama','numpy','mdv','html2text','gnuplotlib','termgraph'],
    python_requires='>=3.6',
    requires=['requests','prettytable','bs4','colorama','numpy','mdv','html2text','gnuplotlib','termgraph'],
    version='1.0.0',
    url='https://github.com/prasoonbatham11/cfcli',
    license='MIT',
    author='Prasoon Batham',
    author_email='prasoonbatham@gmail.com',
)
