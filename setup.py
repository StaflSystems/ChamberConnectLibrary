'''setup script for this module'''

from setuptools import setup

def readme():
    '''pull in the readme file for the long description'''
    with open('README.md') as rfile:
        return rfile.read()

setup(
    name='chamberconnectlibrary',       # should match the pkg folder
<<<<<<< HEAD
    version='1.0.1',                    # important for future updates
=======
    version='2.0.0',                    # important for future updates
>>>>>>> cclibrary-py3
    description='A library for interfacing with Espec North America chambers via Python 3.6+',
    long_description=readme(),          # loads the README.md file 
    url='https://github.com/EspecNorthAmerica/ChamberConnectLibrary',
    author='Paul Nong-Laolam',
    author_email='pnong-laolam@espec.com',
    license='MIT',
    packages=['chamberconnectlibrary'],
    install_requires=['pyserial', 'minimalmodbus'],
    zip_safe=False,
    keywords='Espec P300 P300vib SCP220 ES102 F4T F4',
    include_package_data=True,
<<<<<<< HEAD
    scripts=['bin/f4t_runTCP.py'],
=======
    scripts=['bin/f4t_runTCP.py', 'bin/p300vib_sample_run.py'],
>>>>>>> cclibrary-py3

    classifiers=[
        'Programming Language :: Python :: 3.7.3',
        'Programming Language :: Python :: 3.8.10',
        'Programming Language :: Python :: 3.9.3',
        'Programming Language :: Python :: 3.10.12',
    ],
<<<<<<< HEAD
)
=======
)
>>>>>>> cclibrary-py3
