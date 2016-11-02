import os

DEBUG = True
SERVICE_NAME = 'wunderground'
SERVICE_VERSION = '0.1.0'
SERVICE_UUID = 'ef223574-0918-42c3-9117-64a1aa56c1a1'
SERVICE_DESCRIPTION = 'I hear whispers'
ZMQ_CONNECTION = {
    'out': 'tcp://tenyks:61124',
    'in': 'tcp://tenyks:61123'
}
WUNDERGROUND_API_KEY = os.environ['WUNDERGROUND_API_KEY']
