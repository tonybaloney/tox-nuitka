from setuptools import setup

with open('README.rst') as readme:
    long_description = readme.read()

with open('HISTORY.rst') as history:
    history_txt = history.read()


_version = '0.0.1'

requirements = [
    'tox>=3.0.0',
    'nuitka',
]


def main():
    setup(
        name='tox-nuitka',
        description='A nuitka plugin for tox',
        long_description=long_description + '\n\n' + history_txt,
        version=_version,
        url='https://github.com/tonybaloney/tox-nuitka',
        license='MIT',
        platforms=['unix', 'linux', 'osx', 'cygwin', 'win32'],
        author='Anthony Shaw',
        classifiers=['Development Status :: 4 - Beta',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: POSIX',
                     'Operating System :: Microsoft :: Windows',
                     'Operating System :: MacOS :: MacOS X',
                     'Topic :: Software Development :: Testing',
                     'Topic :: Software Development :: Libraries',
                     'Topic :: Utilities',
                     'Programming Language :: Python',
                     ],
        # package_dir={'tox_nuitka': 'src/tox_nuitka'},
        packages=['tox_nuitka', ],
        py_modules=['tox_nuitka'],
        install_requires=[requirements],
        entry_points={'tox': ['nuitka = tox_nuitka.plugin']},
        tests_require=['pytest','pytest-mock']
    )


if __name__ == '__main__':
    main()
