import os

from setuptools import setup


def required(requirements_file):
    """ Read requirements file and remove comments and empty lines. """
    with open(os.path.join(os.path.dirname(__file__), requirements_file),
              'r') as f:
        requirements = f.read().splitlines()
        return [pkg for pkg in requirements
                if pkg.strip() and not pkg.startswith("#")]


with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name='jarbas_lingua_franca',
    version='0.1.0',
    packages=['lingua_franca', 'lingua_franca.lang'],
    url='https://github.com/JarbasAl/lingua-franca',
    license='Apache2.0',
    include_package_data=True,
    install_requires=required('requirements.txt'),
    author='Jarbas AI',
    author_email='jarbasai@mailfence.com',
    description='Jarbas fork of Mycroft\'s multilingual text parsing and formatting library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
