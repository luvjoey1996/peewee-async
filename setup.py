"""
aiopeewee = asyncio + peewee
https://github.com/05bit/python-aiopeewee
"""
from setuptools import setup, find_packages

__version__ = '0.0.1'

setup(
    name="aiopeewee",
    version=str(__version__),
    author="Alexey Kinev",
    author_email='rudy@05bit.com',
    url='https://github.com/05bit/python-aiopeewee',
    description=__doc__,
    license='Apache',
    zip_safe=False,
    install_requires=(
        'peewee',
        #'aiopg', # using dev version
    ),
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
)
