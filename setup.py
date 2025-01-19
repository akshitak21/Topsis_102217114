from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Topsis_AkshitaKlair_102217114",
    version="0.0.1",
    author="Akshita Klair",
    author_email="aklair_be22@thapar.edu",
    url="https://github.com/akshitak21/Topsis_102217114",
    description="A python module for implementation of TOPSIS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas", "numpy"],
    entry_points={"console_scripts": ["Topsis_AkshitaKlair_102217114 = Topsis_AkshitaKlair_102217114.topsis:main"]},
)