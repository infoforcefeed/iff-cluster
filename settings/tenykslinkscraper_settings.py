DEBUG = True
SERVICE_NAME = 'tenykslinkscraper'
SERVICE_VERSION = '0.1.0'
SERVICE_UUID = 'cbb1eab8-8567-4ae8-a5d2-7c4e0da002a9'
SERVICE_DESCRIPTION = 'Scrapes links pasted into channels and stores them on shithouse'
ZMQ_CONNECTION = {
    'out': 'tcp://tenyks:61124',
    'in': 'tcp://tenyks:61123'
}
POST_URL_TITLES = True
POST_URLS = {
    "#infoforcefeed": "http://infoforcefeed.shithouse.tv/submit",
    "#olegdb": "http://infoforcefeed.shithouse.tv/submit",
    "#tenyks": "http://infoforcefeed.shithouse.tv/submit",
}
POST_URL_TITLES = {
    "#infoforcefeed": True,
    "#olegdb": True,
    "#tenyks": True,
}
POST_URLS_SALTS = {
    "#infoforcefeed": "KBzzuxJp2hXo4G6MOWCH",
    "#olegdb": "KBzzuxJp2hXo4G6MOWCH",
    "#tenyks": "KBzzuxJp2hXo4G6MOWCH",
}
