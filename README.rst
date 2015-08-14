======
PyBack
======
A pure-python pub-sub module for registering, subscribing, and publishing events via callback methods.
:Version: 1.0.0 (8/14/2015)
:Authors:
	Shonte Amato-Grill (<https://github.com/shonteag>)

Goals
-----
1) Provide a simple, easy-to-use, interface for using pub/sub.  
2) Keep it simple.  
3) Make it thread safe. (Needs testing!)  

.. code-block:: python
	import pyback
	pyback.open_channel('test_channel')