from setuptools import setup, find_packages

try:
    long_desc = open('README.md').read()
except:
    long_desc = ''

setup(
    name="variablebutton",
    url="https://github.com/NamUserPerSu/variable-button-extension",
    author="NamUserPerSu",
    author_email="peter.skipper@gmail.com",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "jupyter==1"
    ],
    include_package_data=True,
    description="A button on Jupyter's toolbar for adding pre-configurated varible",
    long_description=long_desc,
)
