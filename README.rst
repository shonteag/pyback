======
PyBack
======
A pure-python pub-sub module for registering, subscribing, and publishing events via callback methods.
**Under development**

Goals
-----
1) Provide a simple, easy-to-use, interface for using pub/sub.  
2) Keep it simple.  
3) Make it thread safe. (Needs testing!)  

Installation & Setup
--------------------
This is a single-file module, and requires no setup to use.  
*Note* distutils (setup.py) may be implemented at some point, but simple download seems easier for a non-package.

``python
import pyback
pyback.open_channel('my_new_channel')
``
