import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="zoompy",
    version="1.0",
    author="Abhimanyu Bhadauria",
    author_email="abhimanyu2911@gmail.com",
    description="Get data from Ergast",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mnayu/zoompy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)