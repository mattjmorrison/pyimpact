from setuptools import setup, find_packages


__version__ = '0.1.0'


setup(
    name='pyimpact',
    version=__version__,
    description="A lightweight development webserver for ImpactJS",
    author="amadeus / taddeimania",
    author_email="jtaddei@gmail.com",
    packages=find_packages(),
    install_requires=['pytool'],
    tests_require=['nose'],
    test_suite="nose.collector",
    entry_points={
        'console_scripts': {
            "startimpact = pyimpact.cmd:Main.console_script",
        }
    }
)

