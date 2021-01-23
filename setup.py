  
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bnmitml",
    version="0.0.1",
    author="Shreyas Bhaskar",
    author_email="shreyasb63@gmail.com",
    description="A small ml library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shreyas-Bhaskar/bnmitml",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
