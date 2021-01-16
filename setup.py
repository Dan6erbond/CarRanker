
from setuptools import setup, find_packages

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='CarRanker',
    version='1.0.0',
    url='https://github.com/Dan6erbond/CarRanker',
    author='RaviAnand Mohabir',
    author_email='moravrav@gmail.com',
    description='Car ranking web app with built - in webscraper to find your perfect car.',
    packages=find_packages(),
    install_requires=requirements,
)
