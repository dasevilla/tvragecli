from setuptools import setup, find_packages


with open('README.rst') as fp:
    long_description = fp.read()


setup(
    name='tvragecli',
    version='0.1.0',

    description='Command line client for TV Rage',
    long_description=long_description,

    author='Devin Sevilla',
    author_email='dasevilla@gmail.com',

    url='https://github.com/dasevilla/tvragecli',
    download_url='https://github.com/dasevilla/tvragecli/tarball/master',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Environment :: Console',
    ],


    install_requires=[
        'cliff',
        'cliff-tablib',
        'tvrage',
    ],

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'tvragecli = tvragecli.main:main'
        ],
        'tvrage.cli': [
            'epinfo = tvragecli.show:EpisodeInfo',
            'showinfo = tvragecli.show:ShowInfo',
            'eplist = tvragecli.list:EpisodeList',
            'search = tvragecli.list:ShowSearchList',
        ],
    },
)
