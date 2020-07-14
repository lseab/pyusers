from distutils.core import setup

setup(
	name='pyusers',
      	version='1.0.0',
      	description='user registration in python',
      	author='Luke Seabright',
      	author_email='luke.seabright@gmail.com',
      	url='https://github.com/lseab/pyusers',
      	packages=['pyuser', 'pyuser.db'],
		install_requires=[],
		extras_require={'test': ['pytest==5.4.3']},
)