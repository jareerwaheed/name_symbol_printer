from setuptools import setup, find_packages

setup(
    name="name_symbol_printer",
    version="1.0.0",
    author="Jareer Waheed",
    author_email="jareerwaheed257@example.com",
    description="A library to print names using symbols in a stylized form.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jareerwaheed/name_symbol_printer",  # Update with your GitHub URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
