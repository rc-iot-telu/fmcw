from distutils.core import setup

setup(
    name="fmcw",
    version="1.0.0",
    description="Application for reading OmniPresence Radar.",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/rc-iot-telu/fmcw",
    author="PUI-PT Intelligent Sensing IoT",
    license="Apache 2",
    classifiers=[
        "License :: OSI Approved :: Apache 2 License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["reader"],
    include_package_data=True,
    entry_points={"console_scripts": ["realpython=main:main"]},
)
