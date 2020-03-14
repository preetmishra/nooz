import codecs
import os
from setuptools import find_packages, setup


def long_description():
    if not (os.path.isfile('README.md') and os.access('README.md', os.R_OK)):
        return ''

    with codecs.open('README.md', encoding='utf8') as f:
        return f.read()


linting_deps = [
    'mypy==0.761',
    'pycodestyle==2.5.0',
]

setup(
    name='nooz',
    version='0.1.0',
    description='Trending headlines right in your terminal.',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/preetmishra/nooz',
    author='Preet Mishra',
    author_email='ipreetmishra@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: End Users/Desktop',
        'Topic :: Internet',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',

        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5, <=3.8',
    keywords='news',
    packages=find_packages(),
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'nooz = nooz.run:main',
        ],
    },
    extras_require={
        'linting': linting_deps,
    },
    install_requires=[
        'mypy_extensions>=0.4',
        'requests>=2.23.0',
        'urwid==2.1.0',
        'urllib3>=1.25.8'
    ],
)