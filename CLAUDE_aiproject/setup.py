from setuptools import setup, find_packages

setup(
    name="data-portfolio",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    # This tells setuptools where to find packages
    install_requires=[
        # List your project dependencies
        "pandas",
        "numpy",
        # Add other dependencies from requirements.txt
    ],
    python_requires=">=3.7",
    author="Your Name",
    description="Data Portfolio Project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
└── README.md