from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='payeezy',
    version='1.1.02',
    description='Unofficial Python 3 module to process basic(purchase and authorize) transactions with Payeezy',
    long_description=readme,
    url='https://github.com/lemmetry/payeezy',
    author='Artem Kisel',
    author_email='artem.a.kisel@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Office/Business :: Financial :: Point-Of-Sale',
    ],
    keywords='Payeezy purchase authorize transaction FirstData',
    packages=find_packages(),
    install_requires=[],
)
