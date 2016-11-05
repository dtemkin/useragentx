from setuptools import setup
import os

def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read()


setup(
    name = "useragentx",
    version = "0.1",
    author = "Dan Temkin",
    author_email = "temkin.d01@gmail.com",
    description = ("A useragent spoofer supporting bot, mobile, and browser platforms"),
    license = "MIT",
    keywords = "useragent requests header spoofer",
    url = "https://www.github.com/just-dantastic/useragent-spoofer",
    packages = ['useragentx'],
    long_description=read("README.md"),
    classifiers = [
        "Development Status :: 1 - Alpha",
        "Topic :: Utilities",
        "License :: MIT License",
    ],
)

    
