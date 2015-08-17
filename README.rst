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

.. _github: https://github.com/shonteag

Goals
=====
1) Provide a simple, easy-to-use, interface for using pub/sub.  
2) Keep it simple.  
3) Make it thread safe. (Needs testing!)  

Installation & Setup
====================
This is a single-file module, and requires no setup to use.  
*Note* distutils (setup.py) may be implemented at some point, but simple download seems easier for a non-package.

Available Methods
=================
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
pyback.Evt()
------------
Event handlers must accept exactly one argument, which will
be of type::
	pyback.Evt(channel, **kwargs)

\*\*kwargs argument is dict ({}) with key, value pairs which
will be keyed to Evt's built-in __dict\__. For example: ::
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
	pyback.PybackError()

**Built-in methods**::
	pyback.Evt.get_channel()
