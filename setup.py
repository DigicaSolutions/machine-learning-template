from setuptools import find_packages
from setuptools import setup

setup(
    name="machine-learning-pipeline",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "torch",
        "pandas",
        "matplotlib",
        "tensorboard",
        "black",
    ],
    author="Jakub Chojnacki",
)
