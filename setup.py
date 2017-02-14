from setuptools import setup
import os

def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read()


setup(
    name = "useragentx",
    version = "0.2.1",
    author = "Dan Temkin (just-dantastic)",
    author_email = "temkin.d01@gmail.com",
    description = ("A useragent spoofer supporting bot, mobile, and browser platforms"),
    license = "MIT",
    keywords = "useragent requests header spoofer",
    url = "https://www.github.com/just-dantastic/useragentx",
    packages=["useragentx"],
    long_description=read("README.md"),
    classifiers = [
        "Development Status :: 2 - Beta",
        "Topic :: Utilities",
        "License :: MIT License",
    ],
)

    
