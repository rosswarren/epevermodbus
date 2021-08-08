from setuptools import setup

setup(
    name="epevermodbus",
    version="0.0.4",
    description="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rosswarren/epevermodbus",
    author="Ross Warren",
    author_email="rosswarren4@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["epevermodbus"],
    include_package_data=True,
    install_requires=["minimalmodbus", "retrying"],
    entry_points={
        "console_scripts": [
            "epevermodbus = epevermodbus.command_line:main",
        ],
    },
)
