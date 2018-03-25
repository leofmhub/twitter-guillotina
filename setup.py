from setuptools import find_packages
from setuptools import setup


try:
    README = open('README.rst').read()
except IOError:
    README = None

setup(
    name='twitter_project',
    version="1.0.0",
    description='Testing guillotina with a post endpoint to twitter',
    long_description=README,
    install_requires=[
        'guillotina'
    ],
    author='Leonor Frias Moya',
    author_email='leonor.frias@gmail.com',
    url='',
    packages=find_packages(exclude=['demo']),
    include_package_data=True,
    tests_require=[
        'pytest',
    ],
    extras_require={
        'test': [
            'pytest'
        ]
    },
    classifiers=[],
    entry_points={
    }
)
