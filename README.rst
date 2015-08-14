PyBack
-----------------
A pure-python pub-sub module for registering, subscribing, and publishing events via callback methods.
:Version: 1.0.0 (8/14/2015)
:Authors:
	Shonte Amato-Grill (`github <https://github.com/shonteag`_)

**Goals**
1) Provide a simple, easy-to-use, interface for using pub/sub.  
2) Keep it simple.  
3) Make it thread safe. (Needs testing!)  

**Python versions**
2.7 - Tested and working.
*Needs testing on other python versions, although I anticipate that it will work due to very low requirements*

**Use**
Several static methods available for use:
... code-block:: python
	open_channel(channel_key)
	close_channel(channel_key)

	subscribe(channel_key, handler_method)
	unsubscribe(channel_key, handler_method)
	publish(channel_key, **kwargs)

