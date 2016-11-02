DEBUG = True
SERVICE_NAME = 'TenyksTwitter'
SERVICE_VERSION = '0.1.0'
SERVICE_UUID = '566bab3c-49ad-45e9-afa7-e8635fa5bf64'
SERVICE_DESCRIPTION = 'Takes tweets, scrapes info, post to channel.'
ZMQ_CONNECTION = {
    'out': 'tcp://tenyks:61124',
    'in': 'tcp://tenyks:61123'
}
