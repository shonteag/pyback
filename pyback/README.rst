======
PyBack
======
A pure-python pub-sub module for registering, subscribing, and publishing events via callback methods.  

:Version:
	1.0.0 as of (17 Aug 2015)
:Authors:
	Shonte Amato-Grill (`github`_)
:License:
	MIT
:Python:
	2.7 (working), 3.4 (working)

.. _github: https://github.com/shonteag

Goals
=====
1) Provide a simple, easy-to-use, interface for using pub/sub.  
2) Keep it simple.  
3) Make it thread safe. 

Installation & Setup
====================
**Installation**

1) Download the tarball
2) Extract to your ``site-packages`` directory (in virtualenv or otherwise)
3) ``$ python setup.py install``

**Testing**

If installed from source distribution, included unittests can be run via: ::

	.../pyback/src$ nosetests

Methods
=======
**Helper methods**. These do not need to be called,
but can help the user to manage open channels::
	open_channel('channel_name')
	close_channel('channel_name')

**Pub/Sub**.  These are the real meat of the module,
allowing a user to register an event handler to a channel
(denoted by a channel name of type str), unregister said
handler, and push an event across a channel to all (if any)
handlers on said channel::
	subscribe('channel_name', evt_handler_method)
	unsubscribe('channel_name', evt_handler_method)
	publish('channel_name', kwarg1=value1, kwarg2=value2, ...)

Objects
=======

**pyback.Evt(object)**

Event handlers must accept exactly one argument, which will
be of type::
	pyback.Evt(channel, **kwargs)

``**kwargs`` argument is dict ({}) with key, value pairs which
will be keyed to Evt's built-in ``__dict__``. For example: ::

	import pyback
	def evt_handler(evt):
		print evt.name
		print evt.an_int
	pyback.subscribe('test_channel', evt_handler)
	pyback.publish('test_channel', name="test_evt_name", an_int=42)


This snippet, if run, will output to console: ::

	test_evt_name
	42

The only reserved value that **may not** apear in kwargs passed via
a call to publish() is "__channel". Doing so will throw the exception::

	pyback.PybackError(Exception)


There is also a class method available for all instances of ``Evt`` which
allows user to retrieve the channel name (as a str) over which the event was passed: ::

	pyback.Evt.get_channel()


Examples
========

To view examples, download source directory or `view here on github`_.
There are several examples available, all are documented within the source code. To
run examples: ::

	$ python pyback_examples.py

*Please note* that while pyback is thread-safe, ``example_3()`` makes use of stdout
for 'processing' of tasks, which is *not* thread safe, which will cause text to be
jumbled if you add a second Consumer thread!

.. _view here on github: src/pyback_examples.py

