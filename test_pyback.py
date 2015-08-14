import unittest

class TestCase_Evt(unittest.TestCase):

	def test_Evt_init(self):
		import pyback
		kwargs = {'testval':42}
		evt = pyback.Evt('testchannel',**kwargs)
		self.assertEqual(evt.testval, 42)
		self.assertEqual(evt.get_channel(), 'testchannel')

	def test_static_sub_pub(self):
		import pyback
		self.called = 0
		def callback(evt):
			self.called += 1
			self.assertIsInstance(evt, pyback.Evt)
			self.assertEqual(evt.testval, 42)

		pyback.subscribe('testchannel', callback)
		pyback.publish('testchannel', testval=42)
		self.assertEqual(self.called, 1)

		# remove it
		pyback.unsubscribe('testchannel', callback)
		pyback.publish('testchannel', testval=42)
		self.assertEqual(self.called, 1)  # NOT 2

	def test_object_callback(self):
		import pyback
		class Dummy(object):
			def __init__(self):
				self.called = 0

			def object_callback(self, evt):
				self.called += 1

		dum = Dummy()
		pyback.subscribe('testchannel', dum.object_callback)
		pyback.publish('testchannel', thing='blah')
		self.assertEqual(dum.called, 1)
		pyback.unsubscribe('testchannel', dum.object_callback)

	def test_close_channel(self):
		import pyback
		self.called = 0
		def callback(evt):
			self.called += 1

		pyback.subscribe('testchannel', callback)
		pyback.publish('testchannel')
		self.assertEqual(self.called, 1)
		pyback.close_channel('testchannel')
		pyback.publish('testchannel')
		self.assertEqual(self.called, 1)  # NOT 2