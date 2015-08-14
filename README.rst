======
PyBack
======
A pure-python pub-sub module for registering, subscribing, and publishing events via callback methods.
  License: MIT
  Version: 1.0.0 (as of 8/14/2015)
  Authors: Shonte Amato-Grill (<https://github.com/shonteag>)

Goals
-----
1) Provide a simple, easy-to-use, interface for using pub/sub.  
2) Keep it simple.  
3) Make it thread safe. (Needs testing!)  

Installation & Setup
--------------------
This is a single-file module, and requires no setup to use.
*Note* distutils (setup.py) may be implemented at some point, but simple download seems easier for a non-package.

.. code-block:: python
	import pyback
	pyback.open_channel('test_channel')