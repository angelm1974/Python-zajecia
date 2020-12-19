import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pakiet_szkoleniowy", # Replace with your own username
    version="0.4.2",
    author="Mariusz Mol",
    author_email="mariusz980@gmail.com",
    description="Kilka przydatnych funkcji zwracających czas w różnych postaciach",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/angelm1974/Python-zajecia",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)