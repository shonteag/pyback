"""
pyback setup.py
Script used by distutils to setup and install the
pyback package.
"""

import sys

conf = dict(
	name='pyback',
	version='1.0.0',
	description='Pure-python module for thread-safe pub-sub operations.',
	long_description="""A pure-python module for thread-safe pubsub operations.

Source available from: https://github.com/shonteag/pyback""",
	author='Shonte Amato-Grill',
	author_email='shonte.amatogrill@gmail.com',
	url='https://github.com/shonteag/pyback',
	package_dir={'':'src'},
	py_modules=['pyback', 'test_pyback'],
	classifiers=[
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.7',
		'Development Status :: 4 - Beta'
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		],
	)


if __name__ == "__main__":
	try:
		from setuptools import setup
		conf['test_suite'] = "test_pyback"
	except ImportError:
		from distutils.core import setup

	setup(**conf)