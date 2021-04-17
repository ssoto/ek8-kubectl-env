import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="kubenv",
    version="0.0.3",
    author="Sergio",
    author_email="scots4ever@gmail.com",
    description="Cool utilies'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ssoto/ek8-kubectl-env",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=["bin/kubenv"],
)
