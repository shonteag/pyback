"""
Module  :: pyback
License :: MIT

A pure-python pub-sub module for registering,
subscribing, and publishing events.
"""

# CHANNELS tracks the publisher channels.
#   'channel_key':[callback_function1, callback_function2, ...]
_CHANNELS = {}


class PybackError(Exception):
    pass


class Evt(object):
    """
    Instantiates an event to be passed to
    registered callback function(s).

    channel is the channel_key upon which
    the event was triggered

    kwargs is dict of keyword args to be
    set as Evt attributes. It may not include
    the keyword "channel".
    """
    def __init__(self, channel, **kwargs):
        # check to make sure there are no name
        # conflicts.
        if '__channel' in kwargs:
            raise PybackError("'__channel' is reserved keyword.")
            return

        for k, v in kwargs.items():
            self.__channel = str(channel)
            setattr(self, k, v)

    def get_channel(self):
        return self.__channel


# Channel controls
def open_channel(channel_key):
    """
    Static method for creating a new channel.
    """
    channel_key = str(channel_key)

    if channel_key in _CHANNELS:
        raise PybackError("Channel already exists.")
    else:
        _CHANNELS[channel_key] = []


def close_channel(channel_key):
    """
    Static method for closing an entire channel.
    This will even close currently running pub/subs
    and no events will be passed along the channel.
    """
    channel_key = str(channel_key)

    if channel_key not in _CHANNELS:
        raise PybackError("Channel does not exist.")
    else:
        _CHANNELS.pop(channel_key)


# Pub/subs
def subscribe(channel_key, func_call):
    """
    Static method for subscribing to a channel.

    If the channel does not exist, it will be
    added to _CHANNELS.
    If it does exist, func_call will be added to
    list of callback_functions in _CHANNELS.

    func_call argument should be a method name
    that accepts a single argument (event).
    If func_call is already subscribed, it will
    NOT be subscribed twice.
    """
    channel_key = str(channel_key)

    # if the subscribing to channel_key does not
    # exist, add it, along with the function call.
    if channel_key not in _CHANNELS:
        _CHANNELS.update({channel_key: [func_call]})
    else:
        # check if func_call is already subscribed
        if func_call in _CHANNELS[channel_key]:
            raise PybackError("{0} is already subscribed to {1}"
                              .format(func_call, channel_key))
            return
        else:
            _CHANNELS[channel_key].append(func_call)
# end subscribe


def unsubscribe(channel_key, func_call):
    """
    Static method to remove a func_call from
    a channel.
    """
    channel_key = str(channel_key)

    if channel_key not in _CHANNELS:
        raise PybackError("{0} channel_key does not exist"
                          .format(channel_key))
    else:
        _CHANNELS[channel_key].remove(func_call)
# end unsubscribe


def publish(channel_key, **kwargs):
    """
    Static method for publishing an event.

    kwargs will be set as Evt object
    attributes (setattr()), and the generated
    Evt will be passed back to all registerd
    subscribers.

    If channel_key does not exist, it will be
    ignored as that means there are no subscribers.
    """
    channel_key = str(channel_key)

    if channel_key not in _CHANNELS:
        return
    else:
        # create an Evt instance
        evt = Evt(channel_key, **kwargs)
        for func_call in _CHANNELS[channel_key]:
            # fire each of the callbacks.
            try:
                func_call(evt)
            except:
                # func not avaible at this time.
                # NEEDS A WARNING, NOT AN EXCEPTION
                pass
# end publish


# Instantiated
def Publisher(object):
    """
    Instantiated object for those who require it.
    """
    def __init__(self, channel_key):
        self.channel_key = str(channel_key)

    def publish(**kwargs):
        publish(self.channel_key, **kwargs)
