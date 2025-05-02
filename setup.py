from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Everyone',
    'License :: OSI Approved :: MIT License',
    'Operating System :: Microsoft :: Windows :: Windows 11',
    'Programming Language :: Python :: 3'
]

setup(
    name='pyclicker27',
    version='0.0.1',
    description='A simple and easy-to-use autoclicker library for Python',
    long_description=open('README.txt').read(),
    long_description_content_type='text/markdown',
    author='FJ27cool',
    license='MIT',
    classifiers=classifiers,
    keywords='autoclicker, python, automation',
    packages=find_packages(),
    install_requires=[
        'pywin32',
        'keyboard',
        'mouse',
        'pynput'
    ],
    python_requires='>=3.6',
    url='https://github.com/FJ27cool/pyclicker27'
)