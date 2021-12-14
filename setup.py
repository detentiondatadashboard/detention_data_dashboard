import setuptools

setuptools.setup(
    name="detention_data_dashboard",
    version="0.0.1",
    author="Lucas Olson, Trung-Anh Nguyen, Maddie Gaumer",
    email="lkolson@uw.edu",
    description="a dashboard of ICE enforcement data",
    install_requires=['docutils>=0.3'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/detentiondatadashboard/detention_data_dashboard",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
