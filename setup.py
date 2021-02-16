"""Package setup"""
import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

requirements = ["halo", "requests", "click", "tabulate", "rich<=7.1.0"]

setuptools.setup(
    name="good-first-issues",
    version="2.1.0",
    author="Yankee Maharjan",
    author_email="yankee.exe@gmail.com",
    url="https://github.com/yankeexe/good-first-issues",
    description="Find good first issues right from your CLI!",
    license="MIT",
    packages=setuptools.find_packages(exclude=["dist", "build", "*.egg-info"]),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    entry_points={"console_scripts": ["gfi = good_first_issues.main:cli"]},
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
    ],
)
