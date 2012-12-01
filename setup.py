from setuptools import setup, find_packages
from trybox import VERSION

setup(
    name='trybox',
    version=VERSION,
    description='TryBox',
    author='Sophilabs',
    author_email='contact@sophilabs.com',
    url='https://github.com/sophilabs/try-django',
    download_url='http://github.com/sophilabs/try-django/tarball/trybox-v{0}#egg=trybox'.format(VERSION),
    license='MIT',
    packages=find_packages(),
    scripts = ['trybox/bin/trybox-console.py'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
