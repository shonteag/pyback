import unittest

class TestCase_Evt(unittest.TestCase):

    def test_Evt_init(self):
        import pyback
        kwargs = {'testval':42}
        evt = pyback.Evt('testchannel',**kwargs)
        self.assertEqual(evt.testval, 42)
        self.assertEqual(evt.get_channel(), 'testchannel')

class TestCase_StaticMethods(unittest.TestCase):

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

    def test_two_publishers_one_subscriber(self):
        import pyback

        self.called = 0
        def callback(evt):
            self.called += 1

        pyback.subscribe('testchannel', callback)
        pyback.publish('testchannel')
        self.assertEqual(self.called, 1)
        pyback.publish('testchannel')
        self.assertEqual(self.called, 2)
        pyback.unsubscribe('testchannel', callback)

    def test_one_publisher_two_subscribers(self):
        import pyback

        self.called1 = 0
        self.called2 = 0

        def callback1(evt):
            self.called1 += 1
        def callback2(evt):
            self.called2 += 1

        pyback.subscribe('testchannel', callback1)
        pyback.subscribe('testchannel', callback2)

        pyback.publish('testchannel')

        self.assertEqual(self.called1, 1)
        self.assertEqual(self.called2, 1)

        pyback.unsubscribe('testchannel', callback2)

        pyback.publish('testchannel')

        self.assertEqual(self.called1, 2)
        self.assertEqual(self.called2, 1)