from setuptools import setup

setup(name='moviemon',
      version='1.0',
      description='All your movies inside the command line',
      url='https://github.com/iCHAIT/moviemon',
      author='Chaitanya Gupta',
      author_email='cgupta319@gmail.com',
      license='MIT',
      packages=['moviemon'],
      install_requires=[
                'guessit',
                'prettytable',
                'docopt'
            ],
      keywords=['movies', 'CLI', 'movies-within-CLI', 'python'],
      classifiers=[
          'Environment :: Console',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: Utilities',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: User Interfaces',
          'Topic :: Software Development :: Version Control',
      ],)
