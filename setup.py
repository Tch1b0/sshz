import setuptools


setuptools.setup(
    name="sshz",
    version="1.0",
    packages=setuptools.find_packages(),
    install_requires=["hcloud~=2.2.1", "readchar~=4.2.0"],
    py_modules=["sshz"],
    entry_points={
        "console_scripts": [
            "sshz = sshz:main",
        ],
    },
    include_package_data=True,
)
