from setuptools import setup, find_packages

setup(
    name="change",
    version='0.1',
    install_requires=["click"],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points='''
        [console_scripts]
        change=change.app:main
    ''',
)
