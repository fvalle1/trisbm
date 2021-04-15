import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trisbm",
    version="0.3.0",
    author="Filippo Valle",
    author_email="filippo.valle@unito.it",
    description="Package to run triSBM model.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fvalle1/trisbm",
    packages=setuptools.find_packages(),
    py_modules=["hSBM_Topicmodel/sbmtm"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
    ],
    install_requires = ["numpy", "pandas", "matplotlib", "cloudpickle"],
    python_requires='>=3.6',
)
