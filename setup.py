import os.path
import sys

from setuptools import setup, find_packages

sys.path.insert(0, os.path.dirname(__file__))


def read(f):
    return open(f, "r", encoding="utf-8").read()


setup(
    name="django-states3",
    version="2.0.0",
    url="https://github.com/ulamlabs/django-states3",
    license="BSD",
    description="State machine for django models",
    long_description=read("README.rst"),
    author="Ulam Labs",  # Jonathan Slenders, Gert van Gool, Maarten Timmerman, Steven (rh0dium), Unleashed NV
    author_email="contact@ulam.io",
    packages=find_packages(exclude=['test*']),
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    project_urls={"Source": "https://github.com/ulamlabs/django-states3",},
)
