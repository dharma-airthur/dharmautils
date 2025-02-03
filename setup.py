from setuptools import setup, find_packages

setup(
    name="dharmautils",
    version="1.0",
    packages=find_packages(),
    install_requires=[
    ],
    author="Arthur Ferreira",
    author_email="arthur.ferreira@dharma-ai.com",
    description="Dharma utilities package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DharmaAI/dharmautils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
) 