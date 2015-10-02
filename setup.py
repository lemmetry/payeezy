from setuptools import setup, find_packages


setup(
    name='payeezy',
    version='1.0.4',
    description='Unofficial Python 3 module to process basic(purchase and authorize) transactions with Payeezy',
    url='https://github.com/lemmetry/payeezy',
    author='Artem Kisel',
    author_email='artem.a.kisel@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Topic :: Office/Business :: Financial :: Point-Of-Sale',
    ],
    keywords='Payeezy purchase authorize transaction FirstData',
    packages=find_packages(),
    install_requires=[],
)
