from setuptools import find_packages, setup

setup(
    name="aimnet",
    packages=find_packages(include=["aimnet"]),
    version="0.1",
    description="aimnet models and calculator",
    author="otayfuroglu",
    license="MIT",
    install_requires=["pyyaml"],
)
