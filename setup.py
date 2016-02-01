from setuptools import setup

setup(name='moviemon',
      version='1.0.10',
      description='Everything about your movies within the command line.',
      url='https://github.com/iCHAIT/moviemon',
      author='Chaitanya Gupta',
      author_email='cgupta319@gmail.com',
      license='MIT',
      packages=['moviemon'],
      entry_points={
               'console_scripts': ['moviemon=moviemon:main'],
           },
      install_requires=[
          'guessit<2',
          'terminaltables',
          'docopt',
          'tqdm',
          'colorama'
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
          'Programming Language :: Python :: 3.4',
          'Topic :: Utilities',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: User Interfaces',
          'Topic :: Software Development :: Version Control',
      ],)
