"""
Examples for python2.7
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


def example_3():
	import Queue  # thread safe
	import threading
	import time

	print """EXAMPLE 3
In this example, I created a Producer/Consumer type threaded setup,
using a Queue object to send tasks back and forth.
The 'tasks' are simple string literals, and processing is simply
outputing to stdout, but it's pretty obvious how to adapt such a
structure to be pretty flexible.
OUTPUT:"""
	
	def consumer_method(consumer_id, queue, channel_key):
		while True:
			try:
				string = queue.get_nowait()
			except Queue.Empty, e:
				# queue is now empty
				break
			
			# perform processing
			print "{0} thread processed:".format(consumer_id), string
			# issue an event over the passed channel
			pyback.publish(channel_key, task_data=string, consumer_id=consumer_id)
			# task processing.
			queue.task_done()

		return  # kills the thread

	def evt_handler(evt):
		# alert user to task processing
		print "Evt:"
		print "  task_data:", evt.task_data
		print "  consumer_id:", evt.consumer_id

	queue = Queue.Queue()
	queue.put('task1')
	queue.put('task2')
	queue.put('task3')
	queue.put('task4')
	queue.put('task5')
	queue.put('task6')

	channel_key = 'consumer_channel'
	pyback.subscribe(channel_key, evt_handler)

	# launch consumer
	# NOTE: thread2 is commented out because it makes use of
	# stdout, which is NON-THREAD-SAFE, causing output to be
	# out of order. To use stdout from within event handlers,
	# it will be necessary to use a thread-safe print method.

	thread = threading.Thread(target=consumer_method, args=('consumerID#1', queue, channel_key))
	#thread2 = threading.Thread(target=consumer_method, args=('consumerID#2', queue, channel_key))
	thread.start()
	#thread2.start()
	thread.join()
	#thread2.join()

	print "-" * 50


def example_4():
	print """EXAMPLE 4
In this example, we register a class method as
a handler for evt. Not too difficult, really.
OUTPUT:"""
	class Dummy(object):
		def __init__(self, channel_key):
			# the object subscribes itself to designated
			# channel on __init__. This could also be done
			# from outside the object scope desired.
			pyback.subscribe(channel_key, self.class_evt_handler)

		def class_evt_handler(self, evt):
			print "__channel:", evt.get_channel()
			print "evt name:", evt.name

	dum = Dummy('example_4_channel')
	# publish an event
	pyback.publish('example_4_channel', name='instantiated_handler_evt')
	# unregister from outside the object scope
	pyback.unsubscribe('example_4_channel', dum.class_evt_handler)
	# publish again, this one will be ignored, since handler
	# was unsubscribed
	pyback.publish('example_4_channel', name='instantiated_handler_evt2')


if __name__ == "__main__":
	example_1()
	example_2()
	example_3()
	example_4()