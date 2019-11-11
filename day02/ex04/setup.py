import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

    setuptools.setup(
            name="ai42",
            version="1.0.0",
            author="agelloz",
            author_email="agelloz@student.42.fr",
            description="package containing ft_progress and log functions",
            long_description=long_description,
            long_description_content_type="text/markdown",
            url="https://github.com/agelloz/42AI-python-bootcamp/tree/master/day02/ex04",
            packages=setuptools.find_packages(),
            classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            ],
            python_requires='>=3.7',
            )
