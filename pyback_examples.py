"""
Several examples that demonstrate use of pyback module.
"""

import pyback


def example_1():
	print """EXAMPLE 1
1) Register a new handler.
2) Publish to channel.
3) Unsubscribe handler from channel.
OUTPUT:"""
	def evt_handler(evt):
		# do something with evt here.
		# For sake of argument (haha, get it?), we will
		# print a custom passed kwarg called "name".
		print "__channel:", evt.get_channel()
		print "name:", evt.name

	pyback.subscribe('example_1_channel', evt_handler)

	# now this could be launched from anywhere that
	# imports the pyback module:
	pyback.publish('example_1_channel', name="example_1_event")
	pyback.unsubscribe('example_1_channel', evt_handler)

	print "-" * 50

def example_2():
	print """EXAMPLE 2
1) Open a new channel.
2) Register a new handler to that channel.
3) Register a second handler to the same channel,
   but with a different handling method.
4) Publish to that channel.
5) Close the channel entirely.
6) Publish to same channel. (No output from this one)
OUTPUT:"""
	def evt_handler1(evt):
		print "evt_handler1:"
		print "  __channel:", evt.get_channel()
		print "  name:", evt.name
	def evt_handler2(evt):
		print "evt_handler2:"
		print "  __channel:", evt.get_channel()
		print "  name:", evt.name
		print "  int_arg:", evt.int_arg

	pyback.open_channel('example_2_channel')
	pyback.subscribe('example_2_channel', evt_handler1)
	pyback.subscribe('example_2_channel', evt_handler2)

	# push from anywhere that imports pyback
	pyback.publish('example_2_channel', name="example_2_evt", int_arg=10)

	# close the channel entirely.
	# this automatically unsubscribes all event handlers on this channel.
	pyback.close_channel('example_2_channel')

	# this will cause no callback
	pyback.publish('example_2_channel', name="example_2_evt_fail", int_arg=20)

	print "-" * 50

if __name__ == "__main__":
	example_1()
	example_2()